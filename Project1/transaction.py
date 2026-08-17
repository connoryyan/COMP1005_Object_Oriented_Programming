from account import Account


class Transaction:
    '''
    The information associated with each client

    Attributes:
        id (int): Transaction identifier
        __type (str): Transaction type
        __amount (float): amount of the transaction
        __description (str):  Transaction description
        status (str): Transaction status
    '''

    def __init__(self, id: int, typ: str, amount: float, description: str):
        '''
        Initialization

        Args:
            id (int): Transaction identifier
            typ (str): Transaction type
            amount (float): amount of the transaction
            description (str):  Transaction description
        '''
        if isinstance(id, int): self.id = id
        if isinstance(typ, str): self.__type = typ
        if isinstance(amount, float): self.__amount = amount
        if isinstance(description, str): self.__description = description
        self.status = "Pending"

    def __str__(self):
        '''
        Display the information associated with the transaction

        Returns:
            str: A string containing the account's transaction.
        '''
        return f'''Information of Transaction #{self.id}
    type: {self.__type}
    amount: ${self.__amount}
    Description: {self.__description}
    Status: {self.status}'''

    def __repr__(self):
        '''
        Display the information associated with the transaction

        Returns:
            str: A string containing the account's transaction.
        '''
        return f"Transaction(id = {self.id}, __type = {self.__type}, \
__amount = {self.__amount}, description = {self.__description}, status = {self.status})"

    def get_type(self) -> str:
        '''
        Get the transaction type

        Returns:
            str: transaction type
        '''
        return self.__type

    def get_amount(self) -> float:
        '''
        Get the transaction amount

        Returns:
            float: transaction amount
        '''
        return self.__amount

    def process(self) -> bool:
        '''
        Allow a pending transaction to be processed

        Args:
            # account1 (Account): The subject of the transaction
            # account2 (Account): The object of the transaction

        Returns:
            bool: If the operation is successful
        '''
        if self.status == "Cancelled":
            print("[INFO] The transaction cannot be completed.")
            return False

        # res = account1.withdrawal(self.__amount)
        # if not res:
        #     print("[INFO] The transaction cannot be completed.")
        #     return False

        # account2.deposit(self.__amount)
        self.status = "Processed"
        print("[INFO] Transaction successful.")
        return True

    def cancel(self):
        '''
        Allow a pending transaction to be cancelled
        '''
        self.status = "Cancelled"
        print("[INFO] Transaction cancelled.")

    def get_description(self) -> str:
        '''
        Get transaction description

        Returns:
            str: transaction description
        '''
        return self.__description

    def set_description(self, description: str):
        '''
        Update transaction description

        Args:
            description (str): new transaction description
        '''
        if isinstance(description, str): self.__description = description


if __name__ == "__main__":
    transaction_1 = Transaction(1, "n", 100.0, "Hello")
    transaction_2 = Transaction(2, "d", 120.0, "Hello")

    transaction_1.process()
    transaction_2.cancel()

    print(transaction_1)
    print(transaction_2)
