# Case 01 · Payment Timeout: States, Idempotency, and Recovery

Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.

[English](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/README.md) · [Русский](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/README.ru.md)

A user tops up a balance by €50. The request times out, but the provider may have accepted the payment. This case specifies retries, late confirmations, and balance credit.

This is an illustrative case. Specification version: 0.3. Status: Draft. The 40 scenarios describe expected behavior; implementation tests have not been executed.

## Materials

| Material | Purpose |
|---|---|
| [Full specification](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/specification.en.md) | Four core artifacts, six appendices, and 40 acceptance scenarios |
| [PDF carousel](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/carousel.en.pdf) | Approved compact version, 13 pages |
| [Editable tables and diagrams](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/README.md) | CSV and Mermaid exports with usage notes and limitations |

## Reading the case

Start with the scenario and provider assumptions in the specification. Continue with the state model, transition table, idempotency contract, and matrix. The appendices specify review, error classification, webhooks, outbox delivery, attempts, and reconciliation. Acceptance scenarios trace expected behavior to the rules.

`OUTCOME_UNKNOWN` does not become `FAILED` because of a timer or `NOT_FOUND`. The guard lasts until definitive resolution of the original payment. The balance service enforces posting uniqueness. Negative closure through `NOT_EXECUTED` requires PA-08, including a future-execution fence.

## Publication preparation

This package is in a review branch. LinkedIn publication text has not been added yet. The PDF case link will be connected after the final case URL is verified; the current Full specification caption does not establish an active link.

---

Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
https://github.com/YuliaMelekhova/inside-the-spec  
https://www.linkedin.com/in/yuliamelekhova
