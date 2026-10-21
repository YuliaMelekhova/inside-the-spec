# Dispatch, Monitoring, and Financial Exceptions

Series: Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
Case: 02  
Author: Yulia Melekhova  
Version: 0.3  
Language: en  
Status: Draft

## Purpose
Specify operational safeguards around the three-source projection without turning it into a universal payments or accounting system. Numeric examples below are synthetic test policies, not claims about payment-network service levels.

## Payment policy and durable deadlines
Before dispatch, the trusted registry must select an approved policy by provider, merchant account, payment method/rail, region, and currency. Method alone may be insufficient. Persist policy_id, policy_version, calendar_id, timezone, processing_duration, processing_clock_kind (elapsed or business), visibility_duration, visibility_clock_kind, polling_interval, retry_policy_id, and the resolved absolute UTC deadlines with their calculation inputs. No match blocks dispatch and opens a configuration case; never silently use a generic 15-minute policy.

Processing monitoring starts at the first valid PSP PENDING ingestion, independent of the displayed projection. Issuance/visibility monitoring starts at the first valid PSP COMPLETED ingestion. Persist the anchors even if an earlier prerequisite is missing. A direct first snapshot COMPLETED has no pending interval. Later FAILED cancels the active processing/visibility timers and creates an immediate payments case, even if D01/D02 masks REFUND_FAILED. An authoritative correction can change the anchor only with recorded evidence and explicit audit; ordinary re-delivery and re-baseline without such a correction cannot reset it.

The processing deadline means provider processing is overdue for the configured contract. The visibility deadline prompts a status/trace check, not an automatic conclusion that funds arrived or failed. Bank visibility and provider processing are different stages. Missing-bank-credit reports may create a case earlier through support.

Durations use the pinned calendar version and timezone. Business durations count only configured business dates, preserve the local anchor time, and skip listed holidays; the policy must specify any cutoff and daylight-saving rule. Persisting the UTC deadline avoids recomputation on each event. Configuration changes do not rewrite running deadlines without a recorded migration. For a reproducible fixture, TEST_SLOW uses UTC, Monday–Friday, no holidays, no cutoff, and five business days: Friday 2026-10-23 10:00Z → Friday 2026-10-30 10:00Z. TEST_FAST uses 15 elapsed minutes. These fixtures are not mappings for any real payment method. The run's model checker does not execute calendar arithmetic.

Keep late-outcome subscriptions active after REFUND_ISSUED. Poll at the pinned policy interval when webhooks are missing or delayed. Onboarding must define the provider's late-outcome/replay horizon and retention for linkage and deduplication; absence of that agreement blocks production use. An expiry does not prove bank receipt. Late events beyond a configured horizon create an incident and follow identity validation and exception handling; they are not silently dropped.

The original 15-minute evidence-wait timer concerns integration/dispatch evidence only, not expected bank completion. It creates a diagnostic task and cannot mark a refund failed. Deduplicate/merge tasks into the current return case so overlapping monitors do not flood operations.

## Transactional Outbox and attempt contract
In one OMS database transaction, commit the refund instruction, immutable linkage/amount/currency, policy reference, and outbox row. A unique business instruction ID prevents creating another instruction for the same one-refund operation.

Store instruction_id, outbox_id, return_id, internal_refund_id, original_payment_id, provider, merchant_account, idempotency_key, request_hash, state, lease_token, lease_until, attempt_count, first_attempt_at, next_attempt_at, dedupe_valid_until, provider_refund_id, and acknowledged_at. provider_refund_id starts absent; a native provider ID need not equal the internal F-204. A verified adapter binding connects them. Append each attempt's attempt_id, start/end time, provider_request_id if available, response/error classification, and response digest. Increment attempt_count durably before each create call, not after its result. Queries have separate query-attempt records and do not create another instruction.

States are READY, IN_FLIGHT, UNCERTAIN, ACKNOWLEDGED, and MANUAL_REVIEW. A leased worker moves READY→IN_FLIGHT before sending. A valid provider response or linked webhook can record ACKNOWLEDGED with the native provider object reference. ACKNOWLEDGED means that the external object is identified, not that the refund succeeded; business state still follows validated PSP snapshots. A local timeout or expired lease from IN_FLIGHT becomes UNCERTAIN, never blind READY.

After a crash between provider acceptance and the local acknowledgment, query by the stable merchant reference/key and known native ID. If the object exists, bind it and acknowledge without another create. A temporary 'not found' from an eventually consistent query does not establish that the first call failed. Retry a create only within verified deduplication scope/retention, with the identical key, account, endpoint, and request body, under a contract that safely deduplicates concurrent calls. Otherwise enter MANUAL_REVIEW. Do not rotate keys to resolve an ambiguous result.

The provider contract must define key scope, retention, parameter matching, concurrent-request behavior, query consistency/visibility, and which errors are definitive non-execution. Onboarding checks these guarantees. Outbox, counters, and leases cannot compensate for a PSP that violates them. When guarantees are absent or expired, stop automatic create retries and reconcile rather than claim exactly-once execution.

Pin a retry policy with max_create_attempts, maximum_elapsed_time, backoff schedule, and jitter bounds. Limit all retries by dedupe_valid_until as well. Exhaustion opens MANUAL_REVIEW with a payments owner, preserving uncertainty; it does not set PSP FAILED. Serialize dispatch locally and fence stale local updates, but do not treat a local lease as protection against an already-running remote request.

## Financial exception boundary
Re-baseline changes an observation in the read projection; it is not a money movement, accounting reversal, or permission to recover money from a customer. Do not block recording truthful source evidence merely because ERP is unavailable.

Atomically with a financially consequential correction, persist a financial_exception_id and durable finance-outbox record. A correction is consequential when it changes an implicated return/inspection outcome while a PSP object exists or a dispatch attempt may have reached PSP, changes a PSP outcome, or addresses a money-related conflict. Normal accepted late PSP FAILED also creates this record. Use (return_id, triggering_ingestion_or_resolution_id, exception_kind) for idempotence. Include original payment/refund IDs, instruction and attempt references, amount/currency, before/after facts and revisions, provider evidence references, and reconciliation case ID. It records exposure for assessment, not an asserted loss or receivable.

Finance operations owns the receiving case. The receiving ledger/ERP process determines whether journal entries or an adjustment are needed from accounting evidence and its posting rules. It returns a case acknowledgment with ledger references where applicable, or a documented no-posting decision. All receiving actions must be idempotent. The projection layer does not choose debit/credit accounts or initiate a charge or collection.

If the finance service is unavailable, persist the correction and pending handoff locally, retain the reconciliation flag, retry the finance outbox, and escalate to finance operations after the existing four-hour case-review deadline. A normal late failure may show REFUND_FAILED immediately when D02 is false, while its payments/finance case stays open. For re-baseline, the parent reconciliation case cannot close until finance has accepted ownership; substantive ledger completion may remain tracked in that accepted finance case. D02 must also be false before its projection flag clears. Acknowledging the handoff alone does not erase a remaining business contradiction.

Any recovery, compensation, or write-off requires an authorized business/accounting decision. A warehouse rejection does not by itself establish a collectible debt or prove defective goods. Historical events and journal entries are never overwritten by re-baseline.

## Extension boundary
USD 80.00 is one worked amount. Validation compares events to the registered expected amount and currency; it must not hardcode 8000 or USD globally. A single-refund example at a different amount does not require new status enums.

Multiple partial refunds need a parent payment and a collection of refund instructions/attempts, item allocation, amount aggregation, and concurrency control over refundable balance. Tax, shipping deductions, fees, and FX require explicit amount components and currency-specific invariants. Do not sum unlike currencies or equate gross customer refunds with net merchant balance effects. Item receipt/rejection may also need its own per-item model.

Per-refund status mapping can be reused where provider semantics match. Parent-level completion and consistency rules must be designed separately. D01–D09 must not be copied as the aggregate rule for multiple items/refunds. This is a bounded status-mapping case, not a production-ready general refund architecture.


---
Inside the Spec · Real Scenarios. Working Artifacts. Decisions That Matter.
https://github.com/YuliaMelekhova/inside-the-spec
https://www.linkedin.com/in/yuliamelekhova
