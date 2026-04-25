from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import json

from dailyread_utils import ROOT, iter_markdown_files, read_frontmatter


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def markdown_link(path: Path, label: str) -> str:
    rel = relative(path)
    return f"- [{label}]({rel})"


def main() -> int:
    paper_notes = list(iter_markdown_files([ROOT / "papers"]))
    idea_notes = list(iter_markdown_files([ROOT / "ideas"]))
    report_notes = list(iter_markdown_files([ROOT / "reports"]))

    topic_to_papers: dict[str, list[tuple[str, Path]]] = defaultdict(list)
    venue_to_papers: dict[str, list[tuple[str, Path]]] = defaultdict(list)
    topic_to_ideas: dict[str, list[tuple[str, Path]]] = defaultdict(list)
    kind_to_reports: dict[str, list[tuple[str, Path]]] = defaultdict(list)

    catalog: dict[str, list[dict[str, str]]] = {
        "papers": [],
        "ideas": [],
        "reports": [],
    }

    for path in paper_notes:
        frontmatter, _ = read_frontmatter(path)
        title = str(frontmatter.get("title", path.stem))
        venue = str(frontmatter.get("venue", "unknown"))
        paper_key = str(frontmatter.get("paper_key", path.stem))
        topics = frontmatter.get("topics", []) or []
        catalog["papers"].append({"paper_key": paper_key, "title": title, "path": relative(path)})
        venue_to_papers[venue].append((title, path))
        for topic in topics:
            topic_to_papers[str(topic)].append((title, path))

    for path in idea_notes:
        frontmatter, _ = read_frontmatter(path)
        title = str(frontmatter.get("title", path.stem))
        topics = frontmatter.get("topics", []) or []
        catalog["ideas"].append({"title": title, "path": relative(path)})
        for topic in topics:
            topic_to_ideas[str(topic)].append((title, path))

    for path in report_notes:
        frontmatter, _ = read_frontmatter(path)
        title = str(frontmatter.get("title", path.stem))
        report_kind = str(frontmatter.get("report_kind", "unknown"))
        catalog["reports"].append({"title": title, "path": relative(path)})
        kind_to_reports[report_kind].append((title, path))

    index_root = ROOT / "index"
    index_root.mkdir(parents=True, exist_ok=True)

    (index_root / "catalog.json").write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")

    with (index_root / "papers-by-topic.md").open("w", encoding="utf-8") as handle:
        handle.write("# Papers By Topic\n\n")
        if not topic_to_papers:
            handle.write("No paper notes indexed yet.\n")
        for topic in sorted(topic_to_papers):
            handle.write(f"## {topic}\n\n")
            for title, path in sorted(topic_to_papers[topic]):
                handle.write(markdown_link(path, title) + "\n")
            handle.write("\n")

    with (index_root / "papers-by-venue.md").open("w", encoding="utf-8") as handle:
        handle.write("# Papers By Venue\n\n")
        if not venue_to_papers:
            handle.write("No paper notes indexed yet.\n")
        for venue in sorted(venue_to_papers):
            handle.write(f"## {venue}\n\n")
            for title, path in sorted(venue_to_papers[venue]):
                handle.write(markdown_link(path, title) + "\n")
            handle.write("\n")

    with (index_root / "ideas-by-topic.md").open("w", encoding="utf-8") as handle:
        handle.write("# Ideas By Topic\n\n")
        if not topic_to_ideas:
            handle.write("No idea notes indexed yet.\n")
        for topic in sorted(topic_to_ideas):
            handle.write(f"## {topic}\n\n")
            for title, path in sorted(topic_to_ideas[topic]):
                handle.write(markdown_link(path, title) + "\n")
            handle.write("\n")

    with (index_root / "reports-by-kind.md").open("w", encoding="utf-8") as handle:
        handle.write("# Reports By Kind\n\n")
        if not kind_to_reports:
            handle.write("No report notes indexed yet.\n")
        for report_kind in sorted(kind_to_reports):
            handle.write(f"## {report_kind}\n\n")
            for title, path in sorted(kind_to_reports[report_kind]):
                handle.write(markdown_link(path, title) + "\n")
            handle.write("\n")

    with (index_root / "README.md").open("w", encoding="utf-8") as handle:
        handle.write("# DailyRead Indexes\n\n")
        handle.write(f"- Papers: {len(paper_notes)}\n")
        handle.write(f"- Ideas: {len(idea_notes)}\n")
        handle.write(f"- Reports: {len(report_notes)}\n\n")
        handle.write("Generated files:\n\n")
        handle.write("- `catalog.json`\n")
        handle.write("- `papers-by-topic.md`\n")
        handle.write("- `papers-by-venue.md`\n")
        handle.write("- `ideas-by-topic.md`\n")
        handle.write("- `reports-by-kind.md`\n")

    print("DailyRead indexes generated in index/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
