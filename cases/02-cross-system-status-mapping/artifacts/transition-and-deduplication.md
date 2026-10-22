# Source Transitions and Event Identity

Series: Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
Case: 02  
Author: Yulia Melekhova  
Version: 0.5  
Language: en  
Status: Published

## Purpose
Define complete ordinary transition rules and event-ID handling. These tables apply after identity/content/revision gates; re-baseline is an audited exception.

## Source transitions
All entries below require a strictly higher valid revision. Same-state means identical status and inspection result; other valid payload fields still undergo full validation. First valid full snapshots can establish any dictionary state because this consumer may start late.

| Source | From raw state | To raw state | Outcome |
|---|---|---|---|
| OMS | OPEN | OPEN | Accept newer revision |
| OMS | OPEN | COMPLETED or CLOSED_NO_REFUND | Accept |
| OMS | COMPLETED | COMPLETED | Accept newer revision |
| OMS | CLOSED_NO_REFUND | CLOSED_NO_REFUND | Accept newer revision |
| OMS | Either closed state | OPEN or the other closed state | Retain baseline; latch reconciliation |
| WMS | IN_PROGRESS | IN_PROGRESS | Accept; inspection_result must be absent |
| WMS | IN_PROGRESS | COMPLETED/ACCEPTED or COMPLETED/REJECTED | Accept |
| WMS | COMPLETED/ACCEPTED | COMPLETED/ACCEPTED | Accept newer revision |
| WMS | COMPLETED/REJECTED | COMPLETED/REJECTED | Accept newer revision |
| WMS | Either completed result | IN_PROGRESS or opposite result | Retain baseline; latch reconciliation |
| PSP | PENDING | PENDING, COMPLETED, or FAILED | Accept |
| PSP | COMPLETED | COMPLETED or FAILED | Accept; FAILED is a valid late outcome |
| PSP | COMPLETED | PENDING | Retain baseline; latch reconciliation |
| PSP | FAILED | FAILED | Accept newer revision |
| PSP | FAILED | PENDING or COMPLETED | Retain baseline; latch reconciliation |

## Event identity and revision
| Input after identity gate | Outcome |
|---|---|
| Same source/event_id; identical parsed event | Return stored outcome, including previous rejection |
| Same source/event_id; changed content at any revision | Integrity conflict; preserve facts; latch reliably bound return(s) |
| Missing/malformed event_id | B conflict; incident deduplicated by source object/content hash |
| New ID; lower comparable revision; valid content | Stale no-op |
| New ID; lower comparable revision; invalid content | Quarantine and incident only; preserve projection and flags |
| New ID; unsupported contract or invalid revision | Cannot establish staleness; B conflict |
| New ID; equal revision and equal valid business payload | No-op |
| New ID; equal revision but different payload | B conflict |
| New ID; higher revision, valid content | Apply transition table |

Stale classification requires the supported version-1 envelope and its revision semantics. It cannot suppress an event-ID integrity conflict. All outcomes retain replay protection.

---
Inside the Spec · Real Scenarios. Working Artifacts. Decisions That Matter.
https://github.com/YuliaMelekhova/inside-the-spec
https://www.linkedin.com/in/yuliamelekhova
