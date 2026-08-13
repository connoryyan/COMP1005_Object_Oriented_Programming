

class Client:
    '''
    The information associated with each client

    Attributes:
        id (int): Client identifier
        name (str): Client name
        is_active (bool): Whether the client is active
        preferred_contact (str): Preferred contact method
        contact (str): Client contact
        account_id (str):  Identifier of client's account
    '''

    def __init__(
            self, id: int,
            name: str,
            is_active: bool,
            preferred_contact: str,
            contact: str,
            account_id: int
    ):
        '''
        Initialization

        Args:
            id (int): Client identifier
            name (str): Client name
            is_active (bool): Whether the client is active
            preferred_contact (str): Preferred contact method
            contact (str): Client contact
            account_id (str):  Identifier of client's account
        '''
        self.id = id
        self.name = name
        self.is_active = is_active
        self.preferred_contact = preferred_contact
        self.contact = contact
        self.account_id = account_id

    def __str__(self) -> str:
        '''
        Display the information associated with the client

        Returns:
            str: A string containing the client's information.
        '''
        return f'''Information of Client #{self.id}
    Name: {self.name}
    Active: {'Yes' if self.is_active else 'No'}
    Preferred contact method: {self.preferred_contact}
    Contact: {self.contact}
    Account ID: {self.account_id}'''

    def __repr__(self) -> str:
        '''
        Display the information associated with the client

        Returns:
            str: A string containing the client's information.
        '''
        return f"Client(id = {self.id}, name = {self.name}, \
is_active = {self.is_active}, \
preferred_contact = {self.preferred_contact}, \
contact = {self.contact}, account_id = {self.account_id})"

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
    #     print(f"    Active: {'Yes' if self.is_active else 'No'}")
    #     print(f"    Preferred contact method: {self.preferred_contact}")
    #     print(f"    Contact: {self.contact}")
    #     print(f"    Account ID: {self.account_id}")

    def change_name(self, name: str):
        '''
        Change client's name

        Args:
            name (str): client's new name

        Returns:
            None
        '''
        self.name = name

    def change_preferred_contact(self, preferred_contact: str):
        '''
        Change Client's contact information

        Args:
            preferred_contact (str): client's new preferred contact method

        Returns:
            None
        '''
        self.preferred_contact = preferred_contact
        print(f"[INFO] {self.name}'s preferred contact method has been " 
            + f"changed to {self.preferred_contact}.")

    def change_contact(self, contact: str):
        '''
        Change Client's contact information

        Args:
            contact (str): client's new contact information

        Returns:
            None
        '''
        self.contact = contact
        print(f"[INFO] {self.name}'s contact information has been changed "
            + f"to {self.contact}.")

    def change_is_active(self, is_active: bool):
        '''
        Change the value of self.is_active

        Args:
            is_active (bool): if the client is active

        Returns:
            None
        '''
        self.is_active = is_active
        print(f"[INFO] {self.name}'s has been recorded as \
              {'active' if self.is_active else 'inactive'}.")
