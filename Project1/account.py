class Account:
    '''
    The information associated with accounts and support common financial operations such as deposits, withdrawals and transfers

    Attributes:
        id (int): account identifier
        type (str): account type
        balance (float): account balance
    '''

    def __init__(self, id:int, typ:str):
        '''
        Initialization

        Args:
            id (int): account identifier
            typ (str): account type
        '''
        self.id = id
        self.type = typ
        self.balance = 0.0

    def __str__(self) -> str:
        '''
        Display the information associated with the account

        Returns:
            str: A string containing the account's information.
        '''
        return f'''Information of Account #{self.id}
    Type: {self.type}
    Balance: {self.balance}'''

    def deposit(self, amount:float):
        '''
        Add an amount to the account balance

        Args:
            amount (float): a positive amount of money to be deposited

        Returns:
            None
        '''

        self.balance += amount
        print("[INFO] Deposit successful.")

    def withdrawal(self, amount:float):
        '''
        Take an amount out of the account balance

        Args:
            amount (float): a positive amount of money to be withdrawed

        Returns:
            None
        '''

        if amount > self.balance:
            print("[INFO] Withdrawal failed. Insufficient balance.")
            return False

        self.balance -= amount
        print("[INFO] Withdrawal successful.")
        return True

    def display_balance(self):
        '''
        Display account balance

        Args:
            None

        Returns:
            None
        '''
        print(f"The balance of Account {self.id} is ${self.balance}.")




        