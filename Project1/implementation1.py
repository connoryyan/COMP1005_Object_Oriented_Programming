

class Client:
    '''
    The information associated with each client

    Attributes:
        id (int): Client identifier
        name (str): Client name
        is_active (bool): Whether the client is active
        preferred_contact (str): Preferred contact method
        contact (str): Client contact
        account_id (str):  Identifier of client's account
    '''
    def __init__(self, id, name, is_active, preferred_contact, contact, account_id):
        '''
        Initialization

        Args:
            id (int): Client identifier
            name (str): Client name
            is_active (bool): Whether the client is active
            preferred_contact (str): Preferred contact method
            contact (str): Client contact
            account_id (str):  Identifier of client's account
        '''
        self.id = id
        self.name = name
        self.is_active = is_active
        self.preferred_contact = preferred_contact
        self.contact = contact
        self.account_id = account_id

    def display_info(self):
        '''
        Display the information associated with the client

        Args:
            None

        Returns:
            None
        '''
        print(f"Information of Client #{self.id}")
        print(f"    Name: {self.name}")
        print(f"    Active: {'Yes' if self.is_active else 'No'}")
        print(f"    Preferred contact method: {self.preferred_contact}")
        print(f"    Contact: {self.contact}")
        print(f"    Account ID: {self.account_id}")

    def change_name(self, name):
        '''
        Change client's name

        Args:
            name (str): client's new name

        Returns:
            None
        '''

    def change_preferred_contact(self, preferred_contact):
        '''
        Change Client's contact information

        Args:
            preferred_contact (str): client's new preferred contact method
        
        Returns:
            None
        '''
        self.preferred_contact = preferred_contact
        print(f"[INFO] {self.name}'s preferred contact method has been changed to {self.preferred_contact}.")

    def change_contact(self, contact):
        '''
        Change Client's contact information

        Args:
            contact (str): client's new contact information
        
        Returns:
            None
        '''
        self.contact = contact
        print(f"[INFO] {self.name}'s contact information has been changed to {self.contact}.")

    def change_is_active(self, is_active):
        '''
        Change the value of self.is_active

        Args:
            is_active (bool): if the client is active

        Returns:
            None
        '''
        self.is_active = is_active
        print(f"[INFO] {self.name}'s has been recorded as {'active' if self.is_active else 'inactive'}.")

class Account:
    '''
    The information associated with accounts and support common financial operations such as deposits, withdrawals and transfers

    Attributes:
        id (int): account identifier
        type (str): account type
        balance (float): account balance
    '''

    def __init__(self, id, typ):
        '''
        Initialization

        Args:
            id (int): account identifier
            typ (str): account type
        '''
        self.id = id
        self.type = typ
        self.balance = 0.0

    def deposit(self, amount):
        '''
        Add an amount to the account balance

        Args:
            amount (float): a positive amount of money to be deposited

        Returns:
            None
        '''

        self.balance += amount
        print("[INFO] Deposit successful.")

    def withdrawal(self, amount):
        '''
        Take an amount out of the account balance

        Args:
            amount (float): a positive amount of money to be withdrawed

        Returns:
            None
        '''

        if amount > self.balance:
            print("[INFO] Withdrawal failed. Insufficient balance.")
            return

        self.balance -= amount
        print("[INFO] Withdrawal successful.")

    def display_balance(self):
        '''
        Display account balance

        Args:
            None

        Returns:
            None
        '''
        print(f"The balance of Account {self.id} is ${self.balance}.")

if __name__ == "__main__":
    client_1 = Client(1, "Connor Yan", True, "email", "connor.yan@student.adelaide.edu.au", 1)
    client_2 = Client(2, "Tianyi Zhao", False, "email", "tianyi.zhao@student.adelaide.edu.au", 2)
    client_3 = Client(3, "Leo Messi", True, "phone", "0400 123 456", 3)
 
    account_1 = Account(1, "Savings")
    account_2 = Account(2, "Checking")
    account_3 = Account(3, "Savings")
 
    account_1.balance = 500.0
    account_2.balance = 1200.0
    account_3.balance = 0.0
 
    print("=" * 60)
    print("Client information (using dot notation to access attributes)")
    print("=" * 60)
    print(f"Client 1 name: {client_1.name}")
    print(f"Client 2 preferred contact: {client_2.preferred_contact}")
    print(f"Client 3 is_active: {client_3.is_active}")
 
    print()
    print("=" * 60)
    print("Calling client methods via dot notation")
    print("=" * 60)
    client_1.display_info()
    client_2.change_preferred_contact("phone")
    client_3.change_contact("leo.messi@example.com")
 
    print()
    print("=" * 60)
    print("Account operations")
    print("=" * 60)

 
    print(f"Account 1 balance before deposit: ${account_1.balance}")
    account_1.deposit(250.0)
    print(f"Account 1 balance after deposit: ${account_1.balance}")
 
    print()
 

    print(f"Account 2 balance before deposit: ${account_2.balance}")
    account_2.deposit(300.0)
    print(f"Account 2 balance after deposit: ${account_2.balance}")
 
    print()
 

    print(f"Account 1 balance before withdrawal: ${account_1.balance}")
    account_1.withdrawal(400.0)
    print(f"Account 1 balance after withdrawal: ${account_1.balance}")
 
    print()
 

    print(f"Account 3 balance before withdrawal: ${account_3.balance}")
    account_3.withdrawal(100.0)
    print(f"Account 3 balance after withdrawal: ${account_3.balance}")
 
    print()
 

    print(f"Account 3 balance before over-withdrawal attempt: ${account_3.balance}")
    account_3.withdrawal(9999.0)
    print(f"Account 3 balance after over-withdrawal attempt: ${account_3.balance}")
 
    print()
    print("=" * 60)
    print("Confirming object independence")
    print("=" * 60)
 

    print(f"Before change -> client_1: {client_1.name}, client_2: {client_2.name}")
    client_1.change_name("Connor Y.")
    print(f"After change  -> client_1: {client_1.name}, client_2: {client_2.name}")
 

    print(f"Before change -> account_1: ${account_1.balance}, account_2: ${account_2.balance}")
    account_1.deposit(50.0)
    print(f"After change  -> account_1: ${account_1.balance}, account_2: ${account_2.balance}")




        