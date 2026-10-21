A Payment Timeout Is Not a Failed Payment

A customer adds €50 to a balance. The request times out. The screen offers “Try again.” What should that button do?

If no status response or operation ID arrived, it can replay POST with the original key within the retry budget. Once the client receives a status object or knows the ID, the button becomes “Check status” and reads the existing payment with GET.

This illustrative case opens Inside the Spec – Realistic Scenarios. Working Artifacts. Decisions That Matter.

Case 01 follows one top-up through retries, late confirmation, and balance credit. The key artifacts include state models, transition rules, an idempotency contract, and acceptance scenarios. The chosen instrument requires no user interaction; €50 is an example, not an assumption about an EU card flow.

The specification separates three related dimensions: payment outcome, balance-credit progress, and review. An open review can be nonblocking. A security hold blocks new credit dispatch, while a confirmed posting remains a fact.

Uncertainty applies to both payment and credit. Suppose the provider confirms success, the balance service creates a posting, and its response is lost. A hold then opens. The credit outcome stays unknown until verified; “held” would hide the possible posting. Read-only lookup by payment_id continues while new writes are paused.

Idempotency means a repeat has no additional effect within a defined scope. Here, retries after an ambiguous provider call rely on the same provider key and a verified 24-hour guarantee covering concurrent requests. A separate check blocks a new key with matching payment details while the original remains unresolved. Once the provider confirms that its operation exists, further create attempts are prohibited.

Durable jobs and a watchdog resume interrupted work. A never-dispatched request can be closed locally; a possibly sent request needs evidence. Neither an expired timer nor “not found” proves financial failure.

The credit goal includes progress: eventually exactly one posting, never more. That requires blocking holds to be resolved, valid tasks to remain recoverable, workers to keep processing, and the balance service to recover and accept the operation.

The carousel presents the decisions. GitHub contains the full specification, editable tables and diagrams, and 58 acceptance scenarios. These define expected behavior, not executed implementation tests. Real integration guarantees still need verification.

Links to the English and Russian materials are in the comments.

#SystemsAnalysis #RequirementsEngineering #Payments
