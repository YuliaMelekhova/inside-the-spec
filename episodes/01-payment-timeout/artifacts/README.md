# Editable artifacts · Case 01

Inside the Spec – Realistic Scenarios. Working Artifacts. Decisions That Matter.

[Case index](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/README.md)

The full specification is the source of rules. CSV and Mermaid files are exact extracts for editing and comparison. Use them with the specification assumptions, conditions, and explanations.

[Full specification](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/specification.en.md)

| File | Content |
|---|---|
| [payment-state-machine.en.mmd](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/payment-state-machine.en.mmd) | Payment states |
| [payment-review-credit.en.mmd](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/payment-review-credit.en.mmd) | Payment, review, and credit coupling |
| [review-lifecycle.en.mmd](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/review-lifecycle.en.mmd) | Review lifecycle |
| [credit-state-machine.en.mmd](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/credit-state-machine.en.mmd) | Credit states |
| [status-combinations.en.csv](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/status-combinations.en.csv) | M-01: allowed combinations |
| [state-transitions.en.csv](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/state-transitions.en.csv) | ST-01–ST-18 |
| [idempotency-matrix.en.csv](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/idempotency-matrix.en.csv) | IM-01–IM-25 |
| [acceptance-scenarios.en.csv](https://github.com/YuliaMelekhova/inside-the-spec/blob/case-01-public-package/episodes/01-payment-timeout/artifacts/acceptance-scenarios.en.csv) | AC-01–AC-58 |

## Metadata and use

Version: 0.4  
Language: en  
Status: Draft  
Author: Yulia Melekhova

CSV files contain tables only, encoded in UTF-8 with comma delimiters. Cell text retains Markdown formatting for identifiers. Each CSV has English and Russian versions with the same IDs and row order. Mermaid uses `%%` comments for metadata.

Extracted rows and diagrams were checked against the source specification. These are document checks, not execution of the 58 implementation scenarios. When rules change, update both specifications and derived files together.

---

Inside the Spec – Realistic Scenarios. Working Artifacts. Decisions That Matter.  
https://github.com/YuliaMelekhova/inside-the-spec  
https://www.linkedin.com/in/yuliamelekhova
