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
        costs: dict[str, int] | tuple[int, int, int, int, int]
    ):
        if not isinstance(name, str):
            name = "Unknown"
        if not isinstance(undead_name, str):
            undead_name = "Unknown"
        if (not check_int(starting_health)
                or starting_health < Undead.MIN_HEALTH
                or starting_health > Undead.MAX_HEALTH):
            starting_health = Undead.MIN_HEALTH
        if (not check_int(starting_power)
                or starting_power < Undead.MIN_POWER
                or starting_power > Undead.MAX_POWER):
            starting_power = Undead.MIN_POWER

        self.__name: str = name
        self.__undead_name: str = undead_name
        self.__starting_health: int = starting_health
        self.__starting_power: int = starting_power

        costs = ResourceManager.input_to_dict(costs)
        if costs == None or costs["ectoplasm"] <= 0:
            costs = {
                "necrotic_runes": 0,
                "spirit_runes": 0,
                "bone_runes": 0,
                "flesh_runes": 0,
                "ectoplasm": 1
            }
        self.__costs: dict[str, int] = costs

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

    def can_perform(self, resourceManager: ResourceManager) -> bool:
        """Return True if the ritual can currently be performed."""
        if not isinstance(resourceManager, ResourceManager):
            return False

        return resourceManager.has_resources(self.__costs)

    def perform(self, resourceManager: ResourceManager) -> bool:
        """Consume the resources required by the ritual."""
        if not self.can_perform(resourceManager):
            return False

        return resourceManager.spend_resources(self.__costs)

    def summon(self, id: int) -> Undead:
        """Create and return a new undead creature."""
        return Undead(
            id,
            self.__undead_name,
            self.__starting_health,
            self.__starting_power
        )
