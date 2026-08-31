'''
Integration test for the banking system.

This module creates several objects of each class with different attribute
values and exercises every method to prove that the objects interact with one
another as expected.
'''

from account import Account
from branch import Branch
from client import Client
from transaction import Transaction

if __name__ == "__main__":
    # --- Instantiate three objects of each class with different values. ---
    client_1 = Client(1, "Connor Yan", True, "email",
                      "connor.yan@student.adelaide.edu.au")
    client_2 = Client(2, "Tianyi Zhao", False, "email",
                      "tianyi.zhao@student.adelaide.edu.au")
    client_3 = Client(3, "Leo Messi", True, "phone", "0400 123 456")

    account_1 = Account(1, "Savings")
    account_2 = Account(2, "Checking")
    account_3 = Account(3, "Savings")

    branch_1 = Branch(1, "Firle Branch", "Firle", "08 8123 4567", True)
    branch_2 = Branch(2, "Norwood Branch", "Norwood", "08 8234 5678", False)
    branch_3 = Branch(3, "Adelaide Branch", "Adelaide CBD", "08 8345 6789",
                      True)

    # --- Link the objects together. ---
    client_1.add_account(account_1)
    client_1.add_account(account_2)
    client_2.add_account(account_3)
    client_1.set_preferred_branch(branch_1)
    client_2.set_preferred_branch(branch_2)

    print("=" * 60)
    print("Client getters")
    print("=" * 60)
    print(f"Client 1 name: {client_1.get_name()}")
    print(f"Client 2 preferred contact: {client_2.get_preferred_contact()}")
    print(f"Client 2 contact: {client_2.get_contact()}")
    print(f"Client 3 is_active: {client_3.get_is_active()}")
    print(f"Client 1 accounts: {client_1.get_accounts()}")
    print(f"Client 1 preferred branch: {client_1.get_preferred_branch()}")

    print()
    print("=" * 60)
    print("Client setters")
    print("=" * 60)
    print(client_1)
    client_2.change_preferred_contact("phone")
    client_3.change_contact("leo.messi@example.com")
    client_2.change_is_active(True)

    print()
    print("=" * 60)
    print("Client account management (add / remove / list)")
    print("=" * 60)
    client_1.remove_account(account_2)
    print(f"Client 1 accounts after removing account 2: "
          f"{client_1.get_accounts()}")
    client_1.add_account(account_2)
    print(f"Client 1 accounts after re-adding account 2: "
          f"{client_1.get_accounts()}")
    client_1.set_preferred_branch(branch_2)
    print(f"Client 1 preferred branch after change: "
          f"{client_1.get_preferred_branch()}")

    print()
    print("=" * 60)
    print("Account operations (deposit, withdrawal, getters, display)")
    print("=" * 60)
    account_1.deposit(500.0)
    account_2.deposit(1200.0)
    print(f"Account 1 type: {account_1.get_type()}")
    print(f"Account 1 balance after deposit: ${account_1.get_balance()}")
    account_1.display_balance()
    account_1.withdrawal(200.0)
    print(f"Account 1 balance after withdrawal: ${account_1.get_balance()}")
    # An invalid (negative) amount must be rejected without changing balance.
    account_1.deposit(-50.0)
    # A withdrawal larger than the balance must be rejected.
    account_3.withdrawal(100.0)
    print(f"Account 3 balance after failed withdrawal: "
          f"${account_3.get_balance()}")

    print()
    print("=" * 60)
    print("Transaction operations (process, cancel, description, getters)")
    print("=" * 60)
    # A deposit transaction moves money into a single account.
    transaction_1 = Transaction(1, "Deposit", 200.0, "Initial deposit")
    print(transaction_1)
    print(f"Transaction 1 type: {transaction_1.get_type()}, "
          f"amount: ${transaction_1.get_amount()}")
    transaction_1.process(destination=account_1)
    print(f"Account 1 balance after deposit transaction: "
          f"${account_1.get_balance()}")

    # A withdrawal transaction is cancelled before it can be processed.
    transaction_2 = Transaction(2, "Withdrawal", 150.0, "ATM withdrawal")
    transaction_2.cancel()
    transaction_2.process(source=account_2)
    print(f"Transaction 2 status: {transaction_2.get_status()}")
    print(f"Account 2 balance (unchanged): ${account_2.get_balance()}")

    # A transfer transaction moves money between two accounts.
    transaction_3 = Transaction(3, "Transfer", 250.0, "Transfer to savings")
    transaction_3.set_description("Transfer to savings account")
    print(f"Transaction 3 description: {transaction_3.get_description()}")
    transaction_3.process(source=account_2, destination=account_1)
    print(f"Account 1 balance after transfer: ${account_1.get_balance()}")
    print(f"Account 2 balance after transfer: ${account_2.get_balance()}")
    print(f"Transaction 3 status: {transaction_3.get_status()}")

    print()
    print("=" * 60)
    print("Branch operations (open, close, getters, setters)")
    print("=" * 60)
    print(branch_1)
    branch_1.close()
    branch_2.open()
    branch_3.set_phone("08 8999 8888")
    branch_2.set_name("Norwood Central")
    branch_1.set_location("Firle South")
    print(f"Branch 1 state: {branch_1.get_is_open()}")
    print(f"Branch 1 name/location: {branch_1.get_name()}, "
          f"{branch_1.get_location()}")
    print(f"Branch 2 name: {branch_2.get_name()}")
    print(f"Branch 2 state: {branch_2.get_is_open()}")
    print(f"Branch 3 phone: {branch_3.get_phone()}")
    print(branch_1)

    print()
    print("=" * 60)
    print("Confirming object independence")
    print("=" * 60)
    print(f"Before change -> client 1: {client_1.get_name()}, "
          f"client 2: {client_2.get_name()}")
    client_1.set_name("Connor Yan Jr.")
    print(f"After change  -> client 1: {client_1.get_name()}, "
          f"client 2: {client_2.get_name()}")

    print(f"Before change -> account 1: ${account_1.get_balance()}, "
          f"account 2: ${account_2.get_balance()}")
    account_1.deposit(50.0)
    print(f"After change  -> account 1: ${account_1.get_balance()}, "
          f"account 2: ${account_2.get_balance()}")
