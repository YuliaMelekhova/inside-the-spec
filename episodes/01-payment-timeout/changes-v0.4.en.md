# Case 01 review changes: specification 0.4

Inside the Spec – Realistic Scenarios. Working Artifacts. Decisions That Matter.

Status: Draft. The previous revision is retained in Git history.

| Review point | Resolution |
|---|---|
| Related statuses, source of truth | M-01 complete credit enum and allowed combinations; review_items owns reasons, blocking_review_reasons is derived |
| Lost credit response followed by hold | CR-01–CR-03 DISPATCHING / OUTCOME_UNKNOWN; hold stops new writes, not read-only lookup or recording a posting |
| Stuck CREATED / PROCESSING | WR-01 durable jobs, watchdog, leases, safe never-dispatched expiry, owned handoff |
| Recovery clock / create safety | RP-01 absolute offsets; independent one-hour deadline; defensive 23-hour bound; PA-01 primary ambiguous-retry guarantee |
| Webhook rejects and rotation | WH-01 authenticated quarantine, explicit responses, old-key overlap and emergency revocation; basic rotation already existed in 0.3 |
| Client-key storage | KEY-01 operation-lifetime binding and minimum periods after full resolution; unresolved retention was already present in 0.3 |
| HTTP mapping | API-01 intentionally differs from IETF draft-07: changed payload 409, nonfinal replay 202 |
| Verified provider pending | IC-14 monotonic provider_operation_seen; permanent ban on new CREATE authorization |
| No user interaction | Scenario assumptions and carousel; EUR is illustrative and implies no SCA exemption |
| Post and carousel consistency | Button POST/GET rule, key artifacts, three related dimensions, conditional liveness, ID legend, explained six-minute example |

AC-01–AC-40 retain stable IDs with clarifications. AC-41–AC-58 cover new boundaries. These are expected results, not executed implementation tests. Provider and balance capabilities and the SLO remain unverified for a real integration.

Both language carousels contain 15 pages at the agreed typography. Case links target this review branch until merge and a verified main-link update. No LinkedIn publication is claimed.

---

Inside the Spec – Realistic Scenarios. Working Artifacts. Decisions That Matter.  
https://github.com/YuliaMelekhova/inside-the-spec  
https://www.linkedin.com/in/yuliamelekhova
