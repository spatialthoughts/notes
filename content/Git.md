# Git

## Tips and Tricks

### Delete Git History (Orphan Branch Method)

[Video Tutorial](https://www.youtube.com/watch?v=2yeM0v4tYpw) on deleting Git history using orphan branches.

```bash
git checkout gh-pages
git checkout --orphan last
git add -A
git commit -am 'fresh init'
git branch -D gh-pages
git branch -m gh-pages
git push -f origin gh-pages
git gc --aggressive --prune=all
```
Keywords: Git, history, orphan branch, clean, GitHub Pages
