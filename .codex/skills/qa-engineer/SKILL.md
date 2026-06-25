---
name: qa-engineer
description: Use for quality review of budgetApp changes, checking tests, type hints, complexity, and TDD compliance before commit.
metadata:
  short-description: Quality review for budgetApp
---

# QA Engineer

Use this skill to review budgetApp changes before a commit.

## Review Checklist

- Confirm tests were written before implementation.
- Check that affected functions have type hints.
- Check functions stay within 50 lines when practical.
- Check cyclomatic complexity stays at 10 or below.
- Check `pytest` is passing.
- Check `radon cc` does not report problematic complexity.

## Output

- Report concrete issues first.
- Mention missing tests, risky logic, or rule violations.
- If nothing is wrong, say the change looks ready to commit.
