class Branch:
    '''
    Manage information of a branch of the financial organisation

    Attributes:
        id (int): Brunch number
        __name (str): Brunch name
        __location (str): Brunch suburb or location
        __phone (str):  Phone number
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
        if isinstance(id, int): self.id: int = id
        if isinstance(name, str): self.__name: str = name
        if isinstance(location, str): self.__location: str = location
        if isinstance(phone, str): self.__phone: str = phone
        if is_open in [True, False]: self.is_open: bool = is_open

    def __str__(self) -> str:
        '''
        Display the information associated with the branch

        Returns:
            str: A string containing the branch's information.
        '''
        return f"Branch id:{self.id}, Name: {self.__name}, Location: {self.__location}, Phone No.: {self.__phone},State: {"Open" if self.is_open else "Close"}"

    def __repr__(self) -> str:
        '''
        Display the information associated with the branch

        Returns:
            str: A string containing the branch's information.
        '''
        return f"Branch(id = {self.id}, name = {self.__name}, \
location = {self.__location}, phone = {self.__phone}, \
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

    def get_name(self) -> str:
        '''
        Get branch name

        Returns:
            str: branch name
        '''
        return self.__name

    def set_name(self, name):
        '''
        Set branch name

        Args:
            name (str): branch name
        '''
        if isinstance(name, str): self.__name = name

    def get_location(self) -> str:
        '''
        Get branch location

        Returns:
            str: branch location
        '''
        return self.__location
    
    def set_location(self, location):
        '''
        Set branch location

        Args:
            location (str): branch location
        '''
        if isinstance(location, str): self.__name = location

    def get_phone(self) -> str:
        '''
        Get branch phone number

        Returns:
            str: branch phone number
        '''
        return self.__phone

    def set_phone(self, phone: str):
        '''
        Update phone number

        Args:
            phone (str): new branch phone number
        '''
        if isinstance(phone, str): self.__phone = phone


if __name__ == "__main__":
    branch_1 = Branch(1, "www", "Firle", "12343232", True)
    branch_2 = Branch(2, "ddd", "Norwood", "2141242")

    branch_2.open()

    print(branch_1)
    print(branch_2)
