from __future__ import annotations

from pathlib import Path
import re
from typing import Iterable, Iterator

import yaml


ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)


def workspace_path(*parts: str) -> Path:
    return ROOT.joinpath(*parts)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in YAML file: {path}")
    return data


def read_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"Missing or invalid YAML frontmatter: {path}")
    frontmatter_text, body = match.groups()
    frontmatter = yaml.safe_load(frontmatter_text) or {}
    if not isinstance(frontmatter, dict):
        raise ValueError(f"Frontmatter must be a mapping: {path}")
    return frontmatter, body


def iter_markdown_files(paths: Iterable[Path]) -> Iterator[Path]:
    for base in paths:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.is_file():
                yield path


def slugify(text: str) -> str:
    lowered = text.lower().strip()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    return lowered.strip("-")
