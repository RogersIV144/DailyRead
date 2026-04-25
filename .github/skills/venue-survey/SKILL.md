---
name: venue-survey
description: "Use when surveying one or more venues by year range, topic, or keyword. Produces a structured venue survey report for systems and AI systems research."
argument-hint: "venue list, topic, year range, or track"
user-invocable: true
---

# Venue Survey

## When to Use

- Study a venue over the last few years.
- Understand research trends in a conference family.
- Build a direction overview before committing to deep reading.

## Workspace Assumptions

- Venue metadata lives in `config/dailyread.yaml`.
- Track presets live in `config/tracks/*.yaml`.
- Default template: `templates/survey_report.md`.

## Procedure

1. Resolve the requested venue list or track preset.
2. Default to `recent_5y` when the user does not specify a time window.
3. Search papers and metadata from the configured venue sources.
4. Filter by topic, keywords, and track-specific notes.
5. Synthesize the venue landscape rather than summarizing papers independently.
6. Write the result as a survey report under `reports/`.
7. Optionally create `inbox/` leads or full paper notes for the most important papers.

## Output Expectations

- venue scope and trigger
- thematic synthesis
- highlighted papers
- gap map
- follow-up reading backlog
- concrete action items
