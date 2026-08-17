class Branch:
    '''
    Branch of the financial organisation

    Attributes:
        id (int): Brunch number
        name (str): Brunch name
        location (str): Brunch suburb or location
        phone (str):  Phone number
        is_open (bool): Whether the branch is currently open.
    '''

    def __init__(
            self,
            id: int,
            name: str,
            location: str,
            phone: str,
            is_open=False
    ):
        '''
        Initialization

        Args:
            id (int): Brunch number
            name (str): Brunch name
            location (str): Brunch suburb or location
            phone (str):  Phone number
            is_open (bool): Whether the branch is currently open.
        '''
        if isinstance(id, int): self.id = id
        if isinstance(name, str): self.name = name
        if isinstance(location, str): self.location = location
        if isinstance(phone, str): self.phone = phone
        if is_open in [True, False]: self.is_open = is_open

    def __str__(self) -> str:
        '''
        Display the information associated with the branch

        Returns:
            str: A string containing the branch's information.
        '''
        return f'''Information of Branch #{self.id}
    Name: {self.name}
    Location: {self.location}
    Phone No.: {self.phone}
    State: {"Open" if self.is_open else "Close"}'''

    def __repr__(self) -> str:
        '''
        Display the information associated with the branch

        Returns:
            str: A string containing the branch's information.
        '''
        return f"Branch(id = {self.id}, name = {self.name}, \
location = {self.location}, phone = {self.phone}, \
is_open = {self.is_open})"

    def open(self):
        '''
        Set the branch open
        '''
        self.is_open = True

    def close(self):
        '''
        Set the branch close
        '''
        self.is_open = False

    def set_phone(self, phone: str):
        '''
        Update phone number

        Args:
            phone (str): new branch phone number
        '''
        if isinstance(phone, str): self.phone = phone


if __name__ == "__main__":
    branch_1 = Branch(1, "www", "Firle", "12343232", True)
    branch_2 = Branch(2, "ddd", "Norwood", "2141242")

    branch_2.open()

    print(branch_1)
    print(branch_2)
