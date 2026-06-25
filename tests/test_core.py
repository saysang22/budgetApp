"""Tests for budget.core."""

from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    """Adding a transaction should increase the collection length."""
    transactions = []
    transaction = {
        "date": "2026-01-01",
        "type": "income",
        "category": "salary",
        "description": "January salary",
        "amount": 3000000,
        "memo": "",
    }

    add_transaction(transactions, transaction)

    assert len(transactions) == 1
