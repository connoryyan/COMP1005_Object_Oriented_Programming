"""Finance behaviour tests using class-local pytest fixtures."""

import pytest
from src.account import SavingsAccount


class TestSavingsAccount:

    @pytest.fixture
    def savings_account(self):
        account = SavingsAccount(1, 0.05)
        account.deposit(500.0)
        return account

    def test_valid_withdrawal(self, savings_account):
        assert savings_account.withdraw(200.0)
        assert savings_account.balance == 300.0
        assert len(savings_account.transactions) == 2

    def test_minimum_balance_is_enforced(self, savings_account):
        before = len(savings_account.transactions)
        # The supplied integration script establishes that this must fail after
        # a balance of 500. The exact minimum is defined by the implementation.
        assert not savings_account.withdraw(450.0)
        assert savings_account.balance == 500.0
        assert len(savings_account.transactions) == before

    def test_exact_minimum_balance_boundary(self, ):
        account = SavingsAccount(10, 0.05)
        minimum = SavingsAccount.MINIMUM_BALANCE
        assert account.deposit(minimum + 200.0)
        assert account.withdraw(200.0)
        assert account.balance == minimum
        assert not account.withdraw(0.01)
        assert account.balance == minimum

    def test_invalid_withdrawal_amounts(self, savings_account):
        before = len(savings_account.transactions)
        for amount in (0.0, -10.0):
            assert not savings_account.withdraw(amount)
        assert savings_account.balance == 500.0
        assert len(savings_account.transactions) == before
