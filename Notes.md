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