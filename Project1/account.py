class Account:
    '''
    Manage the information associated with accounts and support common financial operations such as deposits, withdrawals and transfers

    Attributes:
        id (int): account identifier
        __type (str): account type
        __balance (float): account balance
    '''

    def __init__(self, id: int, typ: str):
        '''
        Initialization

        Args:
            id (int): account identifier
            typ (str): account type
        '''
        if isinstance(id, int): self.id: int = id
        if isinstance(typ, str): self.__type: str = typ
        self.__balance: float = 0.0

    def __str__(self) -> str:
        '''
        Display the information associated with the account

        Returns:
            str: A string containing the account's information.
        '''
        return f'''Account id: {self.id}, type: {self.__type}, balance: {self.__balance}'''

    def __repr__(self) -> str:
        '''
        Display the information associated with the account

        Returns:
            str: A string containing the account's information.
        '''
        return f"Account(id = {self.id}, type = {self.__type}, \
balance = {self.__balance})"

    def get_type(self) -> str:
        '''
        Type getter

        Returns:
            str: self.__type
        '''
        return self.__type

    def get_balance(self) -> float:
        '''
        Balance getter

        Returns:
            float: self.__balance
        '''
        return self.__balance

    def deposit(self, amount: float):
        '''
        Add an amount to the account __balance

        Args:
            amount (float): a positive amount of money to be deposited

        Returns:
            None
        '''
        if not isinstance(amount, float):
            print("[INFO] Deposit failed. Invalid amount.")
            return

        self.__balance += amount
        print("[INFO] Deposit successful.")

    def withdrawal(self, amount: float):
        '''
        Take an amount out of the account balance

        Args:
            amount (float): a positive amount of money to be withdrawed

        Returns:
            None
        '''

        if not isinstance(amount, float):
            print("[INFO] Deposit failed. Invalid amount.")
            return

        if amount > self.__balance:
            print("[INFO] Withdrawal failed. Insufficient balance.")
            return False  # can_afford()

        self.__balance -= amount
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
        print(f"The balance of Account {self.id} is ${self.__balance}.")
