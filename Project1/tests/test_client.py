"""Finance behaviour tests using class-local pytest fixtures."""

import pytest
from src.account import SavingsAccount, EverydayAccount
from src.client import Client
from src.branch import Branch


class TestClient:

    @pytest.fixture
    def client_with_accounts(self):
        client = Client(1, "Test Client", True, "email", "test@example.com")
        savings = SavingsAccount(101, 0.05)
        everyday = EverydayAccount(102)
        client.add_account(savings)
        client.add_account(everyday)
        return client, savings, everyday

    @pytest.fixture
    def branch(self):
        return Branch(1, "Firle Branch", "Firle", "08 8123 4567", True)

    def test_add_and_retrieve_multiple_accounts(self, client_with_accounts):
        client, savings, everyday = client_with_accounts
        accounts = client.accounts
        assert set(accounts) == {savings.id, everyday.id}
        assert accounts[savings.id] is savings
        assert accounts[everyday.id] is everyday

    def test_remove_and_readd_account(self, client_with_accounts):
        client, savings, everyday = client_with_accounts
        client.remove_account(everyday)
        assert everyday.id not in client.accounts
        assert savings.id in client.accounts
        client.add_account(everyday)
        assert client.accounts[everyday.id] is everyday

    def test_same_account_can_be_attached_to_different_clients(
            self, client_with_accounts
    ):
        from src.client import Client
        client, savings, _ = client_with_accounts
        other = Client(2, "Other Client", False, "email", "other@example.com")
        other.add_account(savings)
        assert other.accounts[savings.id] is savings
        assert client.accounts[savings.id] is savings

    def test_preferred_branch(self, client_with_accounts, branch):
        client, _, _ = client_with_accounts
        client.set_preferred_branch(branch)
        assert client.preferred_branch is branch

    def test_retrieved_account_is_live_object(self, client_with_accounts):
        client, savings, _ = client_with_accounts
        retrieved = client.accounts[savings.id]
        assert retrieved.deposit(100.0)
        assert savings.balance == 100.0
        assert len(client.accounts[savings.id].transactions) == 1

    def test_distinct_clients_have_independent_account_collections(
            self, client_with_accounts
    ):
        from src.client import Client
        client, _, _ = client_with_accounts
        other = Client(3, "Third Client", True, "email", "third@example.com")
        assert other.accounts == {}
        other.add_account(SavingsAccount(103, 0.05))
        assert 103 not in client.accounts
