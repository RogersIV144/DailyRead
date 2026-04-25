from __future__ import annotations

from pathlib import Path
import sys

from dailyread_utils import ROOT, load_yaml, read_frontmatter


REQUIRED_ROOT_DIRS = [
    ".github",
    "attachments",
    "config",
    "ideas",
    "index",
    "inbox",
    "papers",
    "reports",
    "templates",
    "scripts",
]

REQUIRED_ROOT_FILES = [
    "IMPLEMENTATION_PLAN.md",
    ".github/copilot-instructions.md",
    "config/dailyread.yaml",
    "templates/deep_paper_note.md",
    "templates/idea_note.md",
    "templates/hybrid_report.md",
    "templates/survey_report.md",
]

REQUIRED_CONFIG_KEYS = [
    "general",
    "storage",
    "taxonomy",
    "search",
    "scoring",
    "tracks",
    "tasks",
    "venues",
]

REQUIRED_TEMPLATE_FIELDS = {
    "deep_paper_note.md": [
        "title",
        "type",
        "status",
        "paper_key",
        "year",
        "venue",
        "authors",
        "topics",
        "tags",
        "source_urls",
        "date_added",
        "date_updated",
        "related_ideas",
        "read_priority",
    ],
    "idea_note.md": [
        "title",
        "type",
        "status",
        "topics",
        "tags",
        "origin_papers",
        "confidence",
        "maturity",
        "next_action",
        "blocking_questions",
        "target_venues",
    ],
    "hybrid_report.md": [
        "title",
        "type",
        "status",
        "report_kind",
        "trigger",
        "topics",
        "tags",
        "input_notes",
        "takeaways",
        "action_items",
    ],
    "survey_report.md": [
        "title",
        "type",
        "status",
        "report_kind",
        "trigger",
        "topics",
        "tags",
        "input_notes",
        "takeaways",
        "action_items",
    ],
}


def collect_errors() -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_ROOT_DIRS:
        path = ROOT / relative
        if not path.is_dir():
            errors.append(f"Missing required directory: {relative}")

    for relative in REQUIRED_ROOT_FILES:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"Missing required file: {relative}")

    config_path = ROOT / "config" / "dailyread.yaml"
    if config_path.is_file():
        config = load_yaml(config_path)
        for key in REQUIRED_CONFIG_KEYS:
            if key not in config:
                errors.append(f"Missing top-level config key: {key}")

    for template_name, fields in REQUIRED_TEMPLATE_FIELDS.items():
        template_path = ROOT / "templates" / template_name
        if not template_path.is_file():
            continue
        frontmatter, _ = read_frontmatter(template_path)
        for field in fields:
            if field not in frontmatter:
                errors.append(f"Template {template_name} missing frontmatter field: {field}")

    for skill_file in sorted((ROOT / ".github" / "skills").glob("*/SKILL.md")):
        frontmatter, _ = read_frontmatter(skill_file)
        folder_name = skill_file.parent.name
        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        if name != folder_name:
            errors.append(f"Skill name mismatch: {skill_file} frontmatter name={name!r} folder={folder_name!r}")
        if not description:
            errors.append(f"Skill missing description: {skill_file}")

    for prompt_file in sorted((ROOT / ".github" / "prompts").glob("*.prompt.md")):
        frontmatter, _ = read_frontmatter(prompt_file)
        if not frontmatter.get("description"):
            errors.append(f"Prompt missing description: {prompt_file}")

    for instruction_file in sorted((ROOT / ".github" / "instructions").glob("*.instructions.md")):
        frontmatter, _ = read_frontmatter(instruction_file)
        if not frontmatter.get("description"):
            errors.append(f"Instruction missing description: {instruction_file}")

    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
      print("DailyRead validation failed:")
      for error in errors:
          print(f"- {error}")
      return 1

    print("DailyRead validation passed.")
    print(f"Workspace: {ROOT}")
    print("Validated: config, templates, skills, prompts, instructions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
