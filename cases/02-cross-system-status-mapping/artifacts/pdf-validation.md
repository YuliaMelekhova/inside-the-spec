# PDF Export Validation

Series: Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
Case: 02  
Author: Yulia Melekhova  
Version: 0.5  
Language: en  
Status: Draft

## Purpose
Record PDF export checks separately from the finite model and integration acceptance scenarios.

Both EN and RU exports contain 14 pages at 200 × 250 mm. The approved compact ReportLab renderer and bundled Cyrillic fonts were used. Main text is 12 pt, table text 10.4 pt, and notes 9.6 pt. Page count follows the prepared content.

Every page of each latest export was rasterized and visually inspected for text boundaries, Cyrillic, tables, cover identity, footer numbering, and resource placement. All prepared content blocks were matched against extracted PDF text. The case-specific, repository, and author PDF annotations were checked. The case index was fetched successfully from the review branch before its URL was configured.

The PDFs summarize the case. Full behavior, event fields, operational rules, and all 112 expected acceptance scenarios are in the linked artifacts. This review does not establish that the integration has been implemented or tested.

The editable HTML companion remains internal and was syntax-checked; its browser print output is not the validated PDF export.

---
Inside the Spec · Real Scenarios. Working Artifacts. Decisions That Matter.
https://github.com/YuliaMelekhova/inside-the-spec
https://www.linkedin.com/in/yuliamelekhova
