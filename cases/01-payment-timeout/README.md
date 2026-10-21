# Case 01 · Payment Timeout: States, Idempotency, and Recovery

Inside the Spec – Realistic Scenarios. Working Artifacts. Decisions That Matter.

[English](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/README.md) · [Русский](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/README.ru.md)

A user tops up a balance by €50. The request times out, but the provider may have accepted the payment. This case specifies retries, late confirmations, and balance credit.

This is an illustrative case. Specification version: 0.4. Status: Published on GitHub. The 58 scenarios describe expected behavior; implementation tests have not been executed.

## Materials

| Material | Purpose |
|---|---|
| [Full specification](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/artifacts/specification.en.md) | Four core artifacts, six appendices, and 58 acceptance scenarios |
| [LinkedIn post copy](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/post.en.md) | Complete English publication text |
| [Publication comments](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/comment.en.md) · [Русский](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/comment.ru.md) | Ready-to-copy comments with material links |
| [PDF carousel](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/carousel.en.pdf) | Approved compact version, 15 pages |
| [Editable tables and diagrams](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/artifacts/README.md) | CSV and Mermaid exports with usage notes and limitations |

## Reading the case

Start with the scenario and provider assumptions in the specification. Continue with the state model, transition table, idempotency contract, and matrix. The appendices specify review, error classification, webhooks, outbox delivery, attempts, and reconciliation. Acceptance scenarios trace expected behavior to the rules.

`OUTCOME_UNKNOWN` does not become `FAILED` because of a timer or `NOT_FOUND`. The guard lasts until definitive resolution; WR-01 safely expires a provably never-dispatched CREATED job. Credit OUTCOME_UNKNOWN stays distinct from a hold; read-only balance lookup continues during review. The balance service enforces posting uniqueness. Negative closure through `NOT_EXECUTED` requires PA-08, including a future-execution fence.

[Review changes v0.4](https://github.com/YuliaMelekhova/inside-the-spec/blob/main/cases/01-payment-timeout/changes-v0.4.en.md)

## Publication status

The v0.4 materials are published on the GitHub main branch. English and Russian post and comment copy is ready; LinkedIn publication is pending. Both PDFs and comment links point to the case indexes on main. Publish post.en.md with carousel.en.pdf, then add the prepared English and Russian comments; the Russian post/PDF pair is also available separately.

---

Inside the Spec – Realistic Scenarios. Working Artifacts. Decisions That Matter.  
https://github.com/YuliaMelekhova/inside-the-spec  
https://www.linkedin.com/in/yuliamelekhova
