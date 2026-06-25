---
name: budget-app-cli
description: Use for this repository's Python CSV-based budget CLI app rules, TDD workflow, and quality checks.
metadata:
  short-description: Budget app repo rules and workflow
---

# Budget App CLI

Use this skill when working in the `budgetApp` repository.

## Core Rules

- Write tests first, then implement behavior.
- Keep type hints on all functions and public data structures.
- Keep each function to 50 lines or fewer.
- Keep cyclomatic complexity at 10 or below.
- Before every commit, run the `qa_engineer` review.

## Test Commands

- `pytest`
- `radon cc`

## Commit Workflow

- Finish one feature at a time.
- Commit and push after each completed feature.

## Implementation Notes

- Prefer small CSV-focused helpers.
- Keep logic simple enough to be covered by tests before implementation.
