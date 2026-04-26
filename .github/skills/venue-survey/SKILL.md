---
name: venue-survey
description: "Use when surveying one or more venues by year range, topic, or keyword. Produces a structured venue survey report for systems and AI systems research, and can focus the survey using an existing workflow map."
argument-hint: "venue list, topic, year range, or track"
user-invocable: true
---

# Venue Survey

## When to Use

- Study a venue over the last few years.
- Understand research trends in a conference family.
- Test how one workflow stage or layer appears across venues after running `topic-workflow-map`.
- Build a direction overview before committing to deep reading.

## Workspace Assumptions

- Venue metadata lives in `config/dailyread.yaml`.
- Track presets live in `config/tracks/*.yaml`.
- Default template: `templates/survey_report.md`.
- Primary venue inventories should come from configured venue sources, not editorial recap sites.

## Procedure

1. Resolve the requested venue list or track preset.
2. If a `topic-workflow-map` report exists, use its target layer, lifecycle stage, and focus question to choose the most relevant venues and time window.
3. Default to `recent_5y` when the user does not specify a time window.
4. Search papers and metadata from the configured venue sources.
5. Use editorial sources such as Chaspark only after the canonical venue list is built, and only for extra context or prioritization.
6. Filter by topic, keywords, and track-specific notes.
7. Synthesize the venue landscape rather than summarizing papers independently.
8. Write the result as a survey report under `reports/`.
9. Optionally create `inbox/` leads or full paper notes for the most important papers.

## Output Expectations

- venue scope and trigger
- thematic synthesis
- papers positioned against the targeted workflow stage or layer when that framing exists
- highlighted papers
- gap map
- follow-up reading backlog
- concrete action items
