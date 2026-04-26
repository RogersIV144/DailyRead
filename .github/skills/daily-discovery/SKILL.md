---
name: daily-discovery
description: "Use when discovering recent papers and high-signal research leads for systems, architecture, distributed systems, networking, security, or AI systems. Produces a survey-style discovery report and follow-up reading backlog, and can narrow discovery from an existing workflow map."
argument-hint: "track, topic, keyword, or date window"
user-invocable: true
---

# Daily Discovery

## When to Use

- Find recent papers in the last 30 to 365 days.
- Scan a specific track or topic.
- Drill into a specific layer, bottleneck, or lifecycle stage after running `topic-workflow-map`.
- Build a short research radar before reading deeply.

## Workspace Assumptions

- Root config: `config/dailyread.yaml`
- Track presets: `config/tracks/*.yaml`
- Default template: `templates/survey_report.md`
- Workspace-local Python: `.conda/python.exe`
- Secondary discovery sources, when enabled, live under the `sources` block in the root config.
- Track-specific source filtering can be refined in the selected preset under `source_overrides`.

## Procedure

1. Read `config/dailyread.yaml` and the selected track config.
2. If a `topic-workflow-map` report already exists, reuse its focus question, layer terminology, lifecycle boundaries, and intervention hypotheses to narrow the scan.
3. Determine the topic, track, and year window. Default to `recent_90d` when unspecified.
4. Search recent papers using the venue and category hints for the selected track.
5. Apply any track-level `source_overrides` before using secondary sources.
6. Use enabled secondary sources such as Chaspark for high-signal blogs, paper roundups, or topic briefs that improve prioritization.
7. When a lead comes from Chaspark, resolve canonical paper metadata before creating notes or backlog entries.
8. Rank candidates using the `daily_discovery` scoring block in the root config.
9. Produce a survey-style report under `reports/`.
10. Include a backlog or follow-up section for promising papers that were not fully analyzed.
11. Add especially promising papers to `inbox/` or create linked paper notes when explicitly requested.

## Output Expectations

- Short thematic synthesis, not just a paper list
- Top papers and why they matter
- High-signal secondary context only when it changes prioritization
- Paper candidates positioned against the selected workflow stage or layer when a workflow map is available
- Follow-up reading backlog
- Action items for next reading steps
