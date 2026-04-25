---
name: paper-analyze
description: "Use when deeply analyzing a paper from arXiv, DOI, URL, title, or venue result. Produces a structured paper note focused on problem, design, evidence, limits, and research relevance."
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

## Procedure

1. Resolve the paper from paper key, title, DOI, URL, or prior survey output.
2. Create or update a paper note using the deep paper template.
3. Capture the problem, motivation, key ideas, and system design.
4. Evaluate evidence strength, baseline quality, and missing experiments.
5. Record limitations, assumptions, and research relevance.
6. Link related idea notes if the paper directly triggers a hypothesis.
7. If figures or artifacts matter, hand off to `extract-paper-images` or store follow-up links under `attachments/`.

## Output Expectations

- decisive summary, not paper paraphrase
- explicit evaluation of rigor and assumptions
- clear statement of why the paper matters or does not matter
