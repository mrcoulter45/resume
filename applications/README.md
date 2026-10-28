# Tailored applications

Use `<company>/<role>/<YYYY-MM-DD>/` for a reviewable application revision. Add a
suffix for multiple revisions on one day, or use Git history after deliberate review.
Do not overwrite a reviewed prior edition silently.

- `job.md`: captured posting, preserved as supplied.
- `job.json`: target, capture date, hash and structured requirements with locators.
- `selection.json`: authored résumé text, fact references, positioning and coverage.
- `resume.md`: generated canonical editable résumé.
- `match-analysis.md`: qualifications, gaps, decisions and collection questions.
- `claims.json`: each factual résumé line mapped to facts and source hashes.
- `build-manifest.json`: reproducible input/output fingerprints.

Keep traces and analysis internal. Use `applications/private/` for ignored sensitive
application drafts and back them up separately. The committed `example-labs/`
opening is fictional and clearly labeled. Follow [the workflow](../docs/workflows.md).
