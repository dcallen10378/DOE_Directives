# DOE 413 Project‑Management Q&A (test setup)

A lightweight, subscription‑powered question‑answering tool over a **fixed set of public
DOE 413 directives**, for a Project Management Office to query **413 project guidance —
focused on scheduling and reporting.** No API keys, no servers, no build step.

## How it works
The six directives live in `docs/` as page‑tagged Markdown (extracted from the official
PDFs). A `CLAUDE.md` at the repo root tells Claude to **answer only from those documents,
cite the specific document + section/page, and say so plainly when something isn't covered.**
Retrieval is handled by Claude reading/searching the `docs/` files — there are no
embeddings, database, or external services.

## How to use it (iPad / browser, on your Claude subscription)
1. Go to **claude.ai/code** and open this repository
   (`dcallen10378/DOE_Directives`) in a Claude Code session.
2. Ask a 413 question in plain English. `CLAUDE.md` loads automatically and sets the rules.
3. Read the answer — it will cite the source (e.g. *“per DOE O 413.3B, §2.b …”*).

Anyone you hand the iPad to is just typing into your own session — it runs on your
subscription, no separate accounts or keys.

## What's loaded
| Document | Version | Role |
|----------|---------|------|
| DOE O 413.3B | Chg 7 (06‑21‑2023) | The Order — requirements |
| DOE G 413.3‑5A — Performance Baseline Guide | Chg 1 | Guidance |
| DOE G 413.3‑7A — Risk Management Guide | Chg 2 | Guidance |
| DOE G 413.3‑20 — Change Control Management Guide | Chg 1 (Admin Chg) | Guidance |
| DOE G 413.3‑21A — Cost Estimating Guide | current | Guidance (cost) |
| DOE EVMS Gold Card | current | EVM definitions/formulas |

All six directives are loaded. Estimating is included only so cost questions aren't dead
ends — the tool's focus is scheduling and reporting, not estimating.

## Sample questions to try
- "What are the schedule requirements at CD‑2 per the Order?"
- "How often must project status be reported, and to whom?"
- "What does the Performance Baseline Guide say about schedule contingency?"
- "Define Schedule Variance and SPI." (EVMS Gold Card)
- "What change‑control thresholds require DOE approval?"

## Refreshing or re‑extracting a document
1. Replace/add the PDF in `docs/source-pdfs/`.
2. Re‑run the extractor: `python3 prep/build_md.py` (regenerates the page‑tagged Markdown via OCR).
3. Commit the updated `docs/*.md`.

## Repo layout
```
CLAUDE.md                 # assistant behavior: scope, citation, refusal rules
docs/                     # page-tagged Markdown the assistant reads
  413.3B-Order-Chg7.md
  413.3-5A-PerformanceBaseline-Chg1.md
  413.3-7A-RiskManagement-Chg2.md
  413.3-20-ChangeControl-Chg1.md
  EVMS-GoldCard.md
  source-pdfs/            # original PDFs (provenance)
prep/build_md_par.py      # OCR extractor (PDFs -> page-tagged Markdown)
```

## Notes
- **Extraction is OCR‑based.** The official PDFs had no usable text layer, so each page was
  rendered and OCR'd. Expect occasional OCR artifacts; the EVMS Gold Card (a graphical card)
  was reviewed by hand.
- This is a **test setup** to validate intent; a production deployment would be built
  differently.
