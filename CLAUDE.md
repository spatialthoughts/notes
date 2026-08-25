# Instructions for Organizing and Updating Notes

## Overview

A personal notes organizer maintained by Claude Code. This repo *is* the Obsidian vault for topic notes — open it in Obsidian directly, and it also builds and publishes as a MkDocs site on GitHub Pages.

Quick-capture, including from mobile, happens by appending to `raw/New_Notes.md` — a single running inbox. That file physically lives in the Obsidian vault synced via iCloud at `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Notes/raw/`, which is the only thing left in that iCloud vault besides its `.obsidian/` config. This repo's `raw/` (gitignored — it's really a machine-specific absolute-path symlink, never pushed) points straight at it, so the exact same file can be read and processed directly from here. There's also a broader `icloud-vault/` symlink (also gitignored) to the iCloud vault root, in case anything besides `raw/` ever lives there again.

Prioritize the ability to search and recall specific items. These notes are primarily used by me to find references and resources for my students and for my own work.

## Folder structure

```
- raw/             -- symlink (gitignored) to the iCloud-synced inbox where new notes are
                       captured, incl. from mobile; raw/New_Notes.md is the running inbox file
- icloud-vault/     -- symlink (gitignored) to the root of that iCloud-synced vault
- processed/       -- documents processed from raw/ (gitignored, stays local, never pushed)
- notes/           -- markdown pages for the organized topic notes; also the MkDocs docs_dir
- notes/index.md   -- table of contents of all the notes pages + "Latest Finds"
- notes/log.md     -- append-only record of all operations
```

## Workflow

Always `git pull` to fetch the latest changes from GitHub first.

- Read the unprocessed notes in the `raw/` folder.
- Process each document and all notes inside using the processing instructions below.
- Once processed, move it to the `processed/` folder.
- Add an empty file `New_Notes.md` in the `raw/` file to collect new notes.

## Processing Instructions

When the user adds a new note to `raw/` and asks you to ingest it

* Read the New_Notes.md and process all notes from it.
	* If the note has one or more URLs,  visit them and generate an accurate short description.
	* For notes with text upto 100 characters, add it verbatim. For longer notes, summarize it up to 100 characters.
* Read any other files added to the `raw/` folder and process each file as a separate note.
* If the note has one or more URLs,  visit them and generate an accurate short description.
* Identify the core concepts/topic of the resource. 
* Identify the main topic and related topics. If the resource neatly fits into a single main topic - you do not have to have a related topic.
* Read `notes/index.md` first to find relevant topic pages.
* If there is no match, a new topic page can be added. See the list of topics below for additional topics of interest.
* Add a new item to the main topic page. Keeping the newer notes at the top.
* Add back-links ([[page-name]]) to connect related topics. If the related topic page does not exist, create the page.
* Update `notes/index.md` with new pages and one-line descriptions.
* Append an entry to `notes/log.md` with the date, source name, and what changed

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

- Use Markdown format for each note.
- Use a bullet point for each note
- For notes with URLs, 
	  - Follow the format [title](url]): <description> <keywords>
	  - If there is text accompanying the URL, add it verbatim. 
	  - Add a 1-2 line description from the URLs
- For notes with just text, 
	  - Follow the format *Title*: note text <keywords>
	  - do not summarize notes with just text. add it verbatim.
- Add 3-6 keywords that best describe the note and will aid in recalling them later.

Link to related topics using [[wiki-links]] throughout the text.

## Rules

- Keep page filenames Title Case with underscores (e.g. `Machine_Learning.md`), matching the `[[Page_Name]]` used in Related links.
- Write in clear, plain language.
- Always update `notes/log.md` after changes.
