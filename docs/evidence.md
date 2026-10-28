# Evidence and privacy

| Fact status | Meaning | Application eligibility |
| --- | --- | --- |
| `confirmed` | Explicit owner confirmation | Eligible if public |
| `reported` | Supported by supplied documents, extracts, analyses or correspondence | Eligible if public; retain context |
| `estimated` | Sourced and explicitly labeled estimate | Excluded pending resolution/reviewed contract extension |
| `needs_clarification` | Ambiguous, contradictory or insufficient | Excluded |
| `superseded` | Rejected/replaced assertion retained for provenance | Excluded |

No status implies independent employer verification. Supplied analyses are not the
underlying code, and employer tests cannot be rerun here. Validation checks identity
and structure, not truth or whether a paraphrase follows from its citation.

Visibility is separate: `public` phrasing is suitable for applications even when its
source is private; `private` holds career/implementation context; `restricted` holds
especially sensitive context. Default retrieval/application assembly excludes the
latter two. Explicit local `search --private` includes both for research; do not share
that output by default. Always read notes before using public facts.

Owner statements can resolve conflicting interpretations of their work; timestamps
alone do not decide authority. Later partial corrections do not discard unrelated
facts in older sources. Derived summaries cannot overrule primary evidence. Preserve
conflicts, cite corrections, and ask the owner when the evidence cannot resolve them.

Text citations use one-based `L12-L18`. Binary citations use `p1-p3`, `visual`, or
`section:...`; binary meaning needs an appropriate reader, since core validation only
checks their syntax. Register extracted text separately with `derived_from`; precise
text ranges are automatically bounds-checked, but imagery/layout may be omitted.

Dates permit `YYYY`, `YYYY-MM`, `YYYY-MM-DD`, or null. Preserve supplied precision.
As-of dates are knowledge snapshots, not project start dates. `ongoing: true`
requires evidence of continuing responsibility; false makes no affirmative ongoing
claim and supplies no unknown end date. Do not infer language tenure from a skills
list or date a later feature from an earlier release plaque.

Correct records without rewriting originals: import a revision, record `supersedes`,
and cite the correction in affected facts. Mark rejected claims superseded/private;
preserve their explanation. Git history retains normalized record changes, while
hash checks guard source bytes. Never update a fingerprint merely to silence an error.

Raw evidence includes personal details and private employer information. Keep access
appropriate, inspect diffs before committing, and do not upload/publish automatically.
Inbox/private folders, indexes and secret environment files are ignored. Ignoring is
not encryption/access control. Private local evidence needs separate backup and will
be missing in a clone; validation deliberately fails until needed sources are restored.
Do not store credentials. Application identity omits the street address; originals
remain preserved.
