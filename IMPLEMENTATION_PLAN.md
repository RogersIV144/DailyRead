# DailyRead Implementation Plan

## Purpose

This file is the durable execution plan for the DailyRead research workflow.
It is intended to survive context loss, VS Code restarts, agent handoff, and future sessions.
All implementation progress should be reflected here as work advances.

## Execution Constraints

- Keep this file updated as the implementation proceeds.
- Use a workspace-local Python environment under `.conda` instead of any global base environment.
- When implementation is complete, provide a root-level usage guide in Markdown.

## Project Goal

Build a workspace-first research workflow for a new PhD student in computer systems and architecture, with support for systems, architecture, distributed systems, networking, security, AI systems, and optional embodied systems.

The workflow should cover:

- paper discovery
- venue-specific survey
- deep paper analysis
- idea synthesis
- report writing
- local search over papers and ideas
- optional paper asset extraction

## Scope Decisions

- Workspace root is the primary knowledge base.
- Paths and file names use English.
- Note body language is mixed: Chinese for analysis and conclusions, English for paper names, method names, and technical terms.
- Metadata uses YAML frontmatter.
- Internal enum values use `snake_case`.
- Customizations are workspace-level under `.github/`.
- No custom agent in phase 1.

## Target Workspace Layout

```text
DailyRead/
  .github/
    instructions/
    prompts/
    skills/
  attachments/
  config/
    tracks/
  ideas/
  index/
  inbox/
  papers/
  reports/
  templates/
  .conda/
  IMPLEMENTATION_PLAN.md
  HOW_TO_USE_DAILYREAD.md
```

## Configuration Model

### Root Config Structure

The root config will use these top-level groups:

- `general`
- `storage`
- `taxonomy`
- `search`
- `scoring`
- `tracks`
- `tasks`
- `venues`

### Key Defaults

- `search.search_scopes`: `papers`, `ideas`
- `search.default_sort`: `balanced`
- `search.semantic_search_enabled`: `false`
- `default_year_window`: `recent_30d`, `recent_90d`, `recent_365d`, `recent_5y`, `all_years`

### Enabled Tracks

Default enabled tracks:

- `architecture`
- `systems`
- `distributed_systems`
- `network`
- `security`
- `ai_systems`

Tracked but disabled by default:

- `embodied_systems`

## Note Schemas

### Paper Notes

Required fields:

- `title`
- `type`
- `status`
- `paper_key`
- `year`
- `venue`
- `authors`
- `topics`
- `tags`
- `source_urls`
- `date_added`
- `date_updated`
- `related_ideas`
- `read_priority`

Optional fields:

- `abstract`
- `venue_rank`
- `reading_stage_notes`
- `bibtex_key`

Defaults:

- `status: queued`
- `read_priority: medium`

Enums:

- paper status: `inbox`, `queued`, `reading`, `analyzed`, `archived`
- read priority: `high`, `medium`, `low`

### Idea Notes

Required fields:

- `title`
- `type`
- `status`
- `topics`
- `tags`
- `origin_papers`
- `confidence`
- `maturity`
- `next_action`
- `blocking_questions`
- `target_venues`

Optional fields:

- `hypothesis_type`
- `expected_cost`
- `expected_risk`
- `related_reports`
- `target_timeline`

Defaults:

- `status: incubating`
- `maturity: raw`
- `confidence: low`

Enums:

- idea status: `incubating`, `exploring`, `validating`, `archived`
- idea maturity: `raw`, `working`, `strong`
- idea confidence: `low`, `medium`, `high`

### Report Notes

Required fields:

- `title`
- `type`
- `status`
- `report_kind`
- `trigger`
- `topics`
- `tags`
- `input_notes`
- `takeaways`
- `action_items`

Optional fields:

- `period_label`
- `focus_question`
- `recommended_next_reads`
- `related_ideas`
- `related_venues`

Defaults:

- report status enum: `draft`, `finalized`, `archived`
- report kind enum: `weekly`, `monthly`, `venue_survey`, `topic_review`, `progress_review`

## Venue Strategy

### Default Venue Sets

- architecture: ISCA, MICRO, HPCA, ASPLOS, DAC, DATE, ICCD
- systems: SOSP, OSDI, EuroSys, USENIX ATC, HotOS
- distributed systems: NSDI, SoCC, Middleware, FAST, EuroSys, OSDI
- network: SIGCOMM, NSDI, IMC, CoNEXT, INFOCOM
- security: USENIX Security, NDSS, IEEE S&P, CCS
- ai systems: MLSys, SysML, selected AI infra papers from OSDI, ATC, EuroSys, ASPLOS, plus NSDI as cross-list

### AI Systems Overflow Pool

Keep a disabled overflow pool for:

- NeurIPS
- ICML
- ICLR

## Planned Workspace Customizations

### Instructions

Workspace instructions should define:

- naming rules
- frontmatter conventions
- note-writing style
- paper review rubric
- report structure expectations

### Prompts

Expected prompts include:

- compare several papers
- turn notes into meeting summary
- convert reading outcomes into report sections

### Skills

Expected skills in phase 1:

- `daily-discovery`
- `venue-survey`
- `paper-analyze`
- `idea-synthesis`
- `report-writer`
- `paper-search`
- `extract-paper-images`

## Python Environment Strategy

- Environment root: `.conda`
- Use workspace-local Python for all scripts and validation
- Avoid dependence on global base Conda environment

## Implementation Phases

### Phase A - Scaffold

- create durable plan file
- create workspace folder structure
- configure `.conda`

### Phase B - Core Data Model

- write root config
- write track config files
- write paper, idea, report templates

### Phase C - Copilot Customizations

- write workspace instructions
- write prompts
- write phase-1 skills

### Phase D - Support Scripts

- add helper scripts for validation, indexing, and future asset download

### Phase E - Validation

- validate YAML/frontmatter layouts
- validate file placement under `.github/`
- validate environment assumptions and internal consistency

### Phase F - Documentation

- write root usage guide

## Progress Tracker

- [x] Phase A - Scaffold
- [x] Phase B - Core Data Model
- [x] Phase C - Copilot Customizations
- [x] Phase D - Support Scripts
- [x] Phase E - Validation
- [x] Phase F - Documentation

## Session Log

### 2026-04-26

- Durable plan file created in workspace root.
- Workspace skeleton created.
- Workspace-local `.conda` environment configured.
- Root config, track presets, note templates, prompts, instructions, and phase-1 skills created.
- Validation script passed in the local `.conda` environment.
- Index generation script created and executed successfully.
- Root usage guide written.
- Chinese usage guide written for mixed-language day-to-day readability.
- Implementation is ready for practical use and future iteration.

## Completion Status

This phase-1 implementation is complete.

Remaining future work is optional and iterative:

- enrich search and discovery with more automation or external APIs
- expand embodied systems defaults when needed
- add more helper scripts for asset extraction or literature ingestion
- tune prompts, skills, and venue presets based on real usage
