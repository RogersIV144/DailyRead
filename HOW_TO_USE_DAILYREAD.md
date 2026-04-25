# How To Use DailyRead

Chinese guide: [HOW_TO_USE_DAILYREAD_ZH.md](./HOW_TO_USE_DAILYREAD_ZH.md)

## What This Workspace Gives You

This workspace is a workspace-first research workflow for:

- paper discovery
- venue survey
- deep paper analysis
- idea generation
- report writing
- local search over papers and ideas
- optional attachment collection

Everything lives inside this repository. You do not need an external Obsidian vault for the core workflow.

## Workspace Layout

```text
papers/        paper notes
ideas/         idea notes
reports/       reading reports, venue surveys, progress reviews
inbox/         temporary leads and backlog items
index/         generated indexes and catalogs
attachments/   optional downloaded PDFs, figures, and other assets
config/        workflow config and track presets
templates/     note and report templates
.github/       Copilot instructions, prompts, and skills
scripts/       validation and indexing helpers
.conda/        workspace-local Python environment
```

## Recommended First Steps

1. Open `config/dailyread.yaml` and scan the defaults.
2. Open the relevant file under `config/tracks/` and tune keywords for your current direction.
3. If you want Copilot to refresh slash command discovery immediately, reload the VS Code window once.
4. Start with one of the phase-1 skills below.

## Phase-1 Skills

Type `/` in chat and select one of these skills:

- `daily-discovery`
- `venue-survey`
- `paper-analyze`
- `idea-synthesis`
- `report-writer`
- `paper-search`
- `extract-paper-images`

### Suggested Usage Order

#### 1. Discover recent papers

Use `daily-discovery` when you want a short survey-style scan of recent papers for a track or topic.

Examples:

- `daily-discovery ai systems recent inference serving papers`
- `daily-discovery architecture memory hierarchy recent_90d`

Expected result:

- a survey-style report under `reports/`
- a backlog section for follow-up reading
- optional follow-up leads in `inbox/`

#### 2. Survey a venue

Use `venue-survey` when you want a focused review of a venue or conference family.

Examples:

- `venue-survey ASPLOS recent_5y LLM serving`
- `venue-survey OSDI cluster scheduling`

Expected result:

- a venue survey report under `reports/`
- highlighted papers
- gap map and follow-up reading suggestions

#### 3. Deeply analyze a paper

Use `paper-analyze` when you want a durable, structured paper note.

Examples:

- `paper-analyze 2024 OSDI paper about inference serving`
- `paper-analyze arXiv:2401.12345`
- `paper-analyze https://doi.org/...`

Expected result:

- a deep paper note under `papers/<year>/<venue>/`

#### 4. Turn reading into ideas

Use `idea-synthesis` when you already have paper notes or survey notes and want concrete hypotheses.

Examples:

- `idea-synthesis compare these three paper notes for unsolved bottlenecks`
- `idea-synthesis from this venue survey generate candidate ideas`

Expected result:

- one or more idea notes under `ideas/`

#### 5. Write a report

Use `report-writer` when you want a weekly, monthly, survey, or progress-style report.

Examples:

- `report-writer weekly report from last week's papers and ideas`
- `report-writer progress review for ai systems reading this month`

Expected result:

- a report under `reports/`

#### 6. Search local notes

Use `paper-search` when you want to find prior notes by title, topic, venue, key, or tag.

Examples:

- `paper-search topic memory disaggregation`
- `paper-search OSDI inference serving`

#### 7. Collect figures or assets

Use `extract-paper-images` when a paper has figures, PDFs, project pages, or artifacts worth storing.

Expected result:

- files or asset references under `attachments/`

## Reusable Prompts

Workspace prompts live under `.github/prompts/`.

Current prompts include:

- `Compare Papers`
- `Reading To Report`
- `Survey To Ideas`
- `Group Meeting Brief`

Use them from chat or with `Chat: Run Prompt...`.

## Notes and Metadata Conventions

### Paper Notes

Use `templates/deep_paper_note.md` as the base shape.

Important fields:

- `paper_key`
- `year`
- `venue`
- `topics`
- `related_ideas`
- `read_priority`

### Idea Notes

Use `templates/idea_note.md`.

Important fields:

- `origin_papers`
- `confidence`
- `maturity`
- `next_action`
- `blocking_questions`

### Reports

Use `templates/hybrid_report.md` or `templates/survey_report.md`.

Important fields:

- `report_kind`
- `trigger`
- `input_notes`
- `takeaways`
- `action_items`

## Python Environment

This workspace uses a local `.conda` environment.

In PowerShell, use:

```powershell
.\.conda\python.exe .\scripts\validate_dailyread.py
.\.conda\python.exe .\scripts\build_indexes.py
```

Use the local environment for future helper scripts as well.

## Validation and Indexing

### Validate the Workspace

Run:

```powershell
.\.conda\python.exe .\scripts\validate_dailyread.py
```

This checks:

- required directories and files
- root config structure
- template frontmatter
- skill naming and descriptions
- prompt and instruction frontmatter

### Rebuild Indexes

Run:

```powershell
.\.conda\python.exe .\scripts\build_indexes.py
```

This updates files under `index/`, including:

- `catalog.json`
- `papers-by-topic.md`
- `papers-by-venue.md`
- `ideas-by-topic.md`
- `reports-by-kind.md`

## How To Extend The Workflow

### Tune research directions

- edit `config/tracks/*.yaml`
- adjust keywords and preferred venues

### Add or adjust prompts

- create or edit files under `.github/prompts/`

### Add or adjust skills

- create or edit folders under `.github/skills/`
- each skill must contain `SKILL.md`
- the `name` field must match the folder name exactly

### Add new instructions

- create files under `.github/instructions/`
- use `description` for on-demand discovery
- use `applyTo` only when the instruction truly fits that file pattern

## Practical Workflow Example

1. Run `daily-discovery` for `ai_systems`.
2. Pick 2 to 3 papers from the generated report.
3. Run `paper-analyze` on the strongest one.
4. Run `idea-synthesis` over the new paper note and the discovery report.
5. Run `report-writer` to summarize the week or topic.
6. Run `build_indexes.py` if you want refreshed index files.

## If Slash Commands Do Not Show Up

1. Reload the VS Code window.
2. Confirm the relevant file exists under `.github/skills/` or `.github/prompts/`.
3. Run the validation script.
4. Check that YAML frontmatter is valid and that skill `name` matches the folder name.

