# Cross-System Status Mapping

Series: Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
Case: 02  
Author: Yulia Melekhova  
Version: 0.3  
Language: en  
Status: Draft

## Purpose
Use this illustrative specification to review status meaning, ownership, and aggregation across a return workflow. Version 0.3 addresses the review of the initial draft; it is not a description of a deployed integration.

## Scope and actors
One return contains one item, one inspection, and at most one full refund of USD 80.00. OMS manages the request and owns trusted object linkage and expected refund amount. WMS owns inspection evidence. PSP owns refund-processing evidence. The integration holds a derived read projection, not a new business authority.

OMS has a dispatch worker. After acceptance, OMS atomically registers refund intent, linkage, and a durable dispatch record before closing as COMPLETED. The worker submits the instruction to PSP. It reuses the same refund ID and provider-supported idempotency key on submission retries; after an ambiguous response it queries PSP before retrying. The key's scope is this one refund instruction, not all payments. A provider contract without safe deduplication/query support requires a different dispatch design. The detailed crash-recovery contract is in operational-contract.md. Transactional Outbox guarantees durable intent, not exactly-once execution at PSP.

The rejected path closes in OMS as CLOSED_NO_REFUND, without a refund instruction. UNKNOWN, OPEN, CLOSED_REFUND_REGISTERED, and CLOSED_NO_REFUND are the four projected OMS states. UNKNOWN means no valid snapshot, not an actual OMS state.

Source adapters emit complete snapshots, immutable event IDs, and monotonically increasing revisions per object. Revisions are never compared across sources. Delivery order can differ from source order. Only contract version 1 is supported. See event-contract.md for all fields and validation outcomes.

Partial returns, new refund attempts, chargebacks, and actual bank-statement confirmation are outside scope. Provider-confirmed failure after issuance is included. A provider-confirmed refund reversal may be normalized to FAILED for this customer projection, while its original reason and financial evidence remain distinct in the adapter audit and finance workflow. Do not treat a chargeback as the same event as a failed refund. A terminal FAILED object is not retried as a new refund in this case; recovery must be handed to an owned exception process. These limits do not remove the operations task or customer support path.

## Source dictionary (generated)
<!-- dictionary:start -->
| Source / object | Raw status | Required result | Target fact | Terminal | Meaning |
|---|---|---|---|---|---|
| OMS / return_request | OPEN | (absent) | return_state=OPEN | false | Return workflow open |
| OMS / return_request | COMPLETED | (absent) | return_state=CLOSED_REFUND_REGISTERED | true | Item accepted and refund instruction registered |
| OMS / return_request | CLOSED_NO_REFUND | (absent) | return_state=CLOSED_NO_REFUND | true | Rejected return closed without a refund instruction |
| WMS / inspection | IN_PROGRESS | (absent) | inspection_state=PENDING | false | Inspection in progress; no result yet |
| WMS / inspection | COMPLETED | ACCEPTED | inspection_state=ACCEPTED | true | Inspection finished; item accepted |
| WMS / inspection | COMPLETED | REJECTED | inspection_state=REJECTED | true | Inspection finished; item rejected |
| PSP / refund | PENDING | (absent) | refund_state=PENDING | false | Provider processing refund |
| PSP / refund | COMPLETED | (absent) | refund_state=COMPLETED | false | Provider confirms refund issued; a later failure is possible; bank credit not independently confirmed |
| PSP / refund | FAILED | (absent) | refund_state=FAILED | true | Provider reports initial or post-issuance refund failure; no conclusion about recovered funds |
<!-- dictionary:end -->

The CSV is authoritative. is_terminal applies to ordinary ingestion, not bank-settlement finality. REFUND_ISSUED is an observation of provider issuance and is not an absorbing success state. Newer authoritative PSP FAILED must update it without a manual re-baseline, including days later. Missing dimensions default to UNKNOWN. An accepted snapshot can update only its source dimension.

## Event processing, in order
1. **Identity gate A.** Authenticate source and validate stable routing/linkage, including return_id and PSP refund_id. A failure is quarantined with an integration incident and no return mutation. A trusted identity must be established before any customer-specific flag is set.
2. **Redelivery identity.** For a valid nonempty event_id, inspect (source_system, event_id). An exact repeat returns the stored ingestion outcome without creating another flag, case, or audit outcome. Changed content under that identity is a B conflict; retain all existing facts. If both the previously bound return and the newly bound return differ, flag both reliably identified returns for review. Missing/malformed event_id proceeds to gate B and cannot use event-ID deduplication; deduplicate its incident by source object and raw-content hash.
3. **Content gate B.** Validate the envelope and full payload against event-contract.md, including contract version, revision type, amount, currency, and dictionary values. On failure, retain the fact and baseline, quarantine, latch reconciliation, and open an immediate case. This check precedes revision comparison, so malformed older events are still reported. A redelivery of an already handled invalid event remains a no-op.
4. **Revision gate.** Compare only within the bound source object. A valid lower revision is stale and cannot update the fact. An equal revision with identical comparable business payload is a no-op; different content is a latched B conflict. A higher revision proceeds to transition validation. Full snapshots permit revision gaps.
5. **Transition gate.** A first valid snapshot may establish any dictionary state. Ordinary transitions are OMS OPEN→COMPLETED or OPEN→CLOSED_NO_REFUND; WMS IN_PROGRESS→COMPLETED with one result; PSP PENDING→COMPLETED, PENDING→FAILED, or COMPLETED→FAILED. PSP COMPLETED is not terminal; COMPLETED→PENDING remains an invalid transition, but COMPLETED→FAILED is a normal late outcome, not a manual correction. A higher-revision repeat of an unchanged state/result is valid. Terminal sets are defined in the CSV. A terminal outcome change or regression is a B conflict and retains the baseline until reconciliation, even when its revision is higher.
6. **Commit.** Atomically persist accepted fact, baseline revision, mapping version, ingestion outcome, audit evidence, recomputed projection, timer changes, and task-outbox records. Serialize by return or use optimistic concurrency with retry. No accepted concurrent update may erase another dimension.
7. **Reconciliation.** Flags are latched. New ordinary events may update valid dimensions but cannot clear the flag. An operator must use the authoritative re-baseline procedure below. Cross-source contradictions under D02 also latch a flag and create an immediate case; they are not treated as harmless delivery lag.

All ingestion outcomes need durable replay protection. Retention duration and replay horizon must be agreed before deployment. Timestamps are diagnostic, not precedence rules.

## Projection decisions: first matching rule wins
Let O=return_state, W=inspection_state, P=refund_state. “P known” means P is one of PENDING, COMPLETED, FAILED, equivalently P != UNKNOWN. F means an unresolved latched reconciliation flag.

| Rule | Condition | Projection enum |
|---|---|---|
| D01 | F=true | NEEDS_RECONCILIATION |
| D02 | (W=REJECTED and (P known or O=CLOSED_REFUND_REGISTERED)) OR (O=CLOSED_NO_REFUND and (P known or W=ACCEPTED)) | NEEDS_RECONCILIATION |
| D03 | W=REJECTED | RETURN_REJECTED |
| D04 | (W in UNKNOWN,PENDING and (P known or O=CLOSED_REFUND_REGISTERED)) OR (O=CLOSED_NO_REFUND and W in UNKNOWN,PENDING) | AWAITING_CONFIRMATION |
| D05 | W=ACCEPTED and P=COMPLETED | REFUND_ISSUED |
| D06 | W=ACCEPTED and P=FAILED | REFUND_FAILED |
| D07 | W=ACCEPTED and P=PENDING | REFUND_PROCESSING |
| D08 | W=ACCEPTED and P=UNKNOWN | REFUND_NOT_CONFIRMED |
| D09 | Otherwise | RETURN_IN_PROGRESS |

D02 emits a reconciliation flag in the same transaction; record D02 as the triggering decision, then subsequent evaluations select D01 until resolution. D04 is missing evidence, not contradictory terminal evidence. It may clear automatically when the missing snapshot arrives. D02 never auto-clears just because new facts happen to align. REJECTED is final inspection evidence under this contract. Delivering PSP completion before or after that rejection yields the same contradiction; neither fact becomes compatible by waiting. This is an exception requiring explanation, not a fraud conclusion. Missing evidence is handled by D04. No grace window or HLC is introduced: cross-source clocks cannot establish business compatibility. A domain with provisional rejection or repeated inspections requires explicit outcomes or attempt IDs and different rules.

Case decision: warehouse acceptance is a prerequisite for showing REFUND_ISSUED, even when PSP completion arrived first. OMS OPEN is only workflow lag and is not a success gate. This intentionally favors consistent return evidence over immediately displaying an early provider result. It does not deny or overwrite that result, which remains available to operations. A confirmed OMS no-refund closure is substantive evidence and does trigger D02 when contradictory.

REFUND_NOT_CONFIRMED says no valid PSP snapshot has arrived; it does not assert that submission never occurred. Projection enums are internal API values. Use display-mapping.md for all UI copy; never render enum names directly.

## Authoritative re-baseline
1. The reconciliation owner fetches the current snapshot directly from the authenticated source object API, not from the disputed event queue. Fetch other implicated sources and trusted linkage for cross-source conflicts. Correct the source/registry through its own authorized workflow first if necessary.
2. Validate identity, supported contract, full payload, amount, and currency. A baseline correction requires a revision >= the current accepted revision. A lower revision cannot roll back the baseline; the source must issue a new authoritative revision. Equal revision with changed payload requires explicit source-owner confirmation of a source correction. Unsupported contracts require a supported adapter/mapping change before resolution.
3. Record case ID, operator, source-owner confirmation where required, reason, fetched evidence, and before/after payloads and revisions. Under a per-return lock, reread current revisions and flags; if they changed since fetch, restart. Newer invalid events are included in the case and cannot be silently discarded.
4. Atomically replace the implicated facts and baseline revisions with validated authoritative values, explicitly bypassing the ordinary transition gate for this audited correction. WMS ACCEPTED rev 2 may therefore be replaced by authoritative REJECTED rev 3. Do not compare the corrective snapshot to the ordinary transition graph.
5. Recompute all contradictions. Resolve addressed flags only if evidence covers them, D02 is false, and any required financial-exception handoff has an accepting finance owner and case acknowledgment. Otherwise retain reconciliation and the open case. Corrected facts may still be stored while unresolved conflicts remain. Record decision, projection, timer changes, and resolution result. Subsequent normal events compare against the new baseline; prior event outcomes remain in the audit log.

An operator cannot clear D02 with a comment alone. If no consistent authoritative state can be obtained, the case stays assigned and is escalated under the operations policy below. Financial exceptions require the durable finance handoff defined in operational-contract.md. The integration cannot post ledger entries or initiate debt collection. Correct observations must still be recorded; resolution is blocked until the required financial handoff is acknowledged.

## Worked sequence
All event IDs below are distinct and all snapshots are valid and correctly linked.

| Arrival | Event / snapshot | Projection and outcome |
|---|---|---|
| 1 | oms-1: OMS OPEN rev 1 | RETURN_IN_PROGRESS |
| 2 | wms-2: WMS COMPLETED / ACCEPTED rev 2 | REFUND_NOT_CONFIRMED |
| 3 | oms-2: OMS COMPLETED rev 2 | REFUND_NOT_CONFIRMED |
| 4 | psp-1: PSP PENDING rev 1 | REFUND_PROCESSING |
| 5 | psp-4: PSP COMPLETED rev 4 | REFUND_ISSUED |
| 6 | psp-3: PSP PENDING rev 3, first delivery | REFUND_ISSUED; stale revision |
| 7 | psp-4: identical redelivery of arrival 5 | REFUND_ISSUED; stored outcome, no-op |

## Operations, ownership, and exit
Thresholds are explicit illustrative assumptions, not provider SLAs. Timers use durable ingestion time, survive restarts, and never fabricate a business outcome. Tasks are idempotent by (return_id, reason, unresolved_interval_id); route changes update the same open case.

| Condition | Start / threshold | Owner and action | Exit |
|---|---|---|---|
| AWAITING_CONFIRMATION or REFUND_NOT_CONFIRMED | One shared evidence-wait interval; task after 15 minutes | Integration operations checks WMS/OMS; payments operations checks dispatch and PSP; integration operations owns coordination | Valid evidence leaves this group, or handoff to reconciliation |
| REFUND_PROCESSING | Persisted method/provider policy deadline; no universal 15-minute default | Payments operations queries PSP, checks its processing status, and contacts provider support | Valid issuance/failure snapshot; monitoring then follows that stage |
| REFUND_FAILED | Immediate task on entry | Payments operations investigates and gives customer support a tracked recovery case | Source correction via re-baseline, or documented transfer to the separately owned recovery process; the truthful FAILED fact remains until evidence changes |
| D01 or D02 | Immediate case | Integration operations owns reconciliation; source owner supplies authoritative evidence; payments operations joins money-related conflicts | Valid re-baseline and resolution, or explicit external recovery handoff with reconciliation flag retained |
| RETURN_IN_PROGRESS | Task after 24 hours from first entry without resolution | Returns operations checks request and inspection progress | Valid evidence changes projection or a recovery handoff |
| RETURN_REJECTED | No new timer | Normal rejected-return outcome | New contradictory evidence opens reconciliation |
| REFUND_ISSUED | Method/provider visibility-check deadline; event monitoring continues | Payments operations monitors later outcomes and investigates missing bank visibility when due | Newer PSP FAILED updates the projection; financial-exception handling continues |

Switching between AWAITING_CONFIRMATION and REFUND_NOT_CONFIRMED does not reset the shared timer. Remaining in any timed state also does not reset its timer. Leaving a timer group closes its interval; later re-entry starts a new interval, while any already open operations case is retained and updated. REFUND_PROCESSING uses its own policy deadline anchored to the first valid PSP PENDING observation, even if D04 or D01 currently masks it. REFUND_ISSUED monitoring is anchored to first valid PSP COMPLETED evidence on the same basis. Repeated snapshots and UI projection changes never reset these deadlines. See operational-contract.md for the precedence of these source-fact monitors over display-state timers. Re-baseline uses these same rules.

Open operations cases have a four-hour review deadline from creation. If unresolved at that deadline, escalate to the owning team lead and record the next four-hour review deadline. An external recovery handoff requires an accepting owner and case reference; it does not relabel the original refund as successful. Handoffs and escalations are persisted, deduplicated, and auditable. These non-payment task-review targets are case assumptions to replace with agreed operational targets before deployment. Payment processing and visibility deadlines use the mandatory versioned policy profile, not these fixed task-review intervals.

## Audit and boundaries
Record raw event, source identity, revision, outcome, mapping_version, before/after facts, triggering decision, projection, flags, timer interval, task references, and corrective evidence. Restrict raw events and reconciliation details to authorized staff.

Separating dimensions preserves meaning but adds aggregation and operational responsibilities. A single shared status is suitable only where object and completion conditions genuinely coincide. Source contract verification, retention, authentication, and production service objectives remain deployment prerequisites.


---
Inside the Spec · Real Scenarios. Working Artifacts. Decisions That Matter.
https://github.com/YuliaMelekhova/inside-the-spec
https://www.linkedin.com/in/yuliamelekhova
