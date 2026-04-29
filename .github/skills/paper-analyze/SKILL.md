---
name: paper-analyze
description: "Use when deeply analyzing a paper from arXiv, DOI, URL, title, or venue result. Produces a structured paper note focused on problem, design, evidence, limits, research relevance, workflow position, and research-object mapping when available."
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
5. If the reading happens interactively in chat, progressively revise the same paper note after each user-confirmed clarification instead of waiting for a final cleanup pass.
6. When the user asks multiple clarification questions at once, answer all of them in one response by default unless they explicitly request step-by-step gating. Preserve depth by giving each question its own focused subsection with mechanism, example, assumptions, evidence boundary, and research implication when relevant.
7. Do not compress or soften technical precision just because multiple questions are answered together. If needed, use a short recap at the end instead of shortening the individual answers.
8. Prefer folding these clarifications back into the existing note sections. If a question exposes ambiguity that would otherwise remain hidden, add a short clarification subsection for methods, metrics, baselines, assumptions, scheduling behavior, or workflow position.
9. Treat repeated user questions as diagnostic signals, not interruptions. Track whether the confusion comes from missing workflow context, unclear first-class system object, hidden control owner, opaque state/resource visibility, unfamiliar experiment semantics, or a gap between the paper's abstraction and the user's research framing.
10. If those signals point to missing topic context rather than a paper-local detail, add or revise a short workflow/object-position paragraph in the note and hand off to `topic-workflow-map` when the broader lifecycle or layer map needs repair.
11. For papers that shape a research direction, fill a compact object map in the note: `first_class_state`, `control_owner`, `resource_bottleneck`, `hardware_visible_signal`, `abstraction_maturity`, and `open_boundary`.
12. At the end of an interactive deep-read, run an after-action reflection: explain why the hard questions arose, identify which workflow or skill gap they exposed, and propose skill updates before editing unless the user has already approved a default implementation.
13. Capture the problem, motivation, key ideas, and system design.
14. Place the paper inside the broader workflow or layered stack when that framing exists.
15. When summarizing experiments, explain each workload as a concrete task or workflow, not just by dataset or benchmark name.
16. Distinguish system baselines from policy/configuration baselines, and state what each baseline stack is actually comparing against.
17. Define every evaluation metric in plain language and tie it to the user-visible or system-level behavior it represents, especially for cross-domain papers where metric names may be unfamiliar.
18. Evaluate evidence strength, baseline quality, and missing experiments.
19. Record limitations, assumptions, and research relevance.
20. Link related idea notes if the paper directly triggers a hypothesis.
21. If figures or artifacts matter, hand off to `extract-paper-images` or store follow-up links under `attachments/`.

## Output Expectations

- decisive summary, not paper paraphrase
- centered on the original paper rather than a secondary-source retelling
- explicit evaluation of rigor and assumptions
- clear statement of which workflow stage or layer the paper belongs to when relevant
- clear statement of why the paper matters or does not matter
- during interactive deep-read sessions, the note should improve incrementally after each clarified question, especially when the clarification changes how methods, metrics, baselines, or assumptions are understood
- experiment sections should make the workload, baseline, and metric semantics legible to a reader who does not already know the subfield jargon
- research-direction papers should make the evolving system-level object explicit, including who controls it and whether it is runtime-visible, hardware-visible, or still only an application-level concept
- when user questions reveal a recurring reading friction, the final note or chat closeout should name the underlying missing context and suggest the smallest useful skill or workflow improvement
- multi-question clarification responses should be complete per question, not shallow summaries; batching is for efficiency, not for reducing analytical rigor
