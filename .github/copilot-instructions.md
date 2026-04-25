# DailyRead Project Guidelines

## Scope

This workspace is a research workflow repository for paper discovery, deep reading, idea capture, and report writing.
Treat the workspace root as the primary knowledge base and write outputs into this repository instead of relying on any external vault.

## Storage Rules

- Keep paper notes under `papers/`.
- Keep idea notes under `ideas/`.
- Keep reports under `reports/`.
- Keep temporary leads under `inbox/`.
- Keep generated indexes under `index/`.
- Keep templates under `templates/`.
- Keep workflow configuration under `config/`.

## Metadata Rules

- Use YAML frontmatter for paper, idea, and report notes.
- Keep enum values in `snake_case`.
- Store cross-note references as stable keys, not file paths.
- Preserve placeholder fields in templates unless a file intentionally removes them.

## Writing Rules

- Use mixed-language note bodies: Chinese for reasoning and conclusions, English for paper titles, method names, systems, and technical terms.
- Prefer concise, structured summaries over long prose.
- When analyzing papers, separate problem, design, evidence, limits, and relevance to current research.
- When writing reports, keep takeaways and action items mirrored in frontmatter and in the body.

## Python and Scripts

- Use the workspace-local `.conda` environment for Python scripts.
- Prefer updating `IMPLEMENTATION_PLAN.md` when implementation milestones change.
- Prefer lightweight scripts under `scripts/` and keep them aligned with `config/dailyread.yaml`.

## Customization Strategy

- Put reusable workflow logic into `.github/skills/`.
- Put single focused tasks into `.github/prompts/`.
- Put file-specific guidance into `.github/instructions/`.
- Do not add a custom agent unless a task clearly needs orchestration or context isolation.
