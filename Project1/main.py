"""
Integration tests for the banking system.

The tests demonstrate inheritance, polymorphism, Client relationships,
Transaction composition, read-only properties, and object independence.
"""

from account import Account, SavingsAccount, EverydayAccount
from branch import Branch
from client import Client


def test_client():
    """Test Client integration with specialised Account objects."""
    print("=" * 60)
    print("Client integration")
    print("=" * 60)

    client_1 = Client(1, "Connor Yan", True, "email", "connor@example.com")
    client_2 = Client(2, "Tianyi Zhao", False, "email", "tianyi@example.com")

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

    assert account_1 in client_1.accounts
    assert account_2 in client_1.accounts
    assert account_1 in client_2.accounts
    assert client_1.preferred_branch == branch_1

    client_1.remove_account(account_2)
    assert account_2 not in client_1.accounts

    client_1.add_account(account_2)
    assert account_2 in client_1.accounts

    print("[PASS] Client can store specialised Account objects.")
    print()


def test_account():
    """Test common Account behaviour inherited by subclasses."""
    print("=" * 60)
    print("Account behaviour")
    print("=" * 60)

    account = Account(1)

    assert account.id == 1
    assert account.balance == 0.0

    assert account.deposit(500.0)
    assert account.balance == 500.0

    assert account.withdraw(200.0)
    assert account.balance == 300.0

    assert not account.deposit(-50.0)
    assert not account.withdraw(500.0)
    assert account.balance == 300.0

    print(f"Account id: {account.id}")
    print(f"Account balance: ${account.balance}")
    print(f"Transactions: {len(account.transactions)}")

    assert len(account.transactions) == 2

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


def test_polymorphism():
    """Test polymorphism through the Account parent type."""
    print("=" * 60)
    print("Polymorphism")
    print("=" * 60)

    accounts: list[Account] = [
        SavingsAccount(1, 0.05),
        EverydayAccount(2),
        SavingsAccount(3, 0.03)
    ]

    for account in accounts:
        account.deposit(1000.0)
        print(f"{type(account).__name__}: ${account.balance}")

    assert all(isinstance(account, Account) for account in accounts)
    assert isinstance(accounts[0], SavingsAccount)
    assert isinstance(accounts[1], EverydayAccount)
    assert isinstance(accounts[2], SavingsAccount)

    print("[PASS] Different subclasses work through Account references.")
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

    account = Account(1)
    account.deposit(500.0)

    print(f"Account id: {account.id}")
    print(f"Account balance: ${account.balance}")

    try:
        account.id = 99
        assert False
    except AttributeError:
        print("[PASS] Account id is read-only.")

    try:
        account.balance = 9999.0
        assert False
    except AttributeError:
        print("[PASS] Account balance is read-only.")

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


def main():
    test_client()
    test_account()
    test_savings_account()
    test_everyday_account()
    test_polymorphism()
    test_transactions()
    test_read_only_properties()
    test_branch()
    test_object_independence()

    print("=" * 60)
    print("All tests passed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
