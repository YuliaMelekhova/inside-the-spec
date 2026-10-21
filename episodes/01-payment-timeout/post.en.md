A Payment Timeout Is Not a Failed Payment

A customer adds €50 to a balance. The request times out. The screen offers “Try again.”

Before specifying that button, an analyst has to answer a question the timeout leaves open: did the provider accept the payment?

This illustrative case opens Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.

Case 01 follows the same top-up through a repeated request, a late confirmation, and balance credit. Four artifacts define the behavior: a state model, a transition table, an idempotency contract, and a matrix of repeated-request scenarios.

The first decision is to preserve uncertainty. OUTCOME_UNKNOWN remains separate from FAILED. A timer or a “not found” response cannot prove that money didn't move. Unresolved operations need an owner, reconciliation with provider evidence, and escalation.

The next decision is what a repeat means. Idempotency lets the same key and payment details identify the existing operation within a defined scope. In this case, provider protection assumes a 24-hour window and support for concurrent requests. A separate check blocks a new key with matching user, instrument, amount, and currency while the original payment remains unresolved.

Payment success and balance credit also need separate states. The provider can confirm success while credit is waiting or held for review. If the balance service creates a posting but its response is lost, another delivery must return that posting. The balance service enforces uniqueness by payment_id.

One useful specification check: let confirmation arrive after both allowed create attempts time out. Then lose the balance service's response. The rules should still identify the payment, preserve the evidence, and permit at most one balance posting under the stated assumptions.

The carousel shows the key decisions. GitHub contains the full specification, editable tables and diagrams, and 40 acceptance scenarios. These describe expected behavior, not executed implementation tests. Real provider guarantees still need verification.

https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/README.md

#SystemsAnalysis #RequirementsEngineering #Payments
