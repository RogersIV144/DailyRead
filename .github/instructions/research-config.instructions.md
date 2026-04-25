---
description: "Use when editing DailyRead YAML configuration, track presets, venue tables, or template metadata. Covers naming, enum style, and config consistency."
name: "Research Config Guidelines"
applyTo:
  - config/**/*.yaml
  - templates/**/*.md
---

# Research Config Guidelines

- Keep enum values in `snake_case`.
- Use lower-case slugs for venue keys.
- Prefer relative workspace paths in config.
- When a field is optional in templates, preserve type-aware empty placeholders.
- Keep venue ordering aligned with default priority, not alphabetic order.
- When a venue appears in multiple tracks, keep the notes aligned with that track's perspective.
