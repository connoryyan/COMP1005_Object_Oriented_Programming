from .account import Account
from .branch import Branch
from .exceptions import AccountNotFoundError


class Client:
    '''
    Models a client of the financial organisation.

    Attributes:
        __id (int): The client's unique identifier.
        __name (str): The client's name.
        __is_active (bool): Whether the client's record is active.
        __preferred_contact (str): The client's preferred contact
            method.
        __contact (str): The client's contact details.
        __accounts (dict[int, Account]): The accounts owned by the
            client.
        __preferred_branch (Branch): The client's preferred branch.
    '''

    def __init__(self, id: int, name: str, is_active: bool,
                 preferred_contact: str, contact: str):
        '''
        Initialise a new client with no accounts and no preferred
            branch.

        Args:
            id (int): The client's unique identifier.
            name (str): The client's name.
            is_active (bool): Whether the client's record is active.
            preferred_contact (str): The client's preferred contact
                method.
            contact (str): The client's contact details.
        '''
        if not isinstance(id, int) or isinstance(id, bool):
            id = None
        if not isinstance(name, str):
            name = None
        if not isinstance(is_active, bool):
            is_active = False
        if not isinstance(preferred_contact, str):
            preferred_contact = None
        if not isinstance(contact, str):
            contact = None

        self.__id: int | None = id
        self.__name: str | None = name
        self.__is_active: bool = is_active
        self.__preferred_contact: str | None = preferred_contact
        self.__contact: str | None = contact
        self.__accounts: dict[int, Account] = dict()
        self.__preferred_branch: Branch | None = None

    def get_id(self) -> int | None:
        '''
        Return the identifier of the client.

        Returns:
            int: The client identifier.
        '''
        return self.__id

    id = property(get_id)

    def get_name(self) -> str | None:
        '''
        Return the name of the client.

        Returns:
            str: The client's name.
        '''
        return self.__name

    def set_name(self, name: str) -> None:
        '''
        Update the name of the client.

        Args:
            name (str): The client's new name.
        '''
        if isinstance(name, str):
            self.__name = name

    name = property(get_name, set_name)

    def get_preferred_contact(self) -> str | None:
        '''
        Return the client's preferred contact method.

        Returns:
            str: The preferred contact method.
        '''
        return self.__preferred_contact

    preferred_contact = property(get_preferred_contact)

    def change_preferred_contact(self, preferred_contact: str) -> None:
        '''
        Update the client's preferred contact method.

        Args:
            preferred_contact (str): The new preferred contact method.
        '''
        if not isinstance(preferred_contact, str):
            print(f"[INFO] {self.__name}'s preferred contact cannot be "
                  f"changed due to invalid input.")
            return

        self.__preferred_contact = preferred_contact
        print(f"[INFO] {self.__name}'s preferred contact method has been "
              f"changed to {self.__preferred_contact}.")

    def get_contact(self) -> str | None:
        '''
        Return the client's contact details.

        Returns:
            str: The client's contact details.
        '''
        return self.__contact

    contact = property(get_contact)

    def change_contact(self, contact: str) -> None:
        '''
        Update the client's contact details.

        Args:
            contact (str): The client's new contact details.
        '''
        if not isinstance(contact, str):
            print(f"[INFO] {self.__name}'s contact cannot be changed due "
                  f"to invalid input.")
            return

        self.__contact = contact
        print(f"[INFO] {self.__name}'s contact information has been changed "
              f"to {self.__contact}.")

    def get_is_active(self) -> bool:
        '''
        Return whether the client's record is active.

        Returns:
            bool: True if the client is active, False otherwise.
        '''
        return self.__is_active

    is_active = property(get_is_active)

    def change_is_active(self, is_active: bool) -> None:
        '''
        Update whether the client's record is active.

        Args:
            is_active (bool): Whether the client should be active.
        '''
        if not isinstance(is_active, bool):
            print(f"[INFO] {self.__name}'s activation cannot be changed "
                  f"due to invalid input.")
            return

        self.__is_active = is_active
        state = "active" if self.__is_active else "inactive"
        print(f"[INFO] {self.__name} has been recorded as {state}.")

    def get_account(self, account_number: int) -> Account | None:
        '''
        Retrieve an account by account number.

        Args:
            account_number (int): The account number.

        Returns:
            Account | None: The matching account. If no matching
                account,
            `None` will be returned.
        '''

        try:
            if (not isinstance(account_number, int)
                    or isinstance(account_number, bool)
                    or account_number not in self.__accounts):
                raise AccountNotFoundError(
                    f"Client {self.id}: account {account_number!r} not found.")
            return self.__accounts[account_number]
        except AccountNotFoundError as error:
            print(f"[INFO] {error}")
            return None

    def get_accounts(self) -> dict[int, Account]:
        '''
        Return the accounts owned by the client.

        A copy of the internal collection is returned so the caller
            cannot
        modify it directly; accounts are only added and removed through
        add_account() and remove_account().

        Returns:
            dict[int, Account]: The client's accounts.
        '''
        return dict(self.__accounts)

    accounts = property(get_accounts)

    def add_account(self, account: Account) -> None:
        '''
        Add an account to the client's dictionary of accounts.

        Args:
            account (Account): The account to add.
        '''
        if (isinstance(account, Account) and account.id is not None
                and account.id not in self.__accounts):
            self.__accounts[account.id] = account

    def remove_account(self, account: Account) -> None:
        '''
        Remove an account from the client's dictionary of accounts.

        Args:
            account (Account): The account to remove.
        '''
        if isinstance(account, Account):
            self.remove_account_number(account.id)

    def remove_account_number(self, account_number: int) -> None:
        '''
        Remove an account using its account number.

        Args:
            account (Account): The account to remove.
        '''
        if self.get_account(account_number) is not None:
            self.__accounts.pop(account_number)

    def get_preferred_branch(self) -> Branch | None:
        '''
        Return the client's preferred branch.

        Returns:
            Branch: The client's preferred branch, or None if not set.
        '''
        return self.__preferred_branch

    preferred_branch = property(get_preferred_branch)

    def set_preferred_branch(self, branch: Branch) -> None:
        '''
        Set the client's preferred branch.

        Args:
            branch (Branch): The client's preferred branch.
        '''
        if isinstance(branch, Branch):
            self.__preferred_branch = branch

    def __str__(self) -> str:
        '''
        Return a readable description of the client.

        Returns:
            str: A string containing the client's information.
        '''
        accounts = "\n              ".join(
            str(a) for a in self.__accounts.values())
        return (f"Information of Client #{self.__id}\n"
                f"    Name: {self.__name}\n"
                f"    Active: {'Yes' if self.__is_active else 'No'}\n"
                f"    Preferred contact method: {self.__preferred_contact}\n"
                f"    Contact: {self.__contact}\n"
                f"    Preferred branch: {self.__preferred_branch}\n"
                f"    Accounts: {accounts}")

    def __repr__(self) -> str:
        '''
        Return an unambiguous string representation of the client.

        Returns:
            str: A string that reconstructs the client's state.
        '''
        return (f"Client(id={self.__id}, name={self.__name}, "
                f"is_active={self.__is_active}, "
                f"preferred_contact={self.__preferred_contact}, "
                f"contact={self.__contact}, accounts={self.__accounts}, "
                f"preferred_branch={self.__preferred_branch})")
