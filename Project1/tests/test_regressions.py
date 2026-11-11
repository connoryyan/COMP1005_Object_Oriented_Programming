"""Business failures, state transitions and end-to-end regressions."""

import pytest

from src.account import Account, EverydayAccount, SavingsAccount
from src.branch import Branch
from src.client import Client
from src.exceptions import (
    InsufficientFundsError, InvalidAmountError, MinimumBalanceError,
    WithdrawalLimitError,
)
from src.transaction import Transaction
from src.main import main


@pytest.fixture(params=[EverydayAccount, lambda i: SavingsAccount(i, 0.05)])
def account(request):
    result = request.param(1)
    result.deposit(500)
    return result


@pytest.mark.parametrize("amount", [
    None, "100", True, False, 0, -1, float("nan"),
    float("inf"), -float("inf"), [], {},
])
def test_invalid_money_is_atomic(account, amount):
    before = (account.balance, account.transactions)
    assert not account.deposit(amount)
    assert isinstance(account.last_error, InvalidAmountError)
    assert not account.withdraw(amount)
    assert isinstance(account.last_error, InvalidAmountError)
    assert (account.balance, account.transactions) == before


def test_overflow_deposit_is_atomic(account):
    before = (account.balance, account.transactions)
    assert not account.deposit(10 ** 1000)
    assert (account.balance, account.transactions) == before
    assert account.deposit(1e308)
    before = (account.balance, account.transactions)
    assert not account.deposit(1e308)
    assert (account.balance, account.transactions) == before


def test_specialised_errors_and_recovery():
    savings = SavingsAccount(1, 0.05)
    savings.deposit(500)
    assert not savings.withdraw(501)
    assert isinstance(savings.last_error, InsufficientFundsError)
    assert not savings.withdraw(401)
    assert isinstance(savings.last_error, MinimumBalanceError)
    assert savings.withdraw(400)
    assert savings.last_error is None
    everyday = EverydayAccount(2)
    everyday.deposit(2000)
    assert not everyday.withdraw(1001)
    assert isinstance(everyday.last_error, WithdrawalLimitError)
    assert everyday.withdraw(1000)
    assert everyday.last_error is None


@pytest.mark.parametrize("bounds", [
    {"amount_min": "1"}, {"amount_max": True},
    {"amount_min": float("nan")},
    {"amount_min": 10, "amount_max": 1},
])
def test_invalid_filters_preserve_history(account, bounds):
    history = account.transactions
    assert account.get_transactions_filter(**bounds) == []
    assert isinstance(account.last_error, InvalidAmountError)
    assert account.transactions == history


def test_recorded_transactions_are_completed(account):
    assert account.withdraw(100)
    assert [t.status for t in account.transactions] == [
        "Processed", "Processed"]
    assert [t.resulting_balance for t in account.transactions] == [500, 400]
    assert len(account.get_transactions_filter(status="Processed")) == 2
    assert account.get_transactions_filter(status="Pending") == []
    assert not account.transactions[0].cancel()
    assert account.transactions[0].status == "Processed"
    assert account.type == type(account).__name__
    assert account.type in str(account)
    assert account.type in repr(account)


def test_transaction_state_machine():
    processed = Transaction(1, "Deposit", 10)
    assert processed.process()
    assert not processed.process()
    assert not processed.cancel()
    cancelled = Transaction(2, "Withdraw", 5)
    assert cancelled.cancel()
    assert not cancelled.cancel()
    assert not cancelled.process()
    assert processed.status == "Processed"
    assert cancelled.status == "Cancelled"
    processed.description = "Updated description"
    processed.description = None
    assert "Updated description" in str(processed)
    assert "Processed" in repr(processed)
    invalid = Transaction(True, None, True, None, True, "Unknown")
    assert invalid.status == "Pending"
    assert invalid.amount is None
    assert invalid.resulting_balance is None
    assert "Pending" in str(invalid)


def test_client_collection_and_missing_accounts(capsys):
    client = Client(1, "Test", True, "email", "test@example.com")
    savings = SavingsAccount(10, .05)
    client.add_account(savings)
    client.add_account(EverydayAccount(10))
    client.add_account(None)
    client.add_account(EverydayAccount(None))
    assert client.get_account(10) is savings
    external = client.accounts
    external.clear()
    assert client.get_account(10) is savings
    for number in (99, None, True, [], "10"):
        assert client.get_account(number) is None
        client.remove_account_number(number)
    assert "not found" in capsys.readouterr().out
    client.remove_account(None)
    client.remove_account_number(10)
    assert client.accounts == {}


def test_client_changes_preserve_valid_state():
    client = Client(1, "Test", True, "email", "old@example.com")
    client.change_contact("new@example.com")
    client.change_preferred_contact("phone")
    client.change_is_active(False)
    client.name = "New name"
    client.change_contact(None)
    client.change_preferred_contact(None)
    client.change_is_active(1)
    client.name = None
    client.set_preferred_branch(None)
    expected = ("New name", "new@example.com", "phone", False)
    assert (client.name, client.contact, client.preferred_contact,
            client.is_active) == expected
    assert "New name" in str(client)
    assert "New name" in repr(client)
    invalid = Client(True, None, None, None, None)
    assert invalid.id is None
    assert not invalid.is_active


def test_branch_updates_and_validation():
    branch = Branch(1, "City", "CBD", "123")
    branch.name = "Central"
    branch.location = "North"
    branch.phone = "456"
    branch.name = None
    branch.location = None
    branch.phone = None
    assert (branch.name, branch.location, branch.phone) == (
        "Central", "North", "456")
    branch.open()
    assert "Open" in str(branch)
    branch.close()
    assert "Closed" in str(branch)
    assert "Central" in repr(branch)
    invalid = Branch(True, None, None, None, None)
    assert invalid.id is None
    assert not invalid.is_open


def test_abstract_account_and_invalid_initial_values():
    with pytest.raises(TypeError):
        Account(1)
    account = SavingsAccount(True, float("nan"), name=None)
    assert account.id is None
    assert account.interest_rate == 0
    assert account.name == "Account"


def test_finance_demonstration():
    main()


def test_filter_maximum_and_direct_transaction_data(account):
    assert account.get_transactions_filter(amount_max=1) == []
    transaction = Transaction(7, "Deposit", 20, "Initial")
    assert transaction.id == 7
    assert transaction.description == "Initial"
    assert not account.withdraw(10 ** 1000)
    assert account.balance == 500


def test_display_balance_uses_current_state(account, capsys):
    assert account.withdraw(100)
    account.display_balance()
    assert "$400.00" in capsys.readouterr().out
