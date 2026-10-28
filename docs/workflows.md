# Practical workflows

Run commands from the repository root with Python 3.9+. The core has no package
installation step. Agents should read `AGENTS.md` and use the reusable prompts.

## Explore and validate

```sh
python3 scripts/career.py validate
python3 scripts/career.py search "Rust desktop developer tools" --limit 8
python3 scripts/career.py search "rollback qualification" --private --limit 8
python3 scripts/career.py show project-ia-mcp
python3 scripts/career.py duplicates
rg -n 'PostgreSQL|mentoring|CMN' knowledge
```

Search returns eligible fact references and scoring signals. Read full records,
notes and citations; do not infer a requirement is satisfied from a matching word.
Private search is for local research. `duplicates` flags exact duplicate fact text;
semantic overlap still requires review. Related summaries can overlap legitimately.

For optional local semantic indexing:

```sh
python3 scripts/career.py index --output build/search.jsonl
```

This exports a disposable corpus with stable fact references and evidence. You can
also use `--private` locally; do not upload the corpus without authorization.

## Add a source

Stage a document or attributed owner note in ignored `sources/inbox/`. Preserve it:

```sh
python3 scripts/career.py ingest sources/inbox/project-notes.md \
  --id src-project-notes-2026-10-27 --title 'Owner project notes' \
  --kind owner_statement --date 2026-10-27
```

Use the actual import date. Kinds distinguish owner statements/documents, supplied
analyses, correspondence, artifacts and extractions. The original is copied exactly
to `sources/originals/<id>/`, fingerprinted and registered. Duplicate bytes return
the existing ID without copying; duplicate IDs with different bytes are rejected.
Ingestion is serialized; if another process holds the lock, retry after it finishes.
Only remove a stale `sources/.ingest-lock` after confirming no ingestion is running.

Add `--private` to store highly sensitive originals under ignored `sources/private/`
instead. The registry still tracks the reference, so backups and restoration on
another checkout are your responsibility. The default originals folder is intended
for version control after a privacy review. No tool automatically stages or commits.

For a corrected source, use a new ID and `--supersedes old-source-id`. This preserves
both sources; it does not automatically invalidate every fact from the older source.
Reconcile affected statements explicitly.

## Extract and normalize

The helper reads text and DOCX document/header/footer paragraphs:

```sh
python3 scripts/career.py extract 2020-Sep.docx > sources/inbox/word-extract.txt
python3 scripts/career.py ingest sources/inbox/word-extract.txt \
  --id src-word-extract-new --title 'Word paragraph extraction' \
  --kind extraction --derived-from src-docx --date 2026-10-27
```

Extraction does not replace the original or reliably capture tables/images/layout.
For PDFs, use an available reader or `pdftotext -layout` and register its output as
a derivative. Existing Word/LinkedIn extractions are already registered. Validate
meaning against originals where needed. Repository/code URLs can be preserved in
attributed notes; accessing them does not imply permission to publish private code.

Search for overlap; then copy `templates/record.json` to the appropriate knowledge
category. Replace placeholders, match filename and ID, use only supplied date
precision, add relationships and record each factual statement with status, visibility
and exact source lines. Capture challenges, personal actions, ownership, outcomes
and metric context separately when useful. Use private facts/notes for deep detail;
do not discard it because it will not fit on a résumé. Templates live outside the
authoritative records and intentionally fail until completed. Run `validate` and
`duplicates`, inspect citations and review the diff.

For updates, preserve source bytes and stable IDs. Cite the correction, retain
rejected claims as superseded/private where useful, and record unresolved conflicts
in `docs/open-questions.md`. Never simply refresh a source hash after an error.

## Tailor a résumé

Create `applications/<company>/<role>/<YYYY-MM-DD>/`. Copy the actual posting to
`job.md`, then copy `templates/job.json` and `templates/selection.json` into that
folder. Set the target and dates, replace every placeholder, and compute the source
hash with `shasum -a 256 path/to/job.md` (or Python's `hashlib`). Store only the hex
digest in `job.json`. Capture a live posting before analysis rather than relying on
a title or search snippet. A redacted posting is a distinct source, labeled as such.

Read the job in full. Record required/preferred qualifications, responsibilities,
technologies, seniority, ownership, years, domain and location/eligibility constraints
as individual requirements with line locators and retrieval terms. Then run:

```sh
python3 scripts/career.py match applications/company/role/2026-10-27
```

The agent must assess meaning, not copy ranking into a coverage decision. Search
additional terms and related records, read caveats, and inspect original evidence.
Choose positioning and concise accomplishment bullets. `selection.json` contains
the authored text and references for every résumé line, plus coverage of every
requirement, decisions, gaps and follow-ups. Strong/partial matches need eligible
fact references; gaps have no supporting references. Record why partial evidence
does not establish the missing scope. Missing documentation is not a claim that
the person lacks the experience.

Sections are flexible standard headings. Entries can be paragraphs, role headings
or bullets; every factual entry has references. `verbatim: true` enforces an exact
single-fact quote. Use false for polished rewrites or synthesis and review their
entailment yourself. Avoid invented metrics or generic keyword stuffing. Record
the factual review in `review_notes`—this is agent review, not a permission gate.

```sh
python3 scripts/career.py build applications/company/role/2026-10-27
python3 scripts/career.py audit applications/company/role/2026-10-27
```

Outputs are `resume.md`, `match-analysis.md`, `claims.json` and `build-manifest.json`.
The trace maps Markdown line numbers and prose to facts, evidence paths and hashes.
Keep traces/analysis internal. Read the final copy for factual accuracy, density,
repetition, natural keywords, clear ownership and appropriate seniority. Aim for
one or two readable pages when exporting. Structural checks cannot guarantee an
ATS vendor's parsing or that a paraphrase is entailed.

Build refuses existing outputs. Create a new revision folder for substantive edits;
after deliberately reviewing changes, `build --replace` explicitly regenerates the
same revision. Do not hand-edit generated Markdown without updating the selection.
Audit detects source, selection, contract, tooling or output drift. Git revisions
preserve historical inputs for exact reproduction. Registry changes invalidate old
manifest snapshots even when the prose is unchanged; review before rebuilding.

See the committed complete example under
`applications/example-labs/staff-ai-developer-tools/2026-10-27/`. Its opening is
fictional, while career claims are grounded in the real knowledge base.

## Exports

New résumés use Markdown as canonical output. When Pandoc and its output tooling
are available, a straightforward path is:

```sh
pandoc path/to/resume.md -o path/to/resume.docx
pandoc path/to/resume.md --pdf-engine=xelatex -o path/to/resume.pdf
```

These tools are optional and not installed or assumed by the core CLI. Use a simple
single-column reference document if available; keep real selectable text, standard
headings, readable type, ordinary bullets and contact links. Apply the applicable
document/PDF skill when exporting; render pages and inspect clipping, reading order,
page breaks and text extraction. A Markdown-only example has no asserted PDF layout.

The preserved `resume-output/build_resume.py` can still build its existing curated
versions using `resume-output/resume-content.json` and the pinned requirements there.
That is a separate legacy pipeline: new selections are not automatically imported
into its schema. Its validator resolves historical README evidence to the immutable
copy, retaining original audit keys and hashes. Do not rebuild unrelated old outputs
just to create a new application.

## Verify tooling changes

```sh
python3 -m unittest discover -s tests -v
python3 scripts/career.py validate
python3 scripts/career.py audit applications/example-labs/staff-ai-developer-tools/2026-10-27
```

Tests use explicitly synthetic data outside `knowledge/` and temporary repositories.
They cover malformed inputs, source drift, private/uncertain claim rejection,
ingestion deduplication, path escapes, concurrent ingestion and reproducible tracing.
