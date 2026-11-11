from resource import ResourceManager
from ritual import SummoningRitual
from undead import Undead


class Necromancer:
    """
    Represent a necromancer who manages resources and controls undead.

    Attributes:
        __name (str): Name of the necromancer.
        __resources (ResourceManager): Resource manager owned by the
            necromancer.
        __undead (list[Undead]): Undead creatures currently controlled.
        __next_id (int): Identifier assigned to the next summoned
            undead.
    """

    MAX_UNDEAD = 10

    def __init__(
        self,
        name: str,
        necrotic_quant: int = 0,
        spirit_quant: int = 0,
        bone_quant: int = 0,
        flesh_quant: int = 0,
        ectoplasm_quant: int = 0
    ) -> None:
        """
        Initialise a necromancer.

        Args:
            name (str): Name of the necromancer.
            necrotic_quant (int): Initial Necrotic Runes.
            spirit_quant (int): Initial Spirit Runes.
            bone_quant (int): Initial Bone Runes.
            flesh_quant (int): Initial Flesh Runes.
            ectoplasm_quant (int): Initial Ectoplasm.
        """

        if not isinstance(name, str):
            name = "Unknown"

        self.__name: str = name

        self.__resources: ResourceManager = ResourceManager(
            necrotic_quant,
            spirit_quant,
            bone_quant,
            flesh_quant,
            ectoplasm_quant
        )

        self.__undead: list[Undead] = []
        self.__next_id: int = 1

    def get_name(self) -> str:
        """
        Get the necromancer's name.

        Returns:
            str: Name of the necromancer.
        """
        return self.__name

    name = property(get_name)

    def get_resources(self) -> ResourceManager:
        """
        Get the resource manager owned by the necromancer.

        Returns:
            ResourceManager: The necromancer's resource manager.
        """
        return self.__resources

    resources = property(get_resources)

    def get_undead(self) -> list[Undead]:
        """
        Get the undead currently controlled by the necromancer.

        Returns:
            list[Undead]: A copy of the controlled undead collection.
        """
        return self.__undead.copy()

    undead = property(get_undead)

    def __find_undead(self, id: int) -> Undead | None:
        """
        Find a controlled undead using its identifier.

        Args:
            id (int): Identifier of the undead to find.

        Returns:
            Undead | None: The matching undead, or None if it is not
                found.
        """
        for undead in self.__undead:
            if undead.id == id:
                return undead

        return None

    def summon(self, ritual: SummoningRitual) -> Undead | None:
        """
        Perform a summoning ritual and add the resulting undead.

        The ritual is only performed if the necromancer has enough
        resources and has not reached the maximum number of controlled
        undead.

        Args:
            ritual (SummoningRitual): Ritual used to create the undead.

        Returns:
            Undead | None: The newly summoned undead if successful,
                otherwise None.
        """
        if not isinstance(ritual, SummoningRitual):
            return None

        if len(self.__undead) >= self.MAX_UNDEAD:
            return None

        if not ritual.can_perform(self.__resources):
            return None

        # Construct before spending so factory errors cannot consume resources.
        try:
            undead = ritual.create_summon(self.__next_id)
            if not isinstance(undead, Undead):
                return None
        except (TypeError, ValueError) as error:
            print(f"[INFO] Summon creation failed: {error}")
            return None

        if not ritual.perform(self.__resources):
            return None

        self.__undead.append(undead)
        self.__next_id += 1

        return undead

    def dismiss(self, id: int) -> bool:
        """
        Dismiss a controlled undead using its identifier.

        Args:
            id (int): Identifier of the undead to dismiss.

        Returns:
            bool: True if the undead was dismissed, otherwise False.
        """
        undead = self.__find_undead(id)

        if undead is None:
            return False

        self.__undead.remove(undead)
        return True

    def level_up(self, id: int) -> bool:
        """
        Level up a controlled undead using its identifier.

        Args:
            id (int): Identifier of the undead to level up.

        Returns:
            bool: True if the undead was found and levelled,
                otherwise False.
        """
        undead = self.__find_undead(id)

        if undead is None:
            return False

        undead.level_up()

        return True

    def command(self, id: int) -> str | None:
        """Command a controlled summon by its identifier."""
        undead = self.__find_undead(id)
        return undead.command() if undead is not None else None

    def __str__(self) -> str:
        """
        Return a string representation of the necromancer.

        Returns:
            str: Necromancer name, resources, and controlled undead.
        """
        result = f"Necromancer: {self.__name}\n"
        result += "Resources:\n"

        for resource in self.__resources.resources.values():
            result += f"  {resource}\n"

        result += (
            f"Controlled Undead: "
            f"{len(self.__undead)}/{self.MAX_UNDEAD}\n"
        )

        for undead in self.__undead:
            result += f"  {undead}\n"

        return result
