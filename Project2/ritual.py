from resource import ResourceManager, check_int, check_unsigned_int
from undead import Undead


class SummoningRitual:
    """Represent a ritual used to summon an undead creature."""

    def __init__(
        self,
        name: str,
        undead_name: str,
        starting_health: int,
        starting_power: int,
        costs: dict[str, int] | tuple[int, int, int, int, int],
        summon_class: type[Undead] = Undead
    ):
        if not isinstance(name, str):
            name = "Unknown"
        if not isinstance(undead_name, str):
            undead_name = "Unknown"
        if (not check_int(starting_health)
                or starting_health < Undead.MIN_HEALTH
                or starting_health > getattr(summon_class, "MAX_HEALTH",
                                             Undead.MAX_HEALTH)):
            starting_health = Undead.MIN_HEALTH
        if (not check_int(starting_power)
                or starting_power < Undead.MIN_POWER
                or starting_power > getattr(summon_class, "MAX_POWER",
                                            Undead.MAX_POWER)):
            starting_power = Undead.MIN_POWER

        self.__name: str = name
        self.__undead_name: str = undead_name
        self.__starting_health: int = starting_health
        self.__starting_power: int = starting_power

        costs = ResourceManager.input_to_dict(costs)
        if costs is None or costs.get("ectoplasm", 0) <= 0:
            costs = {
                "necrotic_runes": 0,
                "spirit_runes": 0,
                "bone_runes": 0,
                "flesh_runes": 0,
                "ectoplasm": 1
            }
        self.__costs: dict[str, int] = dict.fromkeys(
            ResourceManager.KEYS, 0)
        self.__costs.update(costs)

        if not (isinstance(summon_class, type)
                and issubclass(summon_class, Undead)):
            summon_class = Undead

        self.__summon_class: type[Undead] = summon_class

    def get_summon_class(self) -> type[Undead]:
        '''
        Get the specialised undead class this ritual creates.

        Returns:
            type[Undead]: The summon class of the ritual.
        '''
        return self.__summon_class

    def get_name(self):
        return self.__name

    def get_undead_name(self):
        return self.__undead_name

    def get_starting_health(self):
        return self.__starting_health

    def get_starting_power(self):
        return self.__starting_power

    def get_costs(self):
        return self.__costs.copy()

    name = property(get_name)
    undead_name = property(get_undead_name)
    starting_health = property(get_starting_health)
    starting_power = property(get_starting_power)
    costs = property(get_costs)
    summon_class = property(get_summon_class)

    def can_perform(self, resource_manager: ResourceManager) -> bool:
        """Return True if the ritual can currently be performed."""
        if not isinstance(resource_manager, ResourceManager):
            return False

        return resource_manager.has_resources(self.__costs)

    def perform(self, resource_manager: ResourceManager) -> bool:
        """Consume the resources required by the ritual."""
        if not self.can_perform(resource_manager):
            return False

        return resource_manager.spend_resources(self.__costs)

    def create_summon(self, id: int) -> Undead:
        '''
        Create and return a new undead creature of the ritual's summon
            class.

        Args:
            id (int): Identifier supplied by the necromancer.

        Returns:
            Undead: The newly created specialised undead creature.
        '''
        return self.__summon_class(
            id,
            self.__undead_name,
            self.__starting_health,
            self.__starting_power
        )

    def summon(self, id: int) -> Undead:
        """Create and return a new undead creature."""
        return self.create_summon(id)
