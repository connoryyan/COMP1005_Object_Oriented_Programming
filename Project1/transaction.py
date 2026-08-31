from account import Account


class Transaction:
    '''
    Models a single financial transaction and moves money between accounts
    when it is processed.

    The only public attribute is id. All other state is private and is
    accessed through getter and setter methods.

    Attributes:
        id (int): The transaction's unique identifier.
        __type (str): The type of the transaction.
        __amount (float): The amount of money involved in the transaction.
        __description (str): A description of the transaction.
        __status (str): The current status of the transaction.
    '''

    def __init__(self, id: int, transaction_type: str, amount: float,
                 description: str):
        '''
        Initialise a new pending transaction.

        Args:
            id (int): The transaction's unique identifier.
            transaction_type (str): The type of the transaction.
            amount (float): The amount of money involved.
            description (str): A description of the transaction.
        '''
        if not isinstance(id, int) or isinstance(id, bool):
            id = None
        if not isinstance(transaction_type, str):
            transaction_type = None
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            amount = None
        if not isinstance(description, str):
            description = None

        self.id: int | None = id
        self.__type: str | None = transaction_type
        self.__amount: float | None = amount
        self.__description: str | None = description
        self.__status: str = "Pending"

    def __str__(self) -> str:
        '''
        Return a readable description of the transaction.

        Returns:
            str: A string containing the transaction's information.
        '''
        return (f"Information of Transaction #{self.id}\n"
                f"- Type: {self.__type}\n"
                f"- Amount: ${self.__amount}\n"
                f"- Description: {self.__description}\n"
                f"- Status: {self.__status}")

    def __repr__(self) -> str:
        '''
        Return an unambiguous string representation of the transaction.

        Returns:
            str: A string that reconstructs the transaction's state.
        '''
        return (f"Transaction(id={self.id}, type={self.__type}, "
                f"amount={self.__amount}, description={self.__description}, "
                f"status={self.__status})")

    def get_type(self) -> str:
        '''
        Return the type of the transaction.

        Returns:
            str: The transaction type.
        '''
        return self.__type

    def get_amount(self) -> float:
        '''
        Return the amount involved in the transaction.

        Returns:
            float: The transaction amount.
        '''
        return self.__amount

    def get_status(self) -> str:
        '''
        Return the current status of the transaction.

        Returns:
            str: The transaction status.
        '''
        return self.__status

    def process(self, source: Account = None,
                destination: Account = None) -> bool:
        '''
        Process a pending transaction by moving its amount from the source
        account to the destination account.

        A deposit supplies only a destination, a withdrawal supplies only a
        source, and a transfer supplies both.

        Args:
            source (Account): The account the money is taken from.
            destination (Account): The account the money is paid into.

        Returns:
            bool: True if the transaction was processed, False otherwise.
        '''
        if self.__status == "Cancelled":
            print("[INFO] The transaction cannot be completed.")
            return False

        if self.__status == "Processed":
            print("[INFO] The transaction has already been processed.")
            return False

        if source is not None and not source.withdrawal(self.__amount):
            print("[INFO] The transaction cannot be completed.")
            return False

        if destination is not None and not destination.deposit(self.__amount):
            print("[INFO] The transaction cannot be completed.")
            return False

        self.__status = "Processed"
        print("[INFO] Transaction successful.")
        return True

    def cancel(self) -> None:
        '''
        Cancel a pending transaction.
        '''
        self.__status = "Cancelled"
        print("[INFO] Transaction cancelled.")

    def get_description(self) -> str:
        '''
        Return the description of the transaction.

        Returns:
            str: The transaction description.
        '''
        return self.__description

    def set_description(self, description: str) -> None:
        '''
        Update the description of the transaction.

        Args:
            description (str): The new transaction description.
        '''
        if isinstance(description, str):
            self.__description = description
