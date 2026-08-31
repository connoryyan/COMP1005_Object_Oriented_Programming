from account import Account
from branch import Branch


class Client:
    '''
    Manage the information associated with each client

    Attributes:
        id (int): Client identifier
        name (str): Client name
        __is_active (bool): Whether the client is active
        __preferred_contact (str): Preferred contact method
        __contact (str): Client contact
        accounts (str[]):  accounts of the client
        preferred_branch (Branch): client preferred branch
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
        # self.is_deleted
        if isinstance(id, int): self.id: int = id
        if isinstance(name, str): self.name: str = name
        if isinstance(is_active, bool): self.__is_active: bool = is_active
        if isinstance(preferred_contact, str):
            self.__preferred_contact: str = preferred_contact
        if isinstance(contact, str): self.__contact = contact

        self.accounts:  list[Account] = []
        self.preferred_branch: Branch = None

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
    Preferred branch: {self.preferred_branch}
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
__contact = {self.__contact}, accounts = {self.accounts}), \
preferred_branch = {self.preferred_branch}"

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

    def set_preferred_branch(self, branch: Branch):
        '''
        Set client's preferred branch

        Args:
            branch: the client's preferred branch
        '''
        if isinstance(branch, Branch):
            self.preferred_branch = branch


if __name__ == "__main__":
    account_1 = Account(1, "savings")
    print(account_1)
    account2 = Account(2, "savings")
    print(account2)
    print()

    client_1 = Client(1, "Connor", True, "Email",
                     "connor.yan@student.adelaide.edu.au")
    client_2 = Client(2, "Tianyi", False, "Phone", "04123456")
    client_1.add_account(account_1)
    client_1.add_account(account2)
    print(client_1)
    print()

    client_1.remove_account(account_1)
    print(client_1)
    print()

    print(account_1)
    print()

    branch_1 = Branch(1, "Firle Branch", "Firle", "08 8123 4567", True)
    branch_2 = Branch(2, "Norwood Branch", "Norwood", "08 8234 5678", False)
    branch_3 = Branch(3, "Adelaide Branch",
                        "Adelaide CBD", "08 8345 6789", True)

    client_1.set_preferred_branch(branch_1)
    client_2.set_preferred_branch(branch_3)
    print(client_1)
    print(client_2)
    print()

    client_1.set_preferred_branch(branch_2)
    print(client_1)
    print()

    print(branch_1)
    print(branch_2)
    print(branch_3)
