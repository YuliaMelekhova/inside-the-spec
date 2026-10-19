# Writing and Artifact Rules

**Series:** Inside the Spec  
**Subtitle:** Real Scenarios. Working Artifacts. Decisions That Matter.  
**Author:** Yulia Melekhova  
**Scope:** Posts, comments, PDFs, editable artifacts, repository documentation, and related visuals  
**Version:** 0.1

## Purpose

Use these rules when drafting, translating, reviewing, or publishing this series. They adapt the author's anti-ai-writing.md and anti-ai-artifacts.md for ChatGPT and this repository. They are editorial instructions, not a claim that writing can be classified reliably as human or AI.

## Rule priority

Current explicit author instructions take precedence over these editorial defaults.
Use the approved episode specification for technical behavior and production/RULES.md for layout.
Do not import old series names, phase labels, repository paths, or unavailable reference documents.
If instructions conflict, flag the specific conflict instead of silently changing a technical claim.

## Languages and audience

- Primary LinkedIn posts and PDF carousels use American English.
- Each episode also has a complete Russian post and separate Russian PDF.
- Russian comments may contain an abbreviated introduction and a link to the full Russian package.
- Use Russian for the working conversation unless requested otherwise.
- Posts should be understandable to a professional outside IT. Explain specialist terms on first use.
- Artifacts serve analysts, developers, and QA. Keep precise terminology, formulas, field names, and normative wording where needed.
- A short post explanation of idempotency must state its scope. Do not promise that a key alone prevents every duplicate charge.

## Typography

Never use an em dash, U+2014, in authored prose, slides, tables, diagrams, captions, metadata, or commit messages.
Use an en dash, U+2013, only when needed. Prefer a full stop or comma when that reads better.
Hyphens in filenames, identifiers, code syntax, and compound words remain unchanged.
Do not decorate headings with emojis. Artifacts have no decorative emojis.
Use Step 1: Title for numbered step headings.

The approved series title and subtitle stay together on covers and series descriptions. Compact navigation may use the series title alone when the full identity is already established.

## Voice and factual discipline

Start with the answer, problem, or concrete observation.
Use direct verbs and connected prose. Prefer active voice.
Be professional, plain, and a little dry. Avoid cheering, sales language, and inflated claims.
Use specific numbers when known. Never invent a measurement to make a sentence sound concrete.
Use first person only for verified author experience or an explicitly stated opinion. Do not invent personal stories, clients, outcomes, or production incidents.
Label fictional cases, assumptions, and illustrative amounts.
Keep one clear line of reasoning per paragraph.
No generic praise, restatement of the request, corporate sign-off, or repetitive closing summary.
A CTA is optional. Never force a question or engagement prompt at the end.

## Vocabulary to avoid in authored promotional prose

leverage, navigate, robust, seamless, foster, delve, landscape, tapestry,
vibrant, nestled, underscore, harness, unleash, unlock, elevate, empower,
streamline, pivotal, paradigm, holistic, synergy, ecosystem, realm, sphere,
arena, beacon, cornerstone, testament; metaphorical journey and fabric.

Treat this as a strict prose preference. Do not corrupt a literal technical term, source title, quotation, identifier, or proper name to satisfy the list.
For example, navigation in an interface specification and a bounded domain ecosystem may have literal meanings. Prefer a more precise term where available.
Check every occurrence, not only paragraphs containing several banned words.

Avoid these phrases and their Russian equivalents:
- Not just X, but also Y.
- It's not about X, it's about Y.
- It's not X, it's Y, and similar rhetorical reversals.
- In today's fast-paced world; at the end of the day; when it comes to.
- In the realm of; stands as a testament to; plays a pivotal role in.
- It's important to note; it's worth mentioning.
- Furthermore or moreover as decorative transitions.
- In conclusion; comprehensive guide; robust solution.
- Let me know if you need anything else.
- Circle back; move the needle; low-hanging fruit; touch base; game-changer.
- Metaphorical bandwidth, sports metaphors, and at scale as filler.

Technical negation remains valid: a timeout does not establish a failed payment.
An actual before/after comparison or a distinction needed for correctness remains valid.

## Rhythm and structure

Vary sentence length, openings, complexity, and paragraph size naturally.
Avoid repeated short fragments, uniform paragraph blocks, and mechanical long-short alternation.
Avoid three or more consecutive sentences with the same opening or grammatical shape.
Do not make every sentence a separate paragraph.
Split long sentences that combine unrelated claims. Keep a long sentence when it expresses one connected thought clearly.
Do not stack uncertainty words. State uncertainty once, with its reason.
Read prose aloud during review.

Do not impose numerical rhythm quotas. Do not add filler to reach four list items.
Three items are appropriate when the subject has three relevant elements.
Preserve the approved three-sentence series subtitle exactly.
Tables, requirements, decision rules, and acceptance scenarios may deliberately repeat a structure for comparison and testing.

## English conventions

Use American spelling: analyze, behavior, color, center, organization, canceled, judgment.
Preserve source spelling in company names, standards, quoted titles, and field names.
Use double quotation marks first and the serial comma.
Use Month D, YYYY for English narrative dates, with no ordinal suffix.
Use ISO YYYY-MM-DD for metadata and machine-readable dates.
Use numerals for measurements, money, percentages, dates, and values readers need to scan.
Use words for small ordinary counts when natural.
Use contractions in posts and comments when natural. Avoid them where formal requirements need precision.
Prefer use, start, help, show, before, and because over inflated alternatives.
Use will or must according to meaning. Preserve shall when quoting a source or following an explicitly chosen requirements convention.
Do not replace exact constraints with casual wording.

## Russian conventions and translation

Write natural professional Russian, not an English sentence translated word by word.
Avoid Russian equivalents of the prohibited cliches, artificial contrasts, and repetitive rhythm.
Use Russian punctuation and date conventions in narrative text. Keep ISO dates in metadata.
Keep identifiers, enum values, payloads, example amounts, units, and requirement IDs consistent across languages.
Translate explanations and headings. Do not translate code tokens or API field names.
Both versions must carry the same assumptions, rules, exceptions, and acceptance results.
Allow different line breaks and layout adjustments for longer Russian text. Do not shrink all Russian text to force an English layout.
Review the Russian version independently for meaning and readability.

## Episode organization

Use episodes/01-payment-timeout/ for episode 01 and stable numbered folders for subsequent episodes.
Do not rename published episodes when adding a new one.
Each episode may contain:
- README.md and README.ru.md: language-specific entry points.
- post.en.md and post.ru.md: complete publication text.
- comment.ru.md: short Russian introduction with the final episode link.
- carousel.en.pdf and carousel.ru.pdf: separate language exports.
- artifacts/: editable specifications, tables, and diagrams.

Shared technical files may remain in English when both language indexes clearly explain them.
Provide Russian explanatory notes for a claim that the complete package is available in Russian.
Create only files with usable content. Do not ship empty placeholders.

## Artifact metadata

Markdown artifacts start with an H1 and readable metadata:
- Series: full title, with the subtitle directly below or in its own field.
- Episode: stable two-digit identifier.
- Author: Yulia Melekhova.
- Version: actual artifact version.
- Language: en, ru, or a clearly explained shared technical format.
- Status: Draft or Published, matching reality.

Follow with a Purpose section of at most two sentences describing when to use the artifact.
Add the live LinkedIn URL after publication. Before publication omit it rather than fabricate a URL.
An actual publication date is recorded only after publication.
Metadata lines use Markdown hard breaks and must be checked in the rendered preview.
Root and episode README files prioritize navigation and need no full artifact metadata block.

## Body requirements

Provide a worked example, explicit assumptions, and defined boundaries.
Keep states, events, transitions, conditions, actions, and ownership distinct where the artifact needs them.
Include a test, counterexample, or consistency check that can reveal an incomplete specification.
Explain meaningful trade-offs and limits of applicability.
No TBD markers, filler rows, fake links, or decorative content in released artifacts.
Clearly labeled template examples and drafts are allowed before release.

Machine-readable formats must remain valid:
- CSV files contain tabular data only. Put metadata and explanatory text in a sibling .notes.md.
- Mermaid and YAML use valid comment syntax for brief metadata where safe.
- JSON has no comments; use a companion Markdown file.
- Python, HTML, templates, and other executable sources follow their native structure. Do not force a prose header or footer into generated output or executable data.

## Footer and links

Explanatory Markdown artifacts end with the series identity, repository link, and author LinkedIn link.
Use:
Inside the Spec · Real Scenarios. Working Artifacts. Decisions That Matter.
https://github.com/YuliaMelekhova/inside-the-spec
https://www.linkedin.com/in/yuliamelekhova

Add Related Artifacts only when verified related files exist. Each link explains why to open it.
Use verified absolute GitHub URLs for published cross-references. Files use blob; folders use tree.
Do not invent main-branch URLs for files that exist only in a draft branch.
A relative target can be technically valid, but published links follow the absolute-URL convention for this series.
Check path casing and duplicated path segments.

## Indexes and publication

The root README indexes released episodes, with routes to both languages.
Episode indexes link the post, PDF, and editable artifacts without duplicating full content.
Drafts can be indexed in an explicitly labeled draft section.
Keep technical examples aligned across language versions before publication.
Correct published artifacts with a version change and a short explanation. Do not silently repurpose them.

## Git and delivery

Use concise imperative commit messages without emoji, em dashes, decorative prefixes, or a trailing period.
For example: Add episode 01 idempotency matrix.
Use a branch and reviewable PR for the current setup work. Do not inherit the old repository's direct-to-main rule.
Report the actual saved files, validation performed, remaining limitations, and PR link.
When files are committed through the integration, do not ask the author to paste README rows or commit messages manually.
Mention affected indexes and reverse links when a change requires them.

## Final review

Before delivery:
1. Search authored content for U+2014 and remove it.
2. Check vocabulary, cliches, repetitive structure, and unneeded summaries.
3. Verify facts, assumptions, identifiers, examples, and EN/RU agreement.
4. Check metadata, links, machine-readable syntax, and index entries.
5. Render PDF output and inspect text, diagrams, tables, Cyrillic, and page boundaries.
6. Distinguish completed checks from checks still pending.
7. Confirm the delivered files exist in the stated location and version.

Do not apply prose rhythm rules mechanically to code, CSV, requirements tables, or Given/When/Then scenarios.
