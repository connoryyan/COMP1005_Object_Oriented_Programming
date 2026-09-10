class Branch:
    '''
    Models a single branch of the financial organisation.

    All attributes are private and are exposed through properties. The branch
    name, location and phone number can be updated through their property
    setters, while the open/closed state can only change through the
    behavioural methods open() and close().

    Attributes:
        __id (int): The branch's unique identifier.
        __name (str): The branch's name.
        __location (str): The branch's suburb or location.
        __phone (str): The branch's phone number.
        __is_open (bool): Whether the branch is currently open.
    '''

    def __init__(self, id: int, name: str, location: str, phone: str,
                 is_open: bool = False):
        '''
        Initialise a new branch.

        Args:
            id (int): The branch's unique identifier.
            name (str): The branch's name.
            location (str): The branch's suburb or location.
            phone (str): The branch's phone number.
            is_open (bool): Whether the branch is currently open.
        '''
        if not isinstance(id, int) or isinstance(id, bool):
            id = None
        if not isinstance(name, str):
            name = None
        if not isinstance(location, str):
            location = None
        if not isinstance(phone, str):
            phone = None
        if not isinstance(is_open, bool):
            is_open = False

        self.__id: int | None = id
        self.__name: str | None = name
        self.__location: str | None = location
        self.__phone: str | None = phone
        self.__is_open: bool = is_open

    def get_id(self) -> int | None:
        '''
        Return the identifier of the branch.

        Returns:
            int: The branch identifier.
        '''
        return self.__id

    id = property(get_id)

    def get_name(self) -> str | None:
        '''
        Return the name of the branch.

        Returns:
            str: The branch name.
        '''
        return self.__name

    def set_name(self, name: str) -> None:
        '''
        Update the name of the branch.

        Args:
            name (str): The new branch name.
        '''
        if isinstance(name, str):
            self.__name = name

    name = property(get_name, set_name)

    def get_location(self) -> str | None:
        '''
        Return the location of the branch.

        Returns:
            str: The branch location.
        '''
        return self.__location

    def set_location(self, location: str) -> None:
        '''
        Update the location of the branch.

        Args:
            location (str): The new branch location.
        '''
        if isinstance(location, str):
            self.__location = location

    location = property(get_location, set_location)

    def get_phone(self) -> str | None:
        '''
        Return the phone number of the branch.

        Returns:
            str: The branch phone number.
        '''
        return self.__phone

    def set_phone(self, phone: str) -> None:
        '''
        Update the phone number of the branch.

        Args:
            phone (str): The new branch phone number.
        '''
        if isinstance(phone, str):
            self.__phone = phone

    phone = property(get_phone, set_phone)

    def get_is_open(self) -> bool:
        '''
        Return whether the branch is currently open.

        Returns:
            bool: True if the branch is open, False otherwise.
        '''
        return self.__is_open

    is_open = property(get_is_open)

    def open(self) -> None:
        '''
        Mark the branch as open for business.
        '''
        self.__is_open = True

    def close(self) -> None:
        '''
        Mark the branch as closed for business.
        '''
        self.__is_open = False

    def __str__(self) -> str:
        '''
        Return a readable description of the branch.

        Returns:
            str: A string containing the branch's information.
        '''
        state = "Open" if self.__is_open else "Closed"
        return (f"Branch id: {self.__id}, Name: {self.__name}, "
                f"Location: {self.__location}, Phone No.: {self.__phone}, "
                f"State: {state}")

    def __repr__(self) -> str:
        '''
        Return an unambiguous string representation of the branch.

        Returns:
            str: A string that reconstructs the branch's state.
        '''
        return (f"Branch(id={self.__id}, name={self.__name}, "
                f"location={self.__location}, phone={self.__phone}, "
                f"is_open={self.__is_open})")
