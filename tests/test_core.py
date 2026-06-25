"""Tests for budget.core."""

from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    """Adding a transaction should increase the collection length."""
    transactions = []
    transaction = {
        "date": "2026-01-01",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3000000,
        "memo": "1월급여",
    }

    add_transaction(transactions, transaction)

    assert len(transactions) == 1


def test_add_transaction_preserves_expense_amount() -> None:
    """An expense transaction should keep its negative amount."""
    transactions = []
    transaction = {
        "date": "2026-01-05",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }

    add_transaction(transactions, transaction)

    assert transactions[0]["amount"] == -12000


def test_add_transaction_preserves_income_amount() -> None:
    """An income transaction should keep its positive amount."""
    transactions = []
    transaction = {
        "date": "2026-01-28",
        "type": "기타수입",
        "category": "기타수입",
        "description": "중고 판매",
        "amount": 25000,
        "memo": "중고마켓",
    }

    add_transaction(transactions, transaction)

    assert transactions[0]["amount"] == 25000


def test_add_transaction_accepts_empty_description() -> None:
    """An empty description should be stored without errors."""
    transactions = []
    transaction = {
        "date": "2026-01-30",
        "type": "지출",
        "category": "교통",
        "description": "",
        "amount": -1500,
        "memo": "",
    }

    add_transaction(transactions, transaction)

    assert transactions[0]["description"] == ""
