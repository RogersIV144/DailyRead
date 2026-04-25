---
name: paper-search
description: "Use when searching local paper notes and idea notes by topic, tag, venue, title, author, or paper key. Returns concise results with direct follow-up suggestions."
argument-hint: "paper key, topic, tag, venue, or author"
user-invocable: true
---

# Paper Search

## When to Use

- Search existing notes before re-reading or re-writing.
- Find all notes linked to a venue, topic, or idea.
- Retrieve prior analysis for a known paper key.

## Workspace Assumptions

- Default search scope is `papers/` and `ideas/`.
- Search behavior is governed by `config/dailyread.yaml`.
- Generated indexes live under `index/` when available.

## Procedure

1. Search by paper key first when available.
2. Then search by title, venue, topic, tag, or author.
3. Prefer exact and high-signal matches over broad fuzzy search.
4. Return concise hits with note type, title, and why each result matches.
5. Suggest the next action: open note, compare papers, synthesize idea, or write report.

## Output Expectations

- compact, high-signal results
- note type and stable key surfaced early
- clear next-step suggestion
