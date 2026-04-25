---
name: daily-discovery
description: "Use when discovering recent papers for systems, architecture, distributed systems, networking, security, or AI systems. Produces a survey-style discovery report and follow-up reading backlog."
argument-hint: "track, topic, keyword, or date window"
user-invocable: true
---

# Daily Discovery

## When to Use

- Find recent papers in the last 30 to 365 days.
- Scan a specific track or topic.
- Build a short research radar before reading deeply.

## Workspace Assumptions

- Root config: `config/dailyread.yaml`
- Track presets: `config/tracks/*.yaml`
- Default template: `templates/survey_report.md`
- Workspace-local Python: `.conda/python.exe`

## Procedure

1. Read `config/dailyread.yaml` and the selected track config.
2. Determine the topic, track, and year window. Default to `recent_90d` when unspecified.
3. Search recent papers using the venue and category hints for the selected track.
4. Rank candidates using the `daily_discovery` scoring block in the root config.
5. Produce a survey-style report under `reports/`.
6. Include a backlog or follow-up section for promising papers that were not fully analyzed.
7. Add especially promising papers to `inbox/` or create linked paper notes when explicitly requested.

## Output Expectations

- Short thematic synthesis, not just a paper list
- Top papers and why they matter
- Follow-up reading backlog
- Action items for next reading steps
