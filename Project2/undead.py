class Undead:
    # Current stat boundaries
    MIN_HEALTH = 1
    MAX_HEALTH = 100
    MIN_POWER = 1
    MAX_POWER = 100
    MAX_LEVEL = 10

    # Stat growth
    HEALTH_PER_LEVEL = 10
    POWER_PER_LEVEL = 5

    def __init__(self, id, name, health, power):
        self.__id = id
        self.__name = name
        self.__health = health
        self.__power = power
        self.__level = 1

    def get_id(self):
        return self.__id
    id = property(get_id)

    def get_name(self):
        return self.__name
    name = property(get_name)

    def get_health(self):
        return self.__health
    health = property(get_health)

    def get_power(self):
        return self.__power
    power = property(get_power)

    def get_level(self):
        return self.__level
    level = property(get_level)

    def level_up(self):
        if self.__level < self.MAX_LEVEL:
            self.__level += 1

            self.__health = min(
                self.__health + self.HEALTH_PER_LEVEL,
                self.MAX_HEALTH
            )

            self.__power = min(
                self.__power + self.POWER_PER_LEVEL,
                self.MAX_POWER
            )

    def __str__(self) -> str:
        return (
            f"{self.__id}: {self.__name} "
            f"(Level {self.__level}) "
            f"Health: {self.__health}/{self.MAX_HEALTH}, "
            f"Power: {self.__power}/{self.MAX_POWER}"
        )