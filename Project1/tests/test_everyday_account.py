"""Finance behaviour tests using class-local pytest fixtures."""

import pytest
from src.account import EverydayAccount


class TestEverydayAccount:

    @pytest.fixture
    def everyday_account(self):
        account = EverydayAccount(2)
        account.deposit(1200.0)
        return account

    def test_valid_withdrawal(self, everyday_account):
        assert everyday_account.withdraw(500.0)
        assert everyday_account.balance == 700.0
        assert len(everyday_account.transactions) == 2

    def test_maximum_withdrawal_rule(self, everyday_account):
        before = len(everyday_account.transactions)
        assert not everyday_account.withdraw(1200.0)
        assert everyday_account.balance == 1200.0
        assert len(everyday_account.transactions) == before

    def test_exact_maximum_withdrawal_boundary(self, ):
        account = EverydayAccount(22)
        maximum = EverydayAccount.MAX_WITHDRAWAL
        assert account.deposit(maximum + 100.0)
        assert account.withdraw(maximum)
        assert account.balance == 100.0
        before = len(account.transactions)
        assert not account.withdraw(maximum + 0.01)
        assert account.balance == 100.0
        assert len(account.transactions) == before

    def test_invalid_withdrawal_amounts(self, everyday_account):
        before = len(everyday_account.transactions)
        for amount in (0.0, -10.0):
            assert not everyday_account.withdraw(amount)
        assert everyday_account.balance == 1200.0
        assert len(everyday_account.transactions) == before
