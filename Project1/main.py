from client import Client
from account import Account
from transaction import Transaction
from branch import Branch

if __name__ == "__main__":
    client_1 = Client(1, "Connor Yan", True, "email",
                      "connor.yan@student.adelaide.edu.au")
    client_2 = Client(2, "Tianyi Zhao", False, "email",
                      "tianyi.zhao@student.adelaide.edu.au")
    client_3 = Client(3, "Leo Messi", True, "phone", "0400 123 456")

    account_1 = Account(1, "Savings")
    account_2 = Account(2, "Checking")
    account_3 = Account(3, "Savings")

    account_1.deposit(500.0)
    account_2.deposit(1200.0)

    print("=" * 60)
    print("Client information (using dot notation to access attributes)")
    print("=" * 60)
    print(f"Client 1 name: {client_1.name}")
    print(f"Client 2 preferred contact: {client_2.get_preferred_contact()}")
    print(f"Client 3 is_active: {client_3.get_is_active()}")

    print()
    print("=" * 60)
    print("Calling client methods via dot notation")
    print("=" * 60)
    print(client_1)
    client_2.change_preferred_contact("phone")
    client_3.change_contact("leo.messi@example.com")

    print()
    print("=" * 60)
    print("Account operations")
    print("=" * 60)

    print(f"Account 1 balance before deposit: ${account_1.get_balance()}")
    account_1.deposit(250.0)
    print(f"Account 1 balance after deposit: ${account_1.get_balance()}")

    print()

    print(f"Account 2 balance before deposit: ${account_2.get_balance()}")
    account_2.deposit(300.0)
    print(f"Account 2 balance after deposit: ${account_2.get_balance()}")

    print()

    print(f"Account 1 balance before withdrawal: ${account_1.get_balance()}")
    account_1.withdrawal(400.0)
    print(f"Account 1 balance after withdrawal: ${account_1.get_balance()}")

    print()

    print(f"Account 3 balance before withdrawal: ${account_3.get_balance()}")
    account_3.withdrawal(100.0)
    print(f"Account 3 balance after withdrawal: ${account_3.get_balance()}")

    print()

    print(
        f"Account 3 balance before over-withdrawal attempt: ${account_3.get_balance()}")
    account_3.withdrawal(9999.0)
    print(
        f"Account 3 balance after over-withdrawal attempt: ${account_3.get_balance()}")

    print()
    print("=" * 60)
    print("Confirming object independence")
    print("=" * 60)

    print(
        f"Before change -> client_1: {client_1.name}, client_2: {client_2.name}")
    client_1.set_name("Connor Y.")
    print(
        f"After change  -> client_1: {client_1.name}, client_2: {client_2.name}")

    print(
        f"Before change -> account_1: ${account_1.get_balance()}, account_2: ${account_2.get_balance()}")
    account_1.deposit(50.0)
    print(
        f"After change  -> account_1: ${account_1.get_balance()}, account_2: ${account_2.get_balance()}")

    transaction_1 = Transaction(1, "Deposit", 500.0, "Initial deposit")
    transaction_2 = Transaction(2, "Withdrawal", 150.0, "ATM withdrawal")
    transaction_3 = Transaction(
        3, "Transfer", 250.0, "Transfer to another account")

    print("Initial transactions:")
    print(transaction_1)
    print()
    print(transaction_2)
    print()
    print(transaction_3)

    # Process transaction 1
    transaction_1.process()
    # Cancel transaction 2
    transaction_2.cancel()
    # Update transaction 3 description
    transaction_3.set_description("Transfer to savings account")

    # Process transaction 3
    transaction_3.process()

    print("\nTransactions after operations:")
    print(transaction_1)
    print()
    print(transaction_2)
    print()
    print(transaction_3)

    print("Before changing Transaction 1:")
    print(f"Transaction 1 status: {transaction_1.get_status()}")
    print(f"Transaction 2 status: {transaction_2.get_status()}")

    transaction_1.set_description("Updated deposit description")

    print("\nAfter changing Transaction 1:")
    print(f"Transaction 1 description: {transaction_1.get_description()}")
    print(f"Transaction 2 description: {transaction_2.get_description()}")

    branch_1 = Branch(1, "Firle Branch", "Firle", "08 8123 4567", True)
    branch_2 = Branch(2, "Norwood Branch", "Norwood", "08 8234 5678", False)
    branch_3 = Branch(3, "Adelaide Branch",
                      "Adelaide CBD", "08 8345 6789", True)

    print("Initial branches:")
    print(branch_1)
    print()
    print(branch_2)
    print()
    print(branch_3)

    branch_2.open()
    branch_1.close()
    branch_3.set_phone("08 8999 8888")

    print("\nBranches after operations:")
    print(branch_1)
    print()
    print(branch_2)
    print()
    print(branch_3)

    print("Before changing Branch 2:")
    print(f"Branch 1 state: {'Open' if branch_1.is_open else 'Closed'}")
    print(f"Branch 2 state: {'Open' if branch_2.is_open else 'Closed'}")

    branch_2.close()

    print("\nAfter closing Branch 2:")
    print(f"Branch 1 state: {'Open' if branch_1.is_open else 'Closed'}")
    print(f"Branch 2 state: {'Open' if branch_2.is_open else 'Closed'}")
