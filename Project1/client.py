from account import Account


class Client:
    '''
    The information associated with each client

    Attributes:
        id (int): Client identifier
        name (str): Client name
        __is_active (bool): Whether the client is active
        __preferred_contact (str): Preferred contact method
        __contact (str): Client contact
        accounts (str[]):  accounts of the client
    '''

    def __init__(
            self, id: int,
            name: str,
            is_active: bool,
            preferred_contact: str,
            contact: str
    ):
        '''
        Initialization

        Args:
            id (int): Client identifier
            name (str): Client name
            is_active (bool): Whether the client is active
            preferred_contact (str): Preferred contact method
            contact (str): Client contact
        '''
        self.id = id
        self.name = name
        self.__is_active = is_active
        self.__preferred_contact = preferred_contact
        self.__contact = contact
        self.accounts = []

    def __str__(self) -> str:
        '''
        Display the information associated with the client

        Returns:
            str: A string containing the client's information.
        '''
        return f'''Information of Client #{self.id}
    Name: {self.name}
    Active: {'Yes' if self.__is_active else 'No'}
    Preferred contact method: {self.__preferred_contact}
    Contact: {self.__contact}
    Accounts: {"\n              ".join([a.__str__() for a in self.accounts])}'''

    def __repr__(self) -> str:
        '''
        Display the information associated with the client

        Returns:
            str: A string containing the client's information.
        '''
        return f"Client(id = {self.id}, name = {self.name}, \
__is_active = {self.__is_active}, \
__preferred_contact = {self.__preferred_contact}, \
contact = {self.__contact}, accounts = {self.accounts})"

    # def display_info(self):
    #     '''
    #     Display the information associated with the client

    #     Args:
    #         None

    #     Returns:
    #         None
    #     '''
    #     print(f"Information of Client #{self.id}")
    #     print(f"    Name: {self.name}")
    #     print(f"    Active: {'Yes' if self.__is_active else 'No'}")
    #     print(f"    Preferred contact method: {self.__preferred_contact}")
    #     print(f"    Contact: {self.contact}")
    #     print(f"    Account ID: {self.__account_id}")

    def set_name(self, name: str):
        '''
        Change client's name

        Args:
            name (str): client's new name

        Returns:
            None
        '''
        if isinstance(name, str):
            self.name = name

    def get_preferred_contact(self) -> str:
        '''
        Get Client's preferred contact

        Returns:
            str: client's preferred contact
        '''
        return self.__preferred_contact

    def change_preferred_contact(self, preferred_contact: str):
        '''
        Change Client's preferred contact information

        Args:
            preferred_contact (str): client's new preferred contact method

        Returns:
            None
        '''
        if not isinstance(preferred_contact, str):
            print(f"[INFO] {self.name}'s preferred contact",
                  f"cannot be changed due to invalid input")
            return

        self.__preferred_contact = preferred_contact
        print(f"[INFO] {self.name}'s preferred contact method has been",
              f"changed to {self.__preferred_contact}.")

    def get_contact(self) -> str:
        '''
        Get client's contact

        Returns:
            str: client's contact
        '''
        return self.__contact

    def change_contact(self, contact: str):
        '''
        Change Client's contact information

        Args:
            contact (str): client's new contact information

        Returns:
            None
        '''
        if not isinstance(contact, str):
            print(f"[INFO] {self.name}'s contact",
                  f"cannot be changed due to invalid input")
            return

        self.__contact = contact
        print(f"[INFO] {self.name}'s contact information has been changed "
              f"to {self.__contact}.")

    def get_is_active(self) -> bool:
        '''
        Get if the client is active

        Returns:
            bool: if the client is active
        '''
        return self.__is_active

    def change_is_active(self, is_active: bool):
        '''
        Change the value of self.__is_active

        Args:
            __is_active (bool): if the client is active

        Returns:
            None
        '''
        if is_active not in [True, False]:
            print(f"[INFO] {self.name}'s activation",
                  f"cannot be changed due to invalid input")
            return

        self.__is_active = is_active
        print(f"[INFO] {self.name}'s has been recorded as",
              f"{'active' if self.__is_active else 'inactive'}.")

    def add_account(self, account: Account):
        '''
        Add an account to client

        Args:
            account (Account): the account to be added
        '''
        if isinstance(account, Account) and account not in self.accounts:
            self.accounts.append(account)

    def remove_account(self, account: Account):
        '''
        remove an account by the account name

        Args:
            account (Account): the account to be removed
        '''
        if account in self.accounts:
            self.accounts.remove(account)


if __name__ == "__main__":
    account1 = Account(1, "savings")
    print(account1)
    account2 = Account(2, "savings")
    print(account2)
    print()

    client1 = Client(1, "Connor", True, "Email",
                     "connor.yan@student.adelaide.edu.au")
    client1.add_account(account1)
    client1.add_account(account2)
    print(client1)
    print()

    client1.remove_account(account1)
    print(client1)
    print()

    print(account1)
