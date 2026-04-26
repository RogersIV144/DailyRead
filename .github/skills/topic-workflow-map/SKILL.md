---
name: topic-workflow-map
description: "Use when mapping a topic's end-to-end workflow, lifecycle, key layers, and system versus architecture intervention points before deeper discovery or paper analysis. Produces a beginner-friendly workflow report and next-step handoff."
argument-hint: "track, topic, focus question, or time window"
user-invocable: true
---

# Topic Workflow Map

## When to Use

- Enter a new topic and build orientation before reading papers deeply.
- Clarify how a downstream task fits into the larger application or systems workflow.
- Compare where system optimization and architecture optimization differ across a topic's lifecycle.
- Decide which sub-stage is most worth deeper discovery, venue survey, or paper analysis.

## Workspace Assumptions

- Root config: `config/dailyread.yaml`
- Track presets: `config/tracks/*.yaml`
- Workflow template: `templates/workflow_report.md`
- Reports live under `reports/`
- Existing paper, survey, and report notes can be reused as context when available.

## Procedure

1. Resolve the requested topic, track, and optional focus question or time window.
2. Clarify the topic boundary before collecting papers. If the topic label is overloaded, explicitly separate adjacent meanings.
3. Map the end-to-end workflow or lifecycle first, including upstream inputs, core processing stages, deployment path, and downstream application layer.
4. Propose the most useful layered decomposition for this topic and explain why that decomposition is better than a flat paper list.
5. For each layer or lifecycle stage, explain the role of the workload, the main bottlenecks, and what systems work versus architecture work usually means there.
6. Identify the 1 to 3 most promising sub-stages for deeper study, and explain why they are better targets than nearby crowded or lower-leverage stages.
7. Recommend anchor readings that establish the minimum useful mental model for this topic.
8. Write the result as a workflow report under `reports/` using the workflow template.
9. End with a concrete handoff to one or more downstream skills such as `daily-discovery`, `venue-survey`, `paper-analyze`, `idea-synthesis`, or `report-writer`.

## Output Expectations

- beginner-friendly orientation instead of jargon-heavy shorthand
- explicit workflow or lifecycle map, not only a list of papers
- clear separation between system roles and architecture roles
- concrete judgment about where deeper research effort is most worthwhile
- downstream handoff with focus questions and terminology to reuse