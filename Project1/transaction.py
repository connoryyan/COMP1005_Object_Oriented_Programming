from account import Account


class Transaction:
    '''
    The information associated with each client

    Attributes:
        id (int): Transaction identifier
        type (str): Transaction type
        amount (float): Amount of the transaction
        description (str):  Transaction description
        status (str): Transaction status
    '''

    def __init__(self, id: int, typ: str, amount: float, description: str):
        '''
        Initialization

        Args:
            id (int): Transaction identifier
            typ (str): Transaction type
            amount (float): Amount of the transaction
            description (str):  Transaction description
        '''
        self.id = id
        self.type = typ
        self.amount = amount
        self.description = description
        self.status = "Pending"

    def __str__(self):
        '''
        Display the information associated with the transaction

        Returns:
            str: A string containing the account's transaction.
        '''
        return f'''Information of Transaction #{self.id}
    Type: {self.type}
    Amount: ${self.amount}
    Description: {self.description}
    Status: {self.status}'''

    def __repr__(self):
        '''
        Display the information associated with the transaction

        Returns:
            str: A string containing the account's transaction.
        '''
        return f"Transaction(id = {self.id}, type = {self.type}, \
description = {self.description}, status = {self.status})"

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

        # res = account1.withdrawal(self.amount)
        # if not res:
        #     print("[INFO] The transaction cannot be completed.")
        #     return False

        # account2.deposit(self.amount)
        self.status = "Processed"
        print("[INFO] Transaction successful.")
        return True

    def cancel(self):
        '''
        Allow a pending transaction to be cancelled
        '''
        self.status = "Cancelled"
        print("[INFO] Transaction cancelled.")

    def update_description(self, description: str):
        '''
        Update transaction description

        Args:
            description (str): new transaction description
        '''
        self.description = description


if __name__ == "__main__":
    transaction_1 = Transaction(1, "n", 100.0, "Hello")
    transaction_2 = Transaction(2, "d", 120.0, "Hello")

    transaction_1.process()
    transaction_2.cancel()

    print(transaction_1)
    print(transaction_2)
