# Git Cheat Sheet

## Phase 1 — Basics

| Command | What it does |
|---|---|
| `git config --global user.name "Name"` | Set your name |
| `git config --global user.email "email"` | Set your email |
| `git init` | Initialize a new repo |
| `git status` | See what's changed |
| `git add <file>` | Stage a file |
| `git add .` | Stage all files |
| `git commit -m "message"` | Save a snapshot |
| `git log` | View full history |
| `git log --oneline` | View history (compact) |

## Phase 2 — Branching & Merging

| Command | What it does |
|---|---|
| `git branch` | List all branches |
| `git branch <name>` | Create a new branch |
| `git switch <name>` | Switch to a branch |
| `git merge <name>` | Merge a branch into current branch |
| `git branch -d <name>` | Delete a merged branch |

### Key Concepts
- Branches let you work on features without touching master
- The `*` shows which branch you're currently on
- `Fast-forward` merge = master hadn't changed, Git just moved it forward
- Deleting a branch does NOT delete your commits, just the label
- Always switch TO master before merging a feature branch in

## Phase 3 — History & Undoing Things

| Command | What it does |
|---|---|
| `git diff` | See exactly what changed since last commit |
| `git restore <file>` | Undo uncommitted changes |
| `git restore --staged <file>` | Unstage a file |
| `git reset --soft HEAD~1` | Remove commit, keep changes staged |
| `git reset --mixed HEAD~1` | Remove commit, unstage changes |
| `git reset --hard HEAD~1` | Remove commit AND delete changes ⚠️ |
| `git revert <hash>` | Safely undo a commit, keeps history |

### Key Concepts
- Always use `git diff` before committing to review changes
- `git restore` is permanent for uncommitted changes — be careful!
- `git revert` = safe, keeps history, great for team projects
- `git reset` = rewrites history, only use on local commits
- HEAD~1 means "one commit behind where I am now"