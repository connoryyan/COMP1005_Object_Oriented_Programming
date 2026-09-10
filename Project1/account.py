from transaction import Transaction


class Account:
    '''
    Models a single bank account and supports the core financial operations of
    depositing and withdrawing money. Every successful deposit or withdraw
    creates a Transaction record.

    Attributes:
        __id (int): The account's unique identifier.
        _balance (float): The account's current balance in dollars.
        __transactions (list[Transaction]): Transaction records created by
            this account.
    '''

    def __init__(self, id: int):
        '''
        Initialise a new account with a zero balance and no records.

        Args:
            id (int): The account's unique identifier.
        '''
        if not isinstance(id, int) or isinstance(id, bool):
            id = None

        self.__id: int | None = id
        self._balance: float = 0.0
        self.__transactions: list[Transaction] = []

    def __str__(self) -> str:
        '''
        Return a readable description of the account.

        Returns:
            str: A string containing the account's information.
        '''
        return (f"Account id: {self.__id}, "
                f"balance: {self._balance}")

    def __repr__(self) -> str:
        '''
        Return an unambiguous string representation of the account.

        Returns:
            str: A string that reconstructs the account's state.
        '''
        return (f"Account(id={self.__id}, "
                f"balance={self._balance})")

    def get_id(self) -> int | None:
        '''
        Return the identifier of the account.

        Returns:
            int: The account identifier.
        '''
        return self.__id

    id = property(get_id)

    def get_type(self) -> str | None:
        '''
        Return the type of the account.

        Returns:
            str: The account type.
        '''
        return self.__type

    type = property(get_type)

    def get_balance(self) -> float:
        '''
        Return the current balance of the account.

        Returns:
            float: The account balance.
        '''
        return self._balance

    balance = property(get_balance)

    def deposit(self, amount: float) -> bool:
        '''
        Add a positive amount of money to the account balance.

        On success, a Transaction record of type Deposit is created and stored
        by this account. Invalid amounts are rejected without creating a
        record.

        Args:
            amount (float): A positive amount of money to deposit.

        Returns:
            bool: True if the deposit succeeded, False otherwise.
        '''
        # Avoid boolean values being accepted as integers.
        if (isinstance(amount, bool)
                or not isinstance(amount, (int, float))
                or amount <= 0):
            print("[INFO] Deposit failed. Invalid amount.")
            return False

        self._balance += amount
        print("[INFO] Deposit successful.")
        self.__create_transaction("Deposit", amount)
        return True

    def withdraw(self, amount: float) -> bool:
        '''
        Take a positive amount of money out of the account balance.

        On success, a Transaction record of type Withdraw is created and
        stored by this account. Invalid amounts and amounts larger than the
        balance are rejected without creating a record.

        Args:
            amount (float): A positive amount of money to withdraw.

        Returns:
            bool: True if the withdraw succeeded, False otherwise.
        '''
        # Avoid boolean values being accepted as integers.
        if (isinstance(amount, bool)
                or not isinstance(amount, (int, float))
                or amount <= 0):
            print("[INFO] Withdraw failed. Invalid amount.")
            return False

        if amount > self._balance:
            print("[INFO] Withdraw failed. Insufficient balance.")
            return False

        self._balance -= amount
        print("[INFO] Withdraw successful.")
        self.__create_transaction("Withdraw", amount)
        return True

    def get_transactions(self) -> list[Transaction]:
        '''
        Return the transaction records created by this account.

        Returns:
            list[Transaction]: The transaction records.
        '''
        return self.__transactions.copy()

    transactions = property(get_transactions)

    def display_balance(self) -> None:
        '''
        Print the account balance to the console.

        Returns:
            None
        '''
        print(f"The balance of Account {self.__id} is ${self._balance}.")

    def __create_transaction(self, transaction_type: str,
                             amount: float) -> None:
        '''
        Create and store a transaction record after a successful operation.

        Args:
            transaction_type (str): The type of the operation.
            amount (float): The amount of money involved.
        '''
        transaction_id = len(self.__transactions) + 1
        transaction = Transaction(transaction_id, transaction_type, amount,
                                  resulting_balance=self._balance,
                                  status="Pending")
        self.__transactions.append(transaction)


class SavingsAccount(Account):
    '''
    Models a bank account of type of savings.
    '''
    MINIMUM_BALANCE = 100.0

    def __init__(self, id: int, interest_rate: float):
        super().__init__(id)
        self.__interest_rate = interest_rate

    def get_interest_rate(self) -> float:
        return self.__interest_rate

    interest_rate = property(get_interest_rate)

    def withdraw(self, amount):
        if amount > self._balance - self.MINIMUM_BALANCE:
            print("[INFO] Withdrawal failed. Minimum balance requirement.")
            return False

        return super().withdraw(amount)


class EverydayAccount(Account):
    '''
    Models a bank account of type of everyday
    '''
    MAX_WITHDRAWAL = 1000.0

    def __init__(self, id: int):
        super().__init__(id)

    def withdraw(self, amount: float) -> bool:
        if amount > self.MAX_WITHDRAWAL:
            print("[INFO] Withdraw failed. Maximum withdraw limit.")
            return False

        return super().withdraw(amount)
