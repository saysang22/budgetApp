"""Core logic for the budget CLI app."""

from __future__ import annotations

from collections.abc import MutableSequence
from typing import Any


def add_transaction(
    transactions: MutableSequence[dict[str, Any]],
    transaction: dict[str, Any],
) -> None:
    """Add a transaction to the collection.

    The stored transaction keeps the expected budget fields only.
    """
    transactions.append(
        {
            "date": transaction["date"],
            "type": transaction["type"],
            "category": transaction["category"],
            "description": transaction["description"],
            "amount": transaction["amount"],
            "memo": transaction["memo"],
        }
    )


def get_balance(transactions: list[dict[str, Any]]) -> float:
    """Return the net balance for all transactions."""
    return float(sum(transaction["amount"] for transaction in transactions))


def filter_by_category(
    transactions: list[dict[str, Any]],
    category: str,
) -> list[dict[str, Any]]:
    """Return transactions that match the given category."""
    pass


def load_transactions_from_csv(path: str) -> list[dict[str, Any]]:
    """Load transactions from a CSV file."""
    pass


def monthly_summary(
    transactions: list[dict[str, Any]],
) -> dict[str, dict[str, int]]:
    """Summarize transactions by month."""
    pass
