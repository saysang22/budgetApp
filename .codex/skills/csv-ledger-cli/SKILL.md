---
name: csv-ledger-cli
description: Use for this Python CSV-based accounting CLI project to apply repo rules, enforce TDD, and prepare changes for QA review and commits.
---

# CSV Ledger CLI

Use this skill for work in the CSV-based accounting CLI app.

## Workflow

1. Start with a failing test.
2. Implement the smallest change to pass.
3. Keep functions typed and short.
4. Keep complexity low.
5. Run `pytest` and `radon cc`.
6. Before committing, hand the change to `qa_engineer`.
7. Commit and push once one feature is complete.

## Constraints

- Prefer small, focused changes.
- Every function needs type hints.
- Keep each function at 50 lines or fewer.
- Keep cyclomatic complexity at 10 or below.

## QA Gate

Use the `qa_engineer` subagent to review correctness, test coverage, and complexity before any commit.
