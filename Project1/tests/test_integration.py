"""Finance behaviour tests using class-local pytest fixtures."""

import pytest
from src.account import SavingsAccount, EverydayAccount
from src.client import Client


class TestIntegration:

    @pytest.fixture
    def client_with_accounts(self):
        client = Client(1, "Test Client", True, "email", "test@example.com")
        savings = SavingsAccount(101, 0.05)
        everyday = EverydayAccount(102)
        client.add_account(savings)
        client.add_account(everyday)
        return client, savings, everyday

    def test_client_account_transaction_workflow(self, client_with_accounts):
        client, savings, everyday = client_with_accounts
        for account in client.accounts.values():
            assert account.deposit(500.0)
            assert account.withdraw(100.0)
            assert account.balance == 400.0
            assert [t.amount for t in account.transactions] == [500.0, 100.0]
        assert client.accounts[savings.id] is savings
        assert client.accounts[everyday.id] is everyday

    @pytest.mark.parametrize(
        "factory, expected_success", [
            (lambda: SavingsAccount(31, 0.05), True),
            (lambda: EverydayAccount(32), False),
        ], ids=["savings", "everyday"]
    )
    def test_polymorphic_withdrawal_rules(self, factory, expected_success):
        account = factory()
        assert account.deposit(1500.0)
        assert account.withdraw(1200.0) is expected_success
        assert account.balance == (300.0 if expected_success else 1500.0)
        assert len(account.transactions) == (2 if expected_success else 1)
