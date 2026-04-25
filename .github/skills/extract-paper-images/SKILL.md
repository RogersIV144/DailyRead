---
name: extract-paper-images
description: "Use when collecting figures, PDF links, project pages, code links, or local assets for a target paper. Stores outputs under the workspace attachments directory."
argument-hint: "paper key, URL, DOI, or target note"
user-invocable: true
---

# Extract Paper Images

## When to Use

- A paper contains figures worth preserving for future notes or reports.
- You need local asset organization for a high-value paper.
- You want an attachment trail without committing to full PDF caching for everything.

## Workspace Assumptions

- Attachments root: `attachments/`
- Paper notes live under `papers/`
- Use the workspace-local `.conda` environment for any helper scripts.

## Procedure

1. Resolve the target paper and its stable key.
2. Check whether the existing paper note already records PDF, project, or code links.
3. Create a paper-specific attachment folder under `attachments/` when needed.
4. Prefer storing high-value assets only: figure images, artifact links, or canonical PDF references.
5. Update the related note or follow-up task if asset collection is incomplete.

## Output Expectations

- organized attachment location
- explicit record of what was captured
- no blind full-repository asset dumping
