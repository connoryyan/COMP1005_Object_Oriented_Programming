class Account:
    '''
    Models a single bank account and supports the core financial operations of
    depositing and withdrawing money.

    The only public attribute is id. The account type and balance are
    private and are accessed through getter and setter methods.

    Attributes:
        id (int): The account's unique identifier.
        __type (str): The type of the account (for example, Savings or
            Checking).
        __balance (float): The account's current balance in dollars.
    '''

    def __init__(self, id: int, account_type: str):
        '''
        Initialise a new account with a zero balance.

        Args:
            id (int): The account's unique identifier.
            account_type (str): The type of the account.
        '''

        if not isinstance(id, int) or isinstance(id, bool):
            id = None
        if not isinstance(account_type, str):
            account_type = None

        self.id: int | None = id
        self.__type: str | None = account_type
        self.__balance: float = 0.0

    def __str__(self) -> str:
        '''
        Return a readable description of the account.

        Returns:
            str: A string containing the account's information.
        '''
        return (f"Account id: {self.id}, type: {self.__type}, "
                f"balance: {self.__balance}")

    def __repr__(self) -> str:
        '''
        Return an unambiguous string representation of the account.

        Returns:
            str: A string that reconstructs the account's state.
        '''
        return (f"Account(id={self.id}, type={self.__type}, "
                f"balance={self.__balance})")

    def get_type(self) -> str:
        '''
        Return the type of the account.

        Returns:
            str: The account type.
        '''
        return self.__type

    def get_balance(self) -> float:
        '''
        Return the current balance of the account.

        Returns:
            float: The account balance.
        '''
        return self.__balance

    def deposit(self, amount: float) -> bool:
        '''
        Add a positive amount of money to the account balance.

        Args:
            amount (float): A positive amount of money to deposit.

        Returns:
            bool: True if the deposit succeeded, False otherwise.
        '''
        if (isinstance(amount, bool)
                # Avoid boolean values to be accepted as integers.
                or not isinstance(amount, (int, float))
                or amount <= 0):
            print("[INFO] Deposit failed. Invalid amount.")
            return False

        self.__balance += amount
        print("[INFO] Deposit successful.")
        return True

    def withdrawal(self, amount: float) -> bool:
        '''
        Take a positive amount of money out of the account balance.

        Args:
            amount (float): A positive amount of money to withdraw.

        Returns:
            bool: True if the withdrawal succeeded, False otherwise.
        '''
        if (isinstance(amount, bool)
                # Avoid boolean values to be accepted as integers.
                or not isinstance(amount, (int, float))
                or amount <= 0):
            print("[INFO] Withdrawal failed. Invalid amount.")
            return False

        if amount > self.__balance:
            print("[INFO] Withdrawal failed. Insufficient balance.")
            return False

        self.__balance -= amount
        print("[INFO] Withdrawal successful.")
        return True

    def display_balance(self) -> None:
        '''
        Print the account balance to the console.

        Returns:
            None
        '''
        print(f"The balance of Account {self.id} is ${self.__balance}.")
