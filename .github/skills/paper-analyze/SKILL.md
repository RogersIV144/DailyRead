---
name: paper-analyze
description: "Use when deeply analyzing a paper from arXiv, DOI, URL, title, or venue result. Produces a structured paper note focused on problem, design, evidence, limits, research relevance, and workflow position when available."
argument-hint: "paper key, title, DOI, URL, or note target"
user-invocable: true
---

# Paper Analyze

## When to Use

- Convert a promising paper into a deep paper note.
- Read beyond the abstract and capture systems-relevant judgment.
- Connect a paper to your current research direction.

## Workspace Assumptions

- Default template: `templates/deep_paper_note.md`
- Paper notes live under `papers/`
- Attachments, if needed, live under `attachments/`
- Canonical paper metadata should win over any secondary blog summary when both are available.

## Procedure

1. Resolve the paper from paper key, title, DOI, URL, prior survey output, or a discovery lead.
2. If a `topic-workflow-map` report exists for this topic, reuse its layer terminology, lifecycle framing, and focus question while reading the paper.
3. If the input is a Chaspark blog, roundup, or topic brief, first resolve the original paper URL, venue, authors, and year.
4. Create or update a paper note using the deep paper template.
5. Capture the problem, motivation, key ideas, and system design.
6. Place the paper inside the broader workflow or layered stack when that framing exists.
7. Evaluate evidence strength, baseline quality, and missing experiments.
8. Record limitations, assumptions, and research relevance.
9. Link related idea notes if the paper directly triggers a hypothesis.
10. If figures or artifacts matter, hand off to `extract-paper-images` or store follow-up links under `attachments/`.

## Output Expectations

- decisive summary, not paper paraphrase
- centered on the original paper rather than a secondary-source retelling
- explicit evaluation of rigor and assumptions
- clear statement of which workflow stage or layer the paper belongs to when relevant
- clear statement of why the paper matters or does not matter
