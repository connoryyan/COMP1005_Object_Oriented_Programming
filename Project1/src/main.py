"""
Integration tests for the banking system.

The tests demonstrate inheritance, polymorphism, Client relationships,
Transaction composition, read-only properties, and object independence.
"""

from inspect import isabstract

from .account import Account, SavingsAccount, EverydayAccount
from .branch import Branch
from .client import Client


def test_client():
    """Test Client integration with specialised Account objects."""
    print("=" * 60)
    print("Client integration")
    print("=" * 60)

    client_1 = Client(1, "Connor Yan", True, "email", "connor@example.com")
    client_2 = Client(2, "Tianyi Zhao", False, "email", "tianyi@example.com")

    client_3 = Client(3, "Third Client", True, "phone", "0400 000 003")
    account_3 = EverydayAccount(3, "Daily expenses")
    client_3.add_account(account_3)
    client_1.change_contact("updated@example.com")
    client_2.change_contact("new-contact@example.com")
    print(client_3)

    account_1 = SavingsAccount(1, 0.05)
    account_2 = EverydayAccount(2)

    branch_1 = Branch(1, "Firle Branch", "Firle", "08 8123 4567", True)

    client_1.add_account(account_1)
    client_1.add_account(account_2)
    client_2.add_account(account_1)
    client_1.set_preferred_branch(branch_1)

    print(f"Client 1: {client_1}")
    print(f"Client 1 accounts: {client_1.accounts}")
    print(f"Client 1 preferred branch: {client_1.preferred_branch}")

    assert account_1.id in client_1.accounts
    assert account_2.id in client_1.accounts
    assert account_1.id in client_2.accounts
    assert client_1.preferred_branch == branch_1

    client_1.remove_account(account_2)
    assert account_2.id not in client_1.accounts

    client_1.add_account(account_2)
    assert account_2.id in client_1.accounts

    print("[PASS] Client can store specialised Account objects.")
    print()


def test_account():
    """Test common Account behaviour through specialised accounts."""
    print("=" * 60)
    print("Account behaviour")
    print("=" * 60)

    assert isabstract(Account)
    print("Account is abstract; concrete account types are used below.")

    accounts: list[Account] = [
        SavingsAccount(1, 0.05),
        EverydayAccount(2)
    ]

    for account in accounts:
        assert account.balance == 0.0
        assert account.deposit(500.0)
        assert account.balance == 500.0

    print("[PASS] Common Account behaviour works.")
    print()


def test_savings_account():
    """Test SavingsAccount inheritance and withdrawal override."""
    print("=" * 60)
    print("SavingsAccount")
    print("=" * 60)

    account = SavingsAccount(1, 0.05)

    assert isinstance(account, Account)
    assert isinstance(account, SavingsAccount)
    assert account.interest_rate == 0.05

    account.deposit(500.0)
    assert account.balance == 500.0

    print("Valid withdrawal of $200:")
    assert account.withdraw(200.0)
    assert account.balance == 300.0

    print("Invalid withdrawal of $250:")
    assert not account.withdraw(250.0)
    assert account.balance == 300.0

    print(f"Interest rate: {account.interest_rate}")
    print(f"Minimum balance: ${SavingsAccount.MINIMUM_BALANCE}")
    print(f"Final balance: ${account.balance}")

    assert len(account.transactions) == 2

    print("[PASS] SavingsAccount withdrawal rule works.")
    print()


def test_everyday_account():
    """Test EverydayAccount inheritance and withdrawal override."""
    print("=" * 60)
    print("EverydayAccount")
    print("=" * 60)

    account = EverydayAccount(2)

    assert isinstance(account, Account)
    assert isinstance(account, EverydayAccount)

    account.deposit(1200.0)
    assert account.balance == 1200.0

    print("Valid withdrawal of $500:")
    assert account.withdraw(500.0)
    assert account.balance == 700.0

    print("Invalid withdrawal of $1200:")
    assert not account.withdraw(1200.0)
    assert account.balance == 700.0

    print(f"Maximum withdrawal: ${EverydayAccount.MAX_WITHDRAWAL}")
    print(f"Final balance: ${account.balance}")

    assert len(account.transactions) == 2

    print("[PASS] EverydayAccount withdrawal rule works.")
    print()


def test_account_polymorphism():
    """Test polymorphic withdrawal through Account references."""
    print("=" * 60)
    print("Polymorphism")
    print("=" * 60)

    accounts: list[Account] = [
        SavingsAccount(1, 0.05),
        EverydayAccount(2)
    ]

    for account in accounts:
        account.deposit(1500.0)

    print("Withdrawing $1200 from each account:")

    assert accounts[0].withdraw(1200.0)
    assert not accounts[1].withdraw(1200.0)

    assert accounts[0].balance == 300.0
    assert accounts[1].balance == 1500.0

    for account in accounts:
        print(f"{type(account).__name__}: ${account.balance}")

    print("[PASS] Polymorphic withdrawal uses specialised rules.")
    print()


def test_transactions():
    """Test Transaction creation and transaction collection protection."""
    print("=" * 60)
    print("Transaction")
    print("=" * 60)

    account = SavingsAccount(1, 0.05)

    assert len(account.transactions) == 0

    account.deposit(500.0)
    account.withdraw(100.0)

    assert len(account.transactions) == 2

    # Test transaction filtering.
    assert len(account.get_transactions_filter()) == 2

    deposits = account.get_transactions_filter(
        typ="Deposit"
    )
    assert len(deposits) == 1
    assert deposits[0].amount == 500.0

    withdrawals = account.get_transactions_filter(
        typ="Withdraw"
    )
    assert len(withdrawals) == 1
    assert withdrawals[0].amount == 100.0

    min_amount = account.get_transactions_filter(
        amount_min=100.0
    )
    assert len(min_amount) == 2

    max_amount = account.get_transactions_filter(
        amount_max=100.0
    )
    assert len(max_amount) == 1
    assert max_amount[0].amount == 100.0

    combined = account.get_transactions_filter(
        typ="Deposit",
        amount_min=500.0,
        amount_max=500.0,
    )
    assert len(combined) == 1
    assert combined[0].amount == 500.0

    unmatched = account.get_transactions_filter(
        typ="Transfer"
    )
    assert len(unmatched) == 0

    print("[PASS] Transaction filtering works.")

    print(f"Transaction count: {len(account.transactions)}")

    for transaction in account.transactions:
        print(f"  {transaction}")

    records_before = len(account.transactions)

    account.deposit(-50.0)
    account.withdraw(1000.0)
    account.withdraw(0.0)

    records_after = len(account.transactions)

    assert records_before == records_after
    print("[PASS] Failed operations create no transactions.")

    transaction_list = account.transactions
    transaction_list.clear()

    assert len(transaction_list) == 0
    assert len(account.transactions) == records_before

    print("[PASS] Transaction collection cannot be modified externally.")
    print()


def test_read_only_properties():
    """Test that Account id and balance are read-only."""
    print("=" * 60)
    print("Read-only properties")
    print("=" * 60)

    account = SavingsAccount(1, 0.05)
    account.deposit(500.0)

    print(f"Account id: {account.id}")
    print(f"Account balance: ${account.balance}")

    assert Account.id.fset is None
    assert Account.balance.fset is None
    print("[PASS] Account id and balance have read-only properties.")

    assert account.id == 1
    assert account.balance == 500.0
    print()


def test_branch():
    """Test Branch operations."""
    print("=" * 60)
    print("Branch operations")
    print("=" * 60)

    branch_1 = Branch(1, "Firle Branch", "Firle", "08 8123 4567", True)
    branch_2 = Branch(2, "Norwood Branch", "Norwood", "08 8234 5678", False)
    branch_3 = Branch(3, "Adelaide Branch", "Adelaide CBD",
                      "08 8345 6789", True)

    print(branch_1)

    assert branch_1.is_open
    assert not branch_2.is_open
    assert branch_3.is_open

    branch_1.close()
    branch_2.open()

    assert not branch_1.is_open
    assert branch_2.is_open

    branch_3.phone = "08 8999 8888"
    branch_2.name = "Norwood Central"
    branch_1.location = "Firle South"

    assert branch_3.phone == "08 8999 8888"
    assert branch_2.name == "Norwood Central"
    assert branch_1.location == "Firle South"

    print(f"Branch 1 open: {branch_1.is_open}")
    print(f"Branch 2 open: {branch_2.is_open}")
    print(f"Branch 3 phone: {branch_3.phone}")

    print("[PASS] Branch operations work.")
    print()


def test_object_independence():
    """Test that separate objects maintain independent state."""
    print("=" * 60)
    print("Object independence")
    print("=" * 60)

    client_1 = Client(
        1, "Connor Yan", True, "email", "connor@example.com"
    )
    client_2 = Client(
        2, "Tianyi Zhao", True, "email", "tianyi@example.com"
    )

    account_1 = SavingsAccount(1, 0.05)
    account_2 = EverydayAccount(2)

    account_1.deposit(500.0)
    account_2.deposit(1000.0)

    client_1.name = "Connor Yan Jr."
    account_1.deposit(50.0)

    assert client_1.name == "Connor Yan Jr."
    assert client_2.name == "Tianyi Zhao"

    assert account_1.balance == 550.0
    assert account_2.balance == 1000.0

    print(f"Client 1 name: {client_1.name}")
    print(f"Client 2 name: {client_2.name}")
    print(f"Account 1 balance: ${account_1.balance}")
    print(f"Account 2 balance: ${account_2.balance}")

    print("[PASS] Objects maintain independent state.")
    print()


def demonstrate_handled_errors():
    """Show recovery after expected errors without main-level handlers."""
    client = Client(99, "Demo", True, "email", "demo@example.com")
    account = EverydayAccount(99)
    client.add_account(account)
    retrieved = client.get_account(99)
    assert retrieved is account
    assert account.deposit(1500)
    before = (account.balance, account.transactions)
    assert not account.withdraw(1001)
    print("Handled:", type(account.last_error).__name__, account.last_error)
    assert (account.balance, account.transactions) == before
    assert not account.deposit(float("nan"))
    assert client.get_account(404) is None
    assert account.withdraw(100)
    assert account.last_error is None
    print("Continued successfully:", account)


def main():
    test_client()
    test_account()
    test_savings_account()
    test_everyday_account()
    test_account_polymorphism()
    test_transactions()
    test_read_only_properties()
    test_branch()
    test_object_independence()
    demonstrate_handled_errors()

    print("=" * 60)
    print("All tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
