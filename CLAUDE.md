# Instructions for Organizing and Updating Notes

## Overview
You ar a notes organizer. Read for the the Obsidian Notes Vault on the local machine from the following path

~/Library/Mobile\ Documents/iCloud\~md\~obsidian/Documents/Notes 

There are 2 types of notes. 
- Daily notes in the format YYYY-MM-DD.md files
- Topic notes such as Python.md, Climate.md etc.

You need to read the daily notes and append new notes to the topic notes.
- Do not delete any topic notes
- Once the daily notes are processed, move them to a processed/ folder in the vault.
- Once the topic notes are updated in the local Vault, copy them over to this github repo in the notes/ folder (this repo's `docs_dir`, published via MkDocs). Also copy any new topic note over to notes/index.md's Topics section (card grid) and mkdocs.yml's `nav:` list.

Prioritize the ability to search and recall specific items. These notes are primarily used by me to find references and resources for my students and for my own work.

## Workflow

Always to git pull to fetch the latest changes from Github.

### Processing for the first time
- Identify all topic notes. Merge similar topics in a single file
- Follow the topic notes processing instructions below

### Processing for subsequent runs
- Update topic notes first, if there are new notes which were not processed, processing them first.
- Next go to any new daily notes and process them.

### Update the website
- Update the "Latest Finds" section in notes/index.md with 3 latest notes. Ensure each note is from a different topic. Do not pick these from Misc.md.
- Append an entry to notes/log.md with the date and a short summary of what changed (new/updated topic pages, daily notes processed).
- Push the notes to GitHub (`git add`, `git commit`, `git push`). The site is published via a GitHub Actions workflow (`.github/workflows/deploy.yml`) that builds with MkDocs and deploys to GitHub Pages automatically on every push to `main` — no manual `mkdocs gh-deploy` needed.

## Instructions

### General Notes Organizing Instructions
- Use Markdown format for notes.
- Use a bullet point for each note
- Follow the format [title](url]): 1-2 line description
- Visit the URL and generate an accurate short description
- If there are more than 1 link, use the best link for url but include other links as [GitHub](github link), [Learn more](other_link) etc.
- Add 3-6 keywords focused on tech stack, programming language, and application area, formatted as a plain comma-separated list at the end of the entry: `Keywords: keyword one, keyword two, keyword three` (no brackets, no backticks).
- Add related-topic backlinks where relevant: if the note's keywords or description clearly relate to another topic page, add `Related: [[Other_Topic]], [[Another_Topic]]` (as `[[Page_Name]]` wiki-links, using the topic page's filename) right before the `Keywords:` list. Infer these from the keywords/description first; only look up the web for a note's subject if it's genuinely unclear which other topics it relates to. Don't force a Related link if none is genuinely relevant — it's fine to omit it. The `roamlinks` MkDocs plugin resolves `[[Page_Name]]` into a working link at build time.

### How to process the topic notes
- The topic notes needs to be organized in reverse chornological order with newest note on the top.
- Organize in sections for each year. 2026 at the top.
- Add notes taken during that year in its own section.
- For existing notes, first organize them using instructions for *General Notes Organizing Instructions* section above.
- Every topic page starts with a title, then a `**Summary**` (one to two sentences describing the page) and `**Last updated**` (date of most recent update) header, then a `---` divider, before the year sections:
  ```markdown
  # Page Title

  **Summary**: One to two sentences describing this page.
  **Last updated**: 2026-08-20

  ---

  ## 2026

  - [title](url): description. Related: [[Other_Topic]]. Keywords: keyword one, keyword two
  ```
  Update `**Last updated**` whenever a topic page gets a new entry.
- Keep page filenames Title Case with underscores (e.g. `Machine_Learning.md`), matching the `[[Page_Name]]` used in Related links.
- Following notes should not be processed or moved to GitHub
    - name containing words TODO, Template, Thoughts
    - Newsletter.md

### How to process daily notes
- Read each item in the note. If there is already a liniked topic in the [[Topic]] format, add the note to that topic file. Replace spaces in topic files with an underscore _.
- If there is no topic linked, visit the URL, read the text and decide on the best topic. 
- Ideally, it should fit within an existing topic but if there is no topic file for the best fit topic, create a new one.
- If there is any description and/or text along with the URL/Title, keep it verbatim in the output descriptions. You may fix grammar and typos in existing description. You may add extra text to the description if the supplied discription is too short.
