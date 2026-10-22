# Acceptance Scenarios

Series: Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
Case: 02  
Author: Yulia Melekhova  
Version: 0.5  
Language: en  
Status: Published

## Purpose
Use these expected behaviors to review or implement the specification. These scenarios have not been executed against an integration.

Unless overridden, events are complete, correctly linked, contract version 1, and have unique IDs; there is no existing reconciliation flag. Omitted dimensions are UNKNOWN. Each case starts independently. Re-baseline scenarios include all validation, authorization, and audit steps in specification.md.

| ID | Check | Given / When | Expected result |
|---|---|---|---|
| AC-01 | OMS completion alone | OMS CLOSED_REFUND_REGISTERED; WMS UNKNOWN; PSP UNKNOWN | AWAITING_CONFIRMATION |
| AC-02 | Warehouse acceptance alone | OMS OPEN; WMS ACCEPTED; PSP UNKNOWN | REFUND_NOT_CONFIRMED |
| AC-03 | Inspection rejected | OMS OPEN; WMS REJECTED; PSP UNKNOWN | RETURN_REJECTED |
| AC-04 | Refund pending | WMS ACCEPTED; PSP PENDING | REFUND_PROCESSING |
| AC-05 | Refund confirmed | WMS ACCEPTED; PSP COMPLETED | REFUND_ISSUED; UI provider-issued label and bank-credit note |
| AC-06 | Refund failed | WMS ACCEPTED; PSP FAILED | REFUND_FAILED |
| AC-07 | Conflicting business facts | WMS REJECTED; PSP COMPLETED | D02; NEEDS_RECONCILIATION; latch flag and open immediate case |
| AC-08 | PSP arrives first | WMS UNKNOWN; PSP COMPLETED, then WMS ACCEPTED | AWAITING_CONFIRMATION, then REFUND_ISSUED |
| AC-09 | Delayed revision | PSP COMPLETED rev 4 accepted; first delivery of PENDING rev 3; WMS ACCEPTED | Ignore valid stale event; REFUND_ISSUED |
| AC-10 | Exact redelivery | Same source and event_id with identical content | No state or audit-outcome duplication |
| AC-11 | Equal revision conflict | PSP rev 2 COMPLETED accepted, then rev 2 FAILED with a new event_id | Retain COMPLETED fact; NEEDS_RECONCILIATION |
| AC-12 | Unknown enum | Linked PSP rev 3 SETTLED on contract version 1 | Retain last valid fact; NEEDS_RECONCILIATION |
| AC-13 | Missing result | Linked WMS COMPLETED without inspection_result | Reject snapshot; NEEDS_RECONCILIATION |
| AC-14 | Wrong refund reference | PSP event uses F-999 for R-204 | Quarantine; do not change R-204 |
| AC-15 | Wrong amount on linked refund | PSP F-204 reports amount_minor=7900 with correct identity; last fact PENDING | Quarantine; retain PENDING baseline; latch D01 NEEDS_RECONCILIATION; immediate case |
| AC-16 | Forbidden issuance regression | PSP COMPLETED rev 2 accepted, then PENDING rev 3 | Retain COMPLETED; NEEDS_RECONCILIATION |
| AC-17 | Snapshot gap | PSP PENDING rev 1, then COMPLETED rev 5; WMS ACCEPTED | Accept full snapshot; REFUND_ISSUED |
| AC-18 | Independent revision spaces | OMS rev 20 OPEN; WMS rev 2 ACCEPTED; PSP rev 1 COMPLETED | REFUND_ISSUED; no cross-source comparison |
| AC-19 | Concurrent updates | WMS ACCEPTED and PSP COMPLETED arrive concurrently | Both facts retained; final REFUND_ISSUED |
| AC-20 | Reconciliation latch | Invalid linked event, then ordinary valid newer snapshot | Conflict remains until recorded authoritative reconciliation |
| AC-21 | Evidence timeout | WMS ACCEPTED makes registration/dispatch evidence due; REFUND_NOT_CONFIRMED persists for 15 minutes | One operations task; no fabricated refund outcome |
| AC-22 | Unsupported contract | Linked source snapshot contract_version=2 | Quarantine; no fact update; NEEDS_RECONCILIATION |
| AC-23 | Changed event identity content | Same PSP event_id reused for a different payload on the same linked refund | Conflict; retain valid fact; NEEDS_RECONCILIATION |
| AC-24 | No evidence | All three dimensions UNKNOWN | RETURN_IN_PROGRESS |
| AC-25 | Contradictory refund closure | OMS CLOSED_REFUND_REGISTERED; WMS REJECTED; PSP UNKNOWN | D02; NEEDS_RECONCILIATION; latch and immediate case |
| AC-26 | Same revision duplicate | New event_id; equal revision and identical business payload | No fact change; no conflict |
| AC-27 | Bank display not confirmed | PSP COMPLETED; WMS ACCEPTED; no bank statement data | REFUND_ISSUED with provider-issued label and bank-credit note |
| AC-28 | Warehouse outcome correction | WMS ACCEPTED rev 2; ordinary REJECTED rev 3; then authoritative re-baseline confirms rev 3; OMS OPEN; PSP UNKNOWN | Initially retain ACCEPTED with reconciliation; audited re-baseline replaces with REJECTED rev 3, clears resolved flag, shows RETURN_REJECTED |
| AC-29 | Normal rejected closure | OMS CLOSED_NO_REFUND; WMS REJECTED; PSP UNKNOWN | RETURN_REJECTED; no reconciliation |
| AC-30 | Inspection in progress | OMS OPEN; WMS PENDING; PSP UNKNOWN | RETURN_IN_PROGRESS |
| AC-31 | Inspection pending; refund pending | OMS OPEN; WMS PENDING; PSP PENDING | AWAITING_CONFIRMATION |
| AC-32 | Inspection pending; refund failed | OMS OPEN; WMS PENDING; PSP FAILED | AWAITING_CONFIRMATION; preserved FAILED fact |
| AC-33 | Inspection unknown; refund failed | OMS OPEN; WMS UNKNOWN; PSP FAILED | AWAITING_CONFIRMATION |
| AC-34 | OMS acceptance transition | OMS OPEN rev 1 → COMPLETED rev 2; WMS ACCEPTED; PSP UNKNOWN | CLOSED_REFUND_REGISTERED; REFUND_NOT_CONFIRMED |
| AC-35 | PSP FAILED terminal change | PSP FAILED rev 2 → COMPLETED rev 3; WMS ACCEPTED | Retain FAILED rev 2; reconciliation until authoritative correction |
| AC-36 | Forbidden early result | WMS IN_PROGRESS with inspection_result=ACCEPTED | Gate B; reconciliation; no WMS fact update |
| AC-37 | Case-sensitive value | WMS COMPLETED with inspection_result=accepted | Gate B; no normalization; reconciliation |
| AC-38 | Missing PSP return_id | Valid refund_id but missing return_id | Gate A; quarantine and incident; no return mutation |
| AC-39 | Conflicting PSP identity | object_id=F-204; payload.refund_id=F-999 | Gate A; no return mutation |
| AC-40 | Wrong linked currency | Correct F-204 identity; currency=EUR | Gate B; retain fact; reconciliation and immediate case |
| AC-41 | Missing event_id on linked WMS | Trusted WMS identity; event_id absent | Gate B; content-hash incident deduplication; reconciliation |
| AC-42 | Missing payload on linked WMS | Trusted WMS identity; payload absent | Gate B; reconciliation |
| AC-43 | Processing timeout | REFUND_PROCESSING reaches its pinned method/provider processing deadline | One payments-operations task; state remains REFUND_PROCESSING |
| AC-44 | Failed refund ownership | WMS ACCEPTED; PSP FAILED | Immediate payments case and customer-support path; no fabricated success |
| AC-45 | Shared evidence timer | AWAITING_CONFIRMATION at t0 → REFUND_NOT_CONFIRMED at t0+10m | Task due at t0+15m, not t0+25m |
| AC-46 | Timer re-entry | Leave shared wait group at t0+5m; re-enter at t0+20m | New interval due t0+35m; retain existing open operations case if any |
| AC-47 | Conflict does not auto-clear | D02 latched; later valid facts happen to align | D01 remains until authoritative resolution |
| AC-48 | Re-baseline changes baseline | Audited WMS REJECTED rev 3 replaces ACCEPTED rev 2; then unseen valid rev 2 snapshot | Ignore lower revision; preserve REJECTED rev 3 |
| AC-49 | Unsafe lower re-baseline | Accepted WMS rev 4; authoritative fetch returns rev 3 | Reject baseline rollback; keep reconciliation |
| AC-50 | Concurrent reconciliation | Projection changes after evidence fetch but before commit | Restart fetch/validation; no stale correction commit |
| AC-51 | Contradiction remains after correction | Corrected WMS REJECTED; PSP COMPLETED still authoritative | Store correction; retain D02 conflict/flag and case |
| AC-52 | No-refund closure before warehouse | OMS CLOSED_NO_REFUND; WMS UNKNOWN; PSP UNKNOWN | AWAITING_CONFIRMATION; WMS REJECTED later gives RETURN_REJECTED |
| AC-53 | No-refund closure vs acceptance | OMS CLOSED_NO_REFUND; WMS ACCEPTED; PSP UNKNOWN | D02; reconciliation with immediate case |
| AC-54 | No-refund closure vs payment | OMS CLOSED_NO_REFUND; WMS UNKNOWN; PSP PENDING | D02; reconciliation with immediate case |
| AC-55 | OMS rejected transition | OMS OPEN rev 1 → CLOSED_NO_REFUND rev 2; WMS REJECTED | RETURN_REJECTED |
| AC-56 | Same issuance state new revision | PSP COMPLETED rev 4 → COMPLETED rev 5; WMS ACCEPTED | Accept rev 5; REFUND_ISSUED |
| AC-57 | Initial terminal full snapshot | First WMS snapshot COMPLETED/REJECTED rev 5; OMS OPEN | Accept full snapshot; RETURN_REJECTED |
| AC-58 | Invalid stale snapshot | Accepted PSP rev 4; linked rev 3 has wrong amount | Quarantine; deduplicated integration incident; keep projection, flags, and baseline unchanged |
| AC-59 | Neutral UI | Projection NEEDS_RECONCILIATION | Neutral EN/RU status-check copy; no internal enum or conflict details |
| AC-60 | Source correction at equal revision | Authoritative payload differs at accepted revision | Re-baseline requires explicit source-owner confirmation and audit |
| AC-61 | Unresolved case escalation | Operations case unresolved for four hours | Escalate to owning lead; persist next four-hour deadline |
| AC-62 | No unowned recovery handoff | Payments operator attempts to close FAILED case without accepting recovery owner/reference | Do not close case; retain ownership and deadline |
| AC-63 | Full-snapshot equality | Same object/revision/payload; different event_id and occurred_at | No fact update and no conflict |
| AC-64 | Rejected path has no refund ID | Registry has no refund object; PSP event claims R-204 | Gate A; incident without mutating the return |
| AC-65 | Initial workflow stall | RETURNS_TEST_V1 deadline reached 24 hours after first observation; physical workflow unfinished | Returns-operations task; no automatic rejection |
| AC-66 | Redelivery of invalid event | Exact repeat of a previously quarantined linked event | Stored failure outcome; no second case or flag |
| AC-67 | OMS terminal regression | OMS CLOSED_NO_REFUND rev 2 → OPEN rev 3 | Gate B terminal regression; retain baseline; reconciliation |
| AC-68 | Early PSP completed with WMS pending | WMS PENDING; PSP COMPLETED | AWAITING_CONFIRMATION; provider evidence retained internally |
| AC-69 | Late provider failure | WMS ACCEPTED; PSP COMPLETED rev 4, then valid FAILED rev 5 days later | Accept rev 5 without re-baseline; REFUND_FAILED; immediate payments case and finance outbox |
| AC-70 | Late failure behind D04 | WMS UNKNOWN; PSP COMPLETED rev 4 then FAILED rev 5 | Preserve FAILED; D04 remains; immediate payments case and finance outbox despite UI state |
| AC-71 | Late failure replay | Exact replay of accepted late FAILED event | Stored outcome; no duplicate finance handoff or task |
| AC-72 | No universal processing deadline | TEST_SLOW policy; PSP PENDING for 15 minutes | No processing-overdue task; use pinned deadline |
| AC-73 | Business-day fixture | TEST_SLOW anchor Friday 2026-10-23 10:00Z; five business days; no holidays | Deadline Friday 2026-10-30 10:00Z; not five elapsed days |
| AC-74 | Missing policy | No approved provider/account/method policy at dispatch | Block submission; configuration case; no generic fallback |
| AC-75 | No deadline reset | Repeated PENDING or D04→REFUND_PROCESSING | Original pending-evidence deadline preserved |
| AC-76 | Crash after provider acceptance | PSP created refund; worker crashes before local ACK; restart query finds it | Bind existing object and acknowledge; no new create |
| AC-77 | Ambiguous not-found | Restart query returns temporarily not found; dedupe guarantee unavailable | MANUAL_REVIEW; no automatic create |
| AC-78 | Expired idempotency retention | Uncertain instruction after dedupe_valid_until | Stop create retries; preserve uncertainty; payments case |
| AC-79 | Retry exhaustion | Create-attempt cap reached without definitive provider outcome | MANUAL_REVIEW; do not invent FAILED |
| AC-80 | Outbox atomicity | OMS transaction rolls back before commit | Neither intent nor outbox row committed; no dispatch |
| AC-81 | Finance unavailable during correction | Authoritative WMS correction with existing PSP issuance; finance endpoint unavailable | Persist true correction and finance outbox; retain reconciliation; retry/escalate handoff |
| AC-82 | No accounting override | Operator changes projection via re-baseline | No journal deletion, debit, collection, or money movement initiated by projection |
| AC-83 | Finance acknowledgment insufficient | Finance accepts case but WMS REJECTED/PSP COMPLETED contradiction remains | Do not clear D02 flag |
| AC-84 | No grace-based compatibility | Deliver WMS REJECTED and PSP COMPLETED in either order | Same D02 contradiction; case is not labeled fraud |
| AC-85 | Different single-refund amount | Trusted instruction amount 12000 USD; PSP full snapshot matches | Amount validation passes; no global 8000 constant |
| AC-86 | Out-of-scope partial aggregate | Two refund objects for one return under one-refund contract | Do not apply D01–D09 as a parent aggregate; require extended object/linkage model |
| AC-87 | Issued state remains monitored | PSP COMPLETED accepted; provider later sends a failure event | Continue subscription and process event; issuance did not close ingestion |
| AC-88 | Concurrent stale worker | Lease expires while original remote request may still run | Fence local writes; any create retry still requires provider concurrent-dedup guarantee |
| AC-89 | Transient lookup failure | UNCERTAIN; first lookup times out or returns retryable 5xx | Keep uncertainty; schedule jittered retry; no new per-operation task yet |
| AC-90 | Lookup throttling | 429 includes valid Retry-After later than computed retry | Do not query before Retry-After; keep original review deadline |
| AC-91 | Lookup review deadline | UNCERTAIN remains for LOOKUP_TEST_V1 four hours | MANUAL_REVIEW and owned overdue item; safe polling continues |
| AC-92 | Provider outage circuit | Five retryable lookup failures in 60 seconds for one account | Open circuit 60 seconds; one probe; aggregate incident; operation deadlines preserved |
| AC-93 | Expired create retention with safe reads | Create guarantee expires; lookup remains available | No create retry; continue bounded read-only lookup with manual ownership |
| AC-94 | Late query error after acknowledgment | Webhook binds object and ACKNOWLEDGED; older query then times out | Keep ACKNOWLEDGED; do not reopen uncertainty from the late error |
| AC-95 | Broker acknowledgment only | Finance broker accepts message; receiver has not accepted ownership | Remain unaccepted; aging and acceptance deadline continue |
| AC-96 | Finance delivery deadline | FINANCE_TEST_V1 one-hour deadline expires without receiver acceptance | Owned incident; bounded retries continue; do not delete event |
| AC-97 | Poison finance record | Receiver deterministically rejects schema | PARKED with reason and owner; retain payload; include in backlog and oldest age |
| AC-98 | Lost finance acknowledgment | Receiver already accepted; sender retries same financial_exception_id | Return existing case; no duplicate financial effects |
| AC-99 | Late finance timeout | FINANCE_ACCEPTED committed; earlier sender timeout arrives | Do not regress accepted state or schedule another delivery |
| AC-100 | Finance outage recovery | Destination recovers with parked/pending backlog | Rate-limited recovery; compare receiver acknowledgments; unaccepted records cannot expire |

| AC-101 | Stale lowercase result | WMS ACCEPTED rev 4 accepted; new event ID, version 1 rev 3 has lowercase accepted | Incident and quarantine only; preserve projection and flags |
| AC-102 | Staleness unprovable | Linked event has malformed revision or unsupported contract despite apparently old timestamp | Latch reconciliation; timestamp cannot prove staleness |
| AC-103 | Old event ID collision | Seen event_id replayed with different content and lower revision | Integrity conflict; latch reconciliation despite low revision |
| AC-104 | PSP terminal regression to pending | PSP FAILED rev 4 then PENDING rev 5 | Retain FAILED; latch reconciliation |
| AC-105 | PSP failure same-state | PSP FAILED rev 4 then valid FAILED rev 5 | Accept baseline rev 5; no new conflict or duplicate entry task |
| AC-106 | WMS same-state and regression | ACCEPTED rev 4 then ACCEPTED rev 5 then IN_PROGRESS rev 6 | Accept rev 5; retain it and latch on rev 6 |
| AC-107 | Unaccepted dispatch | OMS worker sees no authoritative acceptance, or a revoked authorization before an unsent create | Block create; owner investigates; no refund submitted |
| AC-108 | Physical inspection wait | O=OPEN, W=PENDING, P=UNKNOWN for 15 minutes | D09; no integration-evidence timeout; returns-policy deadline applies |
| AC-109 | Accepted but no instruction | O=OPEN, W=ACCEPTED, P=UNKNOWN | D08 neutral UI; after 15 minutes check OMS registration before PSP |
| AC-110 | Rejected with failed refund | W=REJECTED; reliably linked PSP FAILED | D02; process case and finance assessment; no asserted loss or mandatory posting |
| AC-111 | D04 parentheses happy path | O=CLOSED_REFUND_REGISTERED, W=ACCEPTED, P=COMPLETED | D05 REFUND_ISSUED; D04 false |
| AC-112 | Store refusal outside scope | Store declines request before warehouse inspection | Do not encode as CLOSED_NO_REFUND in this contract; separate outcome/model required |

---
Inside the Spec · Real Scenarios. Working Artifacts. Decisions That Matter.
https://github.com/YuliaMelekhova/inside-the-spec
https://www.linkedin.com/in/yuliamelekhova
