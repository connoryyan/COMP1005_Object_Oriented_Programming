"""Finance behaviour tests using class-local pytest fixtures."""

import pytest
from src.account import SavingsAccount


class TestTransaction:

    @pytest.fixture
    def savings_account(self):
        account = SavingsAccount(1, 0.05)
        account.deposit(500.0)
        return account

    @pytest.fixture
    def account_with_history(self, savings_account):
        savings_account.withdraw(100.0)
        return savings_account

    def test_successful_operations_record_transactions_in_order(
            self, account_with_history
    ):
        history = account_with_history.transactions
        assert len(history) == 2
        assert [t.amount for t in history] == [500.0, 100.0]

    def test_transaction_filter_by_type(self, account_with_history):
        deposits = account_with_history.get_transactions_filter(typ="Deposit")
        withdrawals = account_with_history.get_transactions_filter(
            typ="Withdraw")
        assert [t.amount for t in deposits] == [500.0]
        assert [t.amount for t in withdrawals] == [100.0]
        assert account_with_history.get_transactions_filter(
            typ="Transfer") == []

    def test_transaction_filter_by_amount(self, account_with_history):
        account = account_with_history
        above = account.get_transactions_filter(amount_min=100)
        below = account.get_transactions_filter(amount_max=100)
        assert [t.amount for t in above] == [500, 100]
        assert [t.amount for t in below] == [100]
        assert [t.amount for t in account.get_transactions_filter(
            typ="Deposit", amount_min=500, amount_max=500
        )] == [500]

    def test_failed_operations_do_not_create_transactions(
            self, account_with_history
    ):
        before = list(account_with_history.transactions)
        assert not account_with_history.deposit(-50.0)
        assert not account_with_history.withdraw(1000.0)
        assert not account_with_history.withdraw(0.0)
        assert account_with_history.transactions == before
        assert account_with_history.balance == 400.0
