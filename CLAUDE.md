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
- Once the topic notes are updated in the local Vault, copy them over to this github repo in the content/ folder.

Prioritize the ability to search and recall specific items. These notes are primarily used by me to find references and resources for my students and for my own work.

## Workflow

### Processing for the first time
- Identify all topic notes. Merge similar topics in a single file
- Follow the topic notes processing instructions below

### Processing for subsequent runs
- Update topic notes first, if there are new notes which were not processed, processing them first.
- Next go to any new daily notes and process them.

### Update the website
- Update the "Latest Finds" section with 3 latest notes. Ensure each note is from a different topic.
- Push the notes to GitHub.

## Instructions

### General Notes Organizing Instructions
- Use Markdown format for notes.
- Use a bullet point for each note
- Follow the format [title](url]): 1-2 line description
- Visit the URL and generate an accurate short description
- Add keywords - focused on tech stack, programming language, application area

### How to process the topic notes
- The topic notes needs to be organized in reverse chornological order with newest note on the top.
- Organize in sections for each year. 2026 at the top.
- Add notes taken during that year in its own section.
- For existing notes, first organize them using instructions for *General Notes Organizing Instructions* section above.
- Following notes should not be processed or moved to GitHub
    - name containing words TODO, Template, Thoughts
    - Newsletter.md

### How to process daily notes
- Read each item in the note. If there is already a liniked topic in the [[Topic]] format, add the note to that topic file. Replace spaces in topic files with an underscore _.
- If there is no topic linked, visit the URL, read the text and decide on the best topic. 
- Ideally, it should fit within an existing topic but if there is no topic file for the best fit topic, create a new one.

