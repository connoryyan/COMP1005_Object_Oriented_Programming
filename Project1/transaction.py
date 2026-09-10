from __future__ import annotations


class Transaction:
    '''
    Models a financial transaction on an account.

    A Transaction can be created in two ways. It can be created as a pending
    operation and later processed or cancelled through process() and cancel().
    It can also be created by an Account after a successful deposit or
    withdrawal, in which case it is a completed record that additionally
    stores the resulting balance (composition between Account and
    Transaction).

    All attributes are private. Identifiers and fixed values are exposed
    through read-only properties; the description has a property setter; and
    the status changes only through process() and cancel().

    Attributes:
        __id (int): The transaction's unique identifier.
        __type (str): The type of the transaction (e.g. Deposit, Withdrawal or
            Transfer).
        __amount (float): The amount of money involved in the transaction.
        __description (str): A description of the transaction.
        __status (str): The current status of the transaction.
        __resulting_balance (float): The balance after the operation, set for
            records created by Account.
    '''

    def __init__(self, id: int, transaction_type: str, amount: float,
                 description: str = "", resulting_balance: float | None = None,
                 status: str = "Pending"):
        '''
        Initialise a new pending transaction.

        Args:
            id (int): The transaction's unique identifier.
            transaction_type (str): The type of the transaction.
            amount (float): The amount of money involved.
            description (str): A description of the transaction.
            resulting_balance (float): The resulting balance, when the
                transaction records a completed deposit or withdrawal.
            status (str): The initial status of the transaction.
        '''
        if not isinstance(id, int) or isinstance(id, bool):
            id = None
        if not isinstance(transaction_type, str):
            transaction_type = None
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            amount = None
        if not isinstance(description, str):
            description = None
        if resulting_balance is not None and (
                isinstance(resulting_balance, bool)
                or not isinstance(resulting_balance, (int, float))):
            resulting_balance = None
        if status not in ("Pending", "Processed", "Cancelled"):
            status = "Pending"

        self.__id: int | None = id
        self.__type: str | None = transaction_type
        self.__amount: float | None = amount
        self.__description: str | None = description
        self.__status: str = status
        self.__resulting_balance: float | None = resulting_balance

    def get_id(self) -> int | None:
        '''
        Return the identifier of the transaction.

        Returns:
            int: The transaction identifier.
        '''
        return self.__id

    id = property(get_id)

    def get_type(self) -> str | None:
        '''
        Return the type of the transaction.

        Returns:
            str: The transaction type.
        '''
        return self.__type

    type = property(get_type)

    def get_amount(self) -> float | None:
        '''
        Return the amount of money involved in the transaction.

        Returns:
            float: The transaction amount.
        '''
        return self.__amount

    amount = property(get_amount)

    def get_description(self) -> str | None:
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

    description = property(get_description, set_description)

    def get_status(self) -> str:
        '''
        Return the current status of the transaction.

        Returns:
            str: The transaction status.
        '''
        return self.__status

    status = property(get_status)

    def get_resulting_balance(self) -> float | None:
        '''
        Return the balance that resulted from the recorded operation.

        Returns:
            float: The resulting balance, or None when not recorded.
        '''
        return self.__resulting_balance

    resulting_balance = property(get_resulting_balance)

    def process(self) -> bool:
        '''
        Process a pending transaction.

        Returns:
            bool: True if the transaction was processed, False otherwise.
        '''
        if self.__status == "Cancelled":
            print("[INFO] The transaction cannot be completed.")
            return False

        if self.__status == "Processed":
            print("[INFO] The transaction has already been processed.")
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

    def __str__(self) -> str:
        '''
        Return a readable description of the transaction.

        Returns:
            str: A string containing the transaction's information.
        '''
        text = (f"Information of Transaction #{self.__id}\n"
                f"- Type: {self.__type}\n"
                f"- Amount: ${self.__amount}\n")
        if self.__description:
            text += f"- Description: {self.__description}\n"
        if self.__resulting_balance is not None:
            text += f"- Resulting balance: ${self.__resulting_balance}\n"
        text += f"- Status: {self.__status}"
        return text

    def __repr__(self) -> str:
        '''
        Return an unambiguous string representation of the transaction.

        Returns:
            str: A string that reconstructs the transaction's state.
        '''
        return (f"Transaction(id={self.__id}, type={self.__type}, "
                f"amount={self.__amount}, description={self.__description}, "
                f"status={self.__status}, "
                f"resulting_balance={self.__resulting_balance})")
