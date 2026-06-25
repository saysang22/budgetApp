"""Core logic for the budget CLI app."""

from __future__ import annotations

from csv import DictReader
from collections.abc import MutableSequence
from pathlib import Path
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
    normalized_category = category.lower()
    return [
        {
            "date": transaction["date"],
            "type": transaction["type"],
            "category": transaction["category"],
            "description": transaction["description"],
            "amount": transaction["amount"],
            "memo": transaction["memo"],
        }
        for transaction in transactions
        if transaction["category"].lower() == normalized_category
    ]


def load_transactions_from_csv(path: str) -> list[dict[str, Any]]:
    """Load transactions from a CSV file."""
    csv_path = Path(path)
    with csv_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        return [
            {
                "date": row["date"],
                "type": row["type"],
                "category": row["category"],
                "description": row["description"],
                "amount": int(row["amount"]),
                "memo": row["memo"],
            }
            for row in DictReader(csv_file)
        ]


def monthly_summary(
    transactions: list[dict[str, Any]],
) -> dict[str, dict[str, int]]:
    """Summarize transactions by month."""
    pass
