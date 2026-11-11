def check_int(num) -> bool:
    return (isinstance(num, int)
            and not isinstance(num, bool))


def check_unsigned_int(num) -> bool:
    return (check_int(num)
            and num >= 0)


class Resource:
    '''
    Handle the information of a type of resource used for summoning.

    Attributes:
        __name (str): Name of the resource.
        __quantity (int): Quantity of the resource.
        __description (str): Description of the resource.
    '''

    MIN_QUANTITY = 0

    def __init__(self, name: str, description: str, quantity: int = 0):
        '''
        Initiate a resource object.

        Args:
            name (str): Resource name.
            description (str): Resource description.
            quantity (int): Resource quantity.
        '''
        if not isinstance(name, str):
            name = "Unknown"
        if not isinstance(description, str):
            description = "Unknown"
        if not check_unsigned_int(quantity):
            quantity = self.MIN_QUANTITY

        self.__name: str = name
        self.__quantity: int = quantity
        self.__description: str = description

    def get_name(self) -> str:
        '''
        Get resource name.

        Returns:
            str: Resource name.
        '''
        return self.__name
    name = property(get_name)

    def get_description(self) -> str:
        '''
        Get resource description.

        Returns:
            str: Resource description.
        '''
        return self.__description
    description = property(get_description)

    def get_quantity(self) -> int:
        '''
        Get resource quantity.

        Returns:
            int: Resource quantity.
        '''
        return self.__quantity

    quantity = property(get_quantity)

    def add_quantity(self, quantity):
        '''
        Add a quantity of resouce.

        Args:
            quantity (int): Quantity of resource to be added.
        '''
        if (not isinstance(quantity, int)
                or isinstance(quantity, bool)
                or self.__quantity + quantity < 0):
            return

        self.__quantity += quantity

    def __str__(self):
        '''
        Returns a string represneting this object.

        Returns:
            str: A string represneting this object.
        '''
        return (f"Resource name: {self.__name}, Quantity: {self.__quantity}, "
                f"Description: {self.__description}.")


class ResourceManager:
    '''
    The class responsible for managing resources used during summoning.

    Attributes:
        __necrotic_runes (Resource): Resource object representing
            Necrotic
          Runes
        __spirit_runes (Resource): Resource object representing Spirit
            Runes.
        __bone_runes (Resource): Resource object representing Bone
            Runes.
        __flesh_runes (Resource): Resourece object representing Flesh
            Runes.
        __ectoplasm (Resource): Resource object representing Ectoplasm.
    '''

    KEYS = (
        "necrotic_runes",
        "spirit_runes",
        "bone_runes",
        "flesh_runes",
        "ectoplasm"
    )

    def __init__(self,
                 necrotic_quant: int = 0,
                 spirit_quant: int = 0,
                 bone_quant: int = 0,
                 flesh_quant: int = 0,
                 ectoplasm_quant: int = 0):
        '''
        Initiate
        '''
        self.__resources = {
            "necrotic_runes": Resource(
                "Necrotic Runes",
                "Necrotic runes are a type of runes consisting of spirit,"
                " bone, flesh, and miasma runes.",
                necrotic_quant  # Validation done in Resource class
            ),
            "spirit_runes": Resource(
                "Spirit Runes",
                "Spirit Runes may be more important for spectral summons.",
                spirit_quant
            ),
            "bone_runes": Resource(
                "Bone Runes",
                "Bone Runes may be more important for skeletal summons.",
                bone_quant
            ),
            "flesh_runes": Resource(
                "Flesh Runes",
                "Flesh Runes may be more important for corpse-based summons.",
                flesh_quant
            ),
            "ectoplasm": Resource(
                "Ectoplasm",
                "Ectoplasm is used to draw alteration glyphs "
                "and for conjuring.",
                ectoplasm_quant
            )
        }

    def get_resources(self) -> dict[str, Resource]:
        '''
        Get resources.

        Returns:
            dict[str, Resource]: name of the resource and the
                coresponding
              Resource object.
        '''
        return self.__resources.copy()  # shallow copy
    resources = property(get_resources)

    @staticmethod
    def input_to_dict(
        quantities: dict[str, int] | tuple[int, int, int, int, int]
    ) -> dict[str, int] | None:

        if isinstance(quantities, dict):
            items = quantities.items()

        elif isinstance(quantities, tuple):
            if len(quantities) != 5:
                return None

            items = zip(ResourceManager.KEYS, quantities)

        else:
            return None

        result = {}

        for key, num in items:
            if not (check_unsigned_int(num)
                    and key in ResourceManager.KEYS):
                return None

            result[key] = num

        return result

    def collect_resources(
        self,
        quantities: dict[str, int] | tuple[int, int, int, int, int]
    ):
        '''
        Add each resource by some quantity.

        Args:
            quantities (dict[str, Resource]): quantity of corresponding
              resource, e.g. {"spirit_runes": 4, ...}
        '''
        requirements = self.input_to_dict(quantities)
        if requirements is None:
            return

        for key, num in requirements.items():
            self.__resources[key].add_quantity(num)

    def has_resources(
        self,
        quantities: dict[str, int] | tuple[int, int, int, int, int]
    ) -> bool:
        requirements = self.input_to_dict(quantities)
        if requirements is None:
            return False

        for key, num in requirements.items():
            if self.__resources[key].quantity < num:
                return False

        return True

    def spend_resources(
        self,
        quantities: dict[str, int] | tuple[int, int, int, int, int]
    ) -> bool:
        '''
        Add each resource by some quantity.

        Args:
            quantities (dict[str, Resource]): quantity of corresponding
                resource, e.g. {"spirit_runes": 4, ...}
        '''
        requirements = self.input_to_dict(quantities)
        if requirements is None:
            return False

        if not self.has_resources(quantities):
            return False

        for key, num in requirements.items():
            self.__resources[key].add_quantity(-num)

        return True

    def __str__(self) -> str:
        return "\n".join(
            str(resource) for resource in self.__resources.values())
