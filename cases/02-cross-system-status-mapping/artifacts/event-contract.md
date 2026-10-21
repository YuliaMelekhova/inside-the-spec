# Event Contract

Series: Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
Case: 02  
Author: Yulia Melekhova  
Version: 0.4  
Language: en  
Status: Draft

## Purpose
Define the illustrative snapshot contract and the validation boundary. This is an assumed adapter contract, not documentation of an existing provider.

All events are JSON objects with envelope fields and a nested payload object. Additional fields are invalid in contract version 1. Optional means absent; null is not valid. Strings are nonempty and case-sensitive, without normalization. Integer fields exclude booleans.

| Field | Type | Required / constraint | Failure class |
|---|---|---|---|
| source_system | string | OMS, WMS, PSP; must match authenticated channel | A |
| object_type | string | return_request, inspection, refund respectively | A |
| object_id | string | Exact object in trusted OMS linkage | A |
| return_id | string | Required in every event, including PSP; must match linkage | A |
| payload.refund_id | string | Required for PSP; equals object_id and linked refund ID; forbidden otherwise | A if missing/mismatched for PSP; B if extra elsewhere |
| event_id | string | Required, immutable per source; nonempty | B |
| revision | integer | Required, >=1; monotonically increases per source object | B |
| contract_version | integer | Required; supported value 1 | B |
| occurred_at | string | Required RFC 3339 UTC timestamp; diagnostics only | B |
| payload | object | Required; all applicable fields below | B unless missing PSP refund identity prevents A |
| payload.status | string | Required; dictionary enum for this object | B |
| payload.inspection_result | string | WMS COMPLETED only; ACCEPTED or REJECTED; required there | B |
| payload.amount_minor | integer | PSP only, required; equal to registered expected amount; 8000 for example F-204 | B |
| payload.currency | string | PSP only, required; equal to registered currency; USD for example F-204 | B |

Class A: identity cannot be trusted. Quarantine, create an integration-operations incident, and change no return fact or return flag. Authentication failure, unreadable JSON, missing routing fields, unknown object, or inconsistent linkage belongs here. Do not guess a return from an untrusted return_id.

Class B: identity is reliably bound but content is invalid. Quarantine the event, keep the last valid fact and baseline, latch the linked return's reconciliation flag, recompute D01, and create an immediate operations case. Wrong amount or currency belongs here. Unknown contract versions are B when the stable identity envelope is still readable and trusted; otherwise A.

The trusted registry is established by OMS before dispatch. For a rejected return it has R-204 and I-204 but no refund ID. The accepted path adds F-204 with expected amount and currency before submission. Updates to this registry are authenticated control operations, not inferred from incoming status events.

Full snapshots contain all applicable fields. A revision gap is allowed. The comparable business payload consists of the four identity fields, contract_version, and the complete payload object, with JSON key order ignored. event_id and occurred_at do not affect same-revision equality. For identical-event redelivery compare the whole parsed event including those fields, ignoring JSON key order.

## Valid PSP snapshot
```json
{
  "source_system": "PSP",
  "object_type": "refund",
  "object_id": "F-204",
  "return_id": "R-204",
  "event_id": "psp-F-204-4",
  "revision": 4,
  "contract_version": 1,
  "occurred_at": "2026-10-21T09:04:00Z",
  "payload": {
    "refund_id": "F-204",
    "status": "COMPLETED",
    "amount_minor": 8000,
    "currency": "USD"
  }
}
```


## Provider adapter obligations
COMPLETED is an illustrative adapter value, not a universal PSP enum. Map it only from evidence meeting this case's issuance meaning. A mere request receipt is PENDING. The adapter must consume subsequent refund-failure notifications and authoritative status queries; a confirmed late failure emits a newer full FAILED snapshot for the same object. Do not discard it because issuance was observed earlier.

If native PSP events lack monotonic revisions/full snapshots, the adapter must reconcile them against authoritative state and maintain an auditable revision stream. Assigning increasing revisions solely by webhook arrival order is insufficient. A provider contract that cannot support authoritative ordering needs a redesigned adapter before onboarding.

Payment method, provider/account, policy version, and deadlines are trusted registry/dispatch metadata defined in operational-contract.md. They are not inferred from status strings and are not new fields in this version-1 source snapshot envelope. Financial handoff records and dispatch attempts use their own internal contracts. This specification does not claim that all PSPs use the illustrated identifiers or states.


---
Inside the Spec · Real Scenarios. Working Artifacts. Decisions That Matter.
https://github.com/YuliaMelekhova/inside-the-spec
https://www.linkedin.com/in/yuliamelekhova
