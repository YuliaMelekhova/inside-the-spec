# Production rules

Series: Inside the Spec
Subtitle: Real Scenarios. Working Artifacts. Decisions That Matter.

## Editorial
- Never use an em dash (U+2014). Use an en dash (U+2013) for prose punctuation.
- English is the primary LinkedIn post and document language.
- Each episode has a Russian post and separate Russian PDF.
- Preserve identifiers, field names, payloads and example values across translations.
- Label assumptions and fictional examples explicitly.
- Explain decisions and include counterexamples or acceptance checks.
- Further writing rules are pending review of the author's two source Markdown files.

## Design v0.1
- Portrait 4:5, PDF page size 200 x 250 mm.
- Paper #F7F4EE; ink #293C3C; teal #607F7A; ochre #B09161.
- Light panel #EDF1EF; separators #D7DEDA.
- No floral illustrations on working pages.
- Use labels as well as colors for all meaningful distinctions.
- Six master layouts: cover, scenario, diagram, table, specification, validation/resources.
- Full title and subtitle on the cover; episode, version and page number in the footer.
- Current system fonts are provisional. Bundle licensed font files before freezing v1.0.

## Template usage
1. Download templates/carousel.html and open it in a desktop browser.
2. Choose English or Russian.
3. Use Save as PDF. Disable browser headers and footers, enable background graphics, and use 100% scale.
4. Verify a six-page 4:5 result, including Cyrillic, wrapping, footers and table rows.
5. Review at phone width before publication.
6. Edit the copy object for content. Extend layouts for full episodes.
7. Check that every page fits. Never hide overflowing content or reduce all text to make it fit.

This is a functional HTML/print prototype, not an approved visual master or a completed episode.
No exported PDF has been visually approved. Automated PDF rendering and overflow checks are a next implementation step.

## Episode file convention
episodes/01-payment-timeout/
- README.md: English case index with Russian link
- README.ru.md: Russian case index with English link
- post.en.md and post.ru.md: complete publication text
- comment.ru.md: short Russian introduction and link
- carousel.en.pdf and carousel.ru.pdf: language-specific exports
- artifacts/: shared editable diagrams, contracts and tables

Create these files when their contents are ready. Avoid empty downloadable placeholders.
Use a direct link to README.ru.md from LinkedIn and the final carousel page.

## Working with ChatGPT
Keep authoritative sources in GitHub with version history.
Project instructions should explicitly require reading these rules and the relevant template before authoring.
Attaching a file to a ChatGPT Project is useful context, but does not itself guarantee automatic enforcement.
The two author-supplied writing files must be reviewed before adding their rules.
