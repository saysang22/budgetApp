"""Tests for budget.core."""

from csv import DictReader
from pathlib import Path

from budget.core import (
    add_transaction,
    filter_by_category,
    get_balance,
    load_transactions_from_csv,
    monthly_summary,
)


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


def test_get_balance_returns_zero_for_empty_list() -> None:
    """An empty collection should have a zero balance."""
    assert get_balance([]) == 0.0


def test_get_balance_uses_sample_csv_amounts() -> None:
    """Balance should match the total amount from step2 sample data."""
    csv_path = Path("data/step2_transactions.csv")
    with csv_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        transactions = [
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

    assert get_balance(transactions) == 24285027.0


def test_filter_by_category_matches_case_insensitively() -> None:
    """Category matching should ignore case differences."""
    transactions = [
        {
            "date": "2026-01-13",
            "type": "지출",
            "category": "쇼핑",
            "description": "생활용품",
            "amount": -326526,
            "memo": "",
        },
        {
            "date": "2026-02-05",
            "type": "지출",
            "category": "쇼핑",
            "description": "옷 구입",
            "amount": -63587,
            "memo": "메모_5",
        },
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "의료",
            "description": "한의원",
            "amount": -65990,
            "memo": "카드결제",
        },
    ]

    filtered = filter_by_category(transactions, "쇼핑")

    assert len(filtered) == 2
    assert all(transaction["category"] == "쇼핑" for transaction in filtered)


def test_filter_by_category_returns_empty_list_for_missing_category() -> None:
    """Unknown categories should return an empty list."""
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "의료",
            "description": "한의원",
            "amount": -65990,
            "memo": "카드결제",
        }
    ]

    assert filter_by_category(transactions, "없는카테고리") == []


def test_filter_by_category_returns_independent_results() -> None:
    """The result should not be tied to the original list object."""
    transactions = [
        {
            "date": "2026-01-13",
            "type": "지출",
            "category": "쇼핑",
            "description": "생활용품",
            "amount": -326526,
            "memo": "",
        },
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "의료",
            "description": "한의원",
            "amount": -65990,
            "memo": "카드결제",
        },
    ]

    filtered = filter_by_category(transactions, "쇼핑")
    filtered[0]["description"] = "수정됨"

    assert transactions[0]["description"] == "생활용품"


def test_load_transactions_from_csv_reads_step1_sample() -> None:
    """CSV loading should parse step1 sample data correctly."""
    csv_path = "data/step1_transactions.csv"

    transactions = load_transactions_from_csv(csv_path)

    assert len(transactions) == 10
    assert transactions[0] == {
        "date": "2026-01-05",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }
    assert isinstance(transactions[0]["amount"], int)


def test_monthly_summary_groups_step3_sample_by_month() -> None:
    """Monthly summary should aggregate step3 sample data correctly."""
    transactions = load_transactions_from_csv("data/step3_transactions.csv")

    summary = monthly_summary(transactions)

    assert len(summary) == 15
    assert summary["2025-01"] == {
        "income": 405037,
        "expense": -2886860,
        "net": -2481823,
    }
    assert summary["2025-02"] == {
        "income": 12940804,
        "expense": -1832242,
        "net": 11108562,
    }
    assert summary["2026-03"] == {
        "income": 489857,
        "expense": -3301374,
        "net": -2811517,
    }
