# External Source Notes

Series: Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
Case: 02  
Author: Yulia Melekhova  
Version: 0.5  
Language: en  
Status: Draft

## Purpose
Separate verified examples of real provider behavior from this case's illustrative adapter contract. Sources checked on 2026-10-21; names and enums in the case are not a reproduction of any provider API.

- [Adyen: refunds](https://docs.adyen.com/online-payments/refund): an initially successful refund notification can be followed by scheme rejection. This supports including late failures; it does not establish a universal meaning for every provider's COMPLETED value.
- [Stripe: asynchronous refund testing](https://docs.stripe.com/testing): documents refunds that initially appear successful and later fail.
- [Stripe: refunds](https://docs.stripe.com/refunds): describes failed refunds and bank/issuer handling. Bank visibility and refund processing are separate concerns.
- [Stripe: idempotent requests](https://docs.stripe.com/api/idempotent_requests): API v1 key retention and request matching constrain safe retries; contract behavior must be pinned to the API version. The case requires provider-specific guarantees rather than copying one retention duration to every PSP.
- [AWS: Transactional Outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html): outbox delivery may duplicate messages; consumers still require idempotency.

The deadline profiles, finance handoff, D02 behavior, and model boundaries are design choices for this case, not financial/legal advice or assertions that a particular posting is required. Card refunds, bank-transfer returns, and chargebacks are not interchangeable event types.


---
Inside the Spec · Real Scenarios. Working Artifacts. Decisions That Matter.
https://github.com/YuliaMelekhova/inside-the-spec
https://www.linkedin.com/in/yuliamelekhova
