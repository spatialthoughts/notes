# Instructions for Organizing and Updating Notes

## Overview

A personal notes organizer maintained by Claude Code. This repo *is* the Obsidian vault — open it in Obsidian directly, and it also builds and publishes as a MkDocs site on GitHub Pages.

Prioritize the ability to search and recall specific items. These notes are primarily used by me to find references and resources for my students and for my own work.

## Folder structure

```
- raw/       -- documents containing unprocessed notes (drop new notes into raw/New_Notes.md)
- processed/ -- documents containing processed notes (gitignored, stays local, never pushed)
- notes/     -- markdown pages for the organized topic notes; also the MkDocs docs_dir
- notes/index.md -- table of contents of all the notes pages + "Latest Finds"
- notes/log.md   -- append-only record of all operations
```

## Workflow

Always `git pull` to fetch the latest changes from GitHub first.

- Read the unprocessed notes in `raw/` (daily-note-style dumps, a pasted URL, a clipped article, or plain text).
- Process each document and every note inside it using the Processing Instructions below.
- Once processed, move the source document to `processed/`.
- Re-add an empty `raw/New_Notes.md` so there's always an inbox file to collect new notes.

## Processing Instructions

When a new note is added to `raw/` and I ask you to ingest it:

- If the note has one or more URLs, visit them and generate an accurate short description.
- If there is any description and/or text already accompanying the URL/title, keep it verbatim in the output description — fix grammar/typos if needed, and add extra text if the supplied description is too short, but never lose the original wording.
- Identify the core concept/topic of the resource, and any related topics.
- Read `notes/index.md` first to find relevant existing topic pages.
- If there's no good match, a new topic page can be created — see the List of Topics below for topics of interest, but don't be limited to it.
- Add a new item to the main topic page, keeping newer notes at the top of their year's section.
- **Every note must have a `Related:` link to at least one other topic page** — infer it from the note's keywords/description first; only look up the web for the note's subject if it's genuinely unclear which other topic it relates to. If the related topic page doesn't exist yet, create it.
- Update `notes/index.md` with any new topic pages and a one-line description, and add the page to `mkdocs.yml`'s `nav:` list.
- Append an entry to `notes/log.md` with the date, source name, and what changed.
- Following notes should not be processed or moved to GitHub:
    - Names containing the words TODO, Template, or Thoughts
    - Newsletter.md

## Update the Website

This vault is published as a MkDocs site on GitHub Pages via GitHub Actions (`.github/workflows/deploy.yml`, Actions-based Pages deploy). After ingesting new notes:

- Update the "Latest Finds" section in `notes/index.md` with the 3 most recently added notes, each from a different topic page. Don't pick these from Misc.md.
- Commit and push the changes to GitHub (`git add`, `git commit`, `git push`) so the site rebuilds and redeploys automatically. `processed/` stays gitignored and is never pushed.

## List of Topics

Existing topic pages — the theme-focused topic is the primary one when a note covers both a technology and a theme.

Technology Topics
- Python, PyQGIS, QGIS
- SQL, DuckDB, XArray
- Git
- AI, Machine Learning, Deep Learning, Embeddings
- Claude Code
- STAC, CNG (Cloud Native Geospatial)
- GEE (Google Earth Engine)
- Data
- Tools

Thematic Topics
- Cartography, Web Mapping
- Remote Sensing
- Climate
- Agriculture
- Water Resources
- Urban Planning
- Papers
- Misc (catch-all; excluded from Latest Finds and from other pages' Related links)

## Topic Page Format

Every note topic page should follow this structure:

```markdown
# Page Title

**Summary**: One to two sentences describing this page.
**Last updated**: Date of most recent update.

---

## 2026

- [title](url): description. Related: [[Other_Topic]], [[Another_Topic]]. Keywords: keyword one, keyword two
```

- Organize each page in reverse chronological order, newest note first, in sections by year (`## 2026` at the top).
- For notes with URLs, follow the format `[title](url): description`. If there's more than one link, use the best one as the main URL but include the others inline as `[GitHub](github link)`, `[Learn more](other link)`, etc.
- For notes with just text (no URL), follow the format `*Title*: note text` and don't summarize — add it verbatim.
- Add `Related: [[Page_Name]]` wiki-links to connect to other relevant topic pages — required on every note (see Processing Instructions above).
- Add 3-6 keywords that best describe the note and will aid recall later, as a plain comma-separated list: `Keywords: keyword one, keyword two, keyword three` (no brackets, no backticks).
- Update `**Last updated**` whenever a page gets a new entry.

## Rules

- Keep page filenames Title Case with underscores (e.g. `Machine_Learning.md`), matching the `[[Page_Name]]` used in Related links.
- Write in clear, plain language.
- Do not delete any topic notes.
- Always update `notes/log.md` after changes.
