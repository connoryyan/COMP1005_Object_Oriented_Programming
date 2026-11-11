class Undead:
    '''
    Models a general undead creature.

    Every undead shares this state and behaviour. Specialised undead
        inherit
    from this class and override only what makes them different, so the
        stat
    boundaries and the command() behaviour can vary between summons.

    Attributes:
        __id (int): Identifier of the undead.
        __name (str): Name of the undead.
        _health (int): Current health of the undead. Protected so that
            subclasses can apply their own stat boundaries.
        _power (int): Current power of the undead. Protected for the
            same
            reason.
        _level (int): Current level of the undead.
    '''

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
        self._health = health
        self._power = power
        self._level = 1
        self._clamp_stats()

    def get_id(self):
        return self.__id
    id = property(get_id)

    def get_name(self):
        return self.__name
    name = property(get_name)

    def get_health(self):
        return self._health
    health = property(get_health)

    def get_power(self):
        return self._power
    power = property(get_power)

    def get_level(self):
        return self._level
    level = property(get_level)

    def level_up(self):
        if self._level < self.MAX_LEVEL:
            self._level += 1

            self._health = min(
                self._health + self.HEALTH_PER_LEVEL,
                self.MAX_HEALTH
            )

            self._power = min(
                self._power + self.POWER_PER_LEVEL,
                self.MAX_POWER
            )

    def command(self) -> str:
        '''
        Give a general order to this undead creature.

        Specialised undead override this method and extend the response
            with
        behaviour that is specific to them.

        Returns:
            str: A description of how the undead responds to the order.
        '''
        return f"{self.name} (Level {self.level}) awaits your command."

    def _clamp_stats(self) -> None:
        '''
        Clamp health and power to the stat boundaries of this class.

        Specialised undead override MIN_HEALTH, MAX_HEALTH, MIN_POWER
            and
        MAX_POWER. This protected helper is reused by their constructors
            so
        every summon stays within its own boundaries without repeating
            the
        same code.
        '''
        self._health = max(
            self.MIN_HEALTH,
            min(self._health, self.MAX_HEALTH)
        )

        self._power = max(
            self.MIN_POWER,
            min(self._power, self.MAX_POWER)
        )

    def __str__(self) -> str:
        return (
            f"{self.__id}: {self.__name} "
            f"(Level {self._level}) "
            f"Health: {self._health}/{self.MAX_HEALTH}, "
            f"Power: {self._power}/{self.MAX_POWER}"
        )


class WarriorUndead(Undead):
    '''
    Models an undead creature specialised in combat.

    Inherits all state and behaviour from Undead. Its constructor passes
        the
    common information up with super(), and command() is overridden with
    behaviour suitable for a warrior.
    '''

    def __init__(self, id, name, health, power):
        '''
        Initialise a warrior undead.

        Args:
            id (int): Identifier of the undead.
            name (str): Name of the undead.
            health (int): Starting health of the undead.
            power (int): Starting power of the undead.
        '''
        super().__init__(id, name, health, power)

    def command(self) -> str:
        '''
        Order the warrior undead into battle.

        Returns:
            str: The general response, extended with warrior behaviour.
        '''
        return super().command() + " It grips its weapon, ready to strike."

    def combat_style(self) -> str:
        return "Fights using direct martial combat."


class CursedUndead(Undead):
    '''
    Models an undead creature twisted by a curse.

    Inherits all state and behaviour from Undead. Its constructor passes
        the
    common information up with super(), and command() is overridden with
    behaviour suitable for a cursed undead.
    '''

    def __init__(self, id, name, health, power):
        '''
        Initialise a cursed undead.

        Args:
            id (int): Identifier of the undead.
            name (str): Name of the undead.
            health (int): Starting health of the undead.
            power (int): Starting power of the undead.
        '''
        super().__init__(id, name, health, power)

    def command(self) -> str:
        '''
        Order the cursed undead to obey.

        Returns:
            str: The general response, extended with cursed behaviour.
        '''
        return super().command() + " Dark energy coils around its body."

    def combat_style(self) -> str:
        return "Fights using cursed supernatural powers."


class SkeletonWarrior(WarriorUndead):
    '''
    Models a skeletal warrior summon.

    Uses its own stat boundaries while reusing the inherited levelling
    behaviour and the warrior command().
    '''

    MIN_HEALTH = 10
    MAX_HEALTH = 90
    MIN_POWER = 10
    MAX_POWER = 70

    def __init__(self, id, name, health, power):
        '''
        Initialise a skeleton warrior.

        Args:
            id (int): Identifier of the undead.
            name (str): Name of the undead.
            health (int): Starting health of the undead.
            power (int): Starting power of the undead.
        '''
        super().__init__(id, name, health, power)
        self._clamp_stats()

    def command(self) -> str:
        '''
        Order the skeleton warrior to advance.

        Returns:
            str: The warrior response, extended with skeletal behaviour.
        '''
        return super().command() + " Its bones clatter as it charges."


class PhantomGuardian(WarriorUndead):
    '''
    Models a spectral guardian summon.

    The toughest summon: it keeps the warrior command() but has the
        highest
    health boundary of the hierarchy.
    '''

    MIN_HEALTH = 30
    MAX_HEALTH = 140
    MIN_POWER = 20
    MAX_POWER = 100

    def __init__(self, id, name, health, power):
        '''
        Initialise a phantom guardian.

        Args:
            id (int): Identifier of the undead.
            name (str): Name of the undead.
            health (int): Starting health of the undead.
            power (int): Starting power of the undead.
        '''
        super().__init__(id, name, health, power)
        self._clamp_stats()


class VengefulGhost(CursedUndead):
    '''
    Models a vengeful ghost summon.

    Frail in body but the strongest in spirit: it keeps the cursed
        command()
    and has the highest power boundary of the hierarchy.
    '''

    MIN_HEALTH = 10
    MAX_HEALTH = 80
    MIN_POWER = 20
    MAX_POWER = 110

    def __init__(self, id, name, health, power):
        '''
        Initialise a vengeful ghost.

        Args:
            id (int): Identifier of the undead.
            name (str): Name of the undead.
            health (int): Starting health of the undead.
            power (int): Starting power of the undead.
        '''
        super().__init__(id, name, health, power)
        self._clamp_stats()

    def command(self) -> str:
        '''
        Order the vengeful ghost to act.

        Returns:
            str: The cursed response, extended with ghost behaviour.
        '''
        return (super().command()
                + " It wails for vengeance and fades from sight.")


class PutridZombie(Undead):
    '''
    Models a rotting zombie summon.

    Inherits directly from Undead: it is durable but weak, and keeps the
    general command() behaviour.
    '''

    MIN_HEALTH = 20
    MAX_HEALTH = 100
    MIN_POWER = 5
    MAX_POWER = 60

    def __init__(self, id, name, health, power):
        '''
        Initialise a putrid zombie.

        Args:
            id (int): Identifier of the undead.
            name (str): Name of the undead.
            health (int): Starting health of the undead.
            power (int): Starting power of the undead.
        '''
        super().__init__(id, name, health, power)
        self._clamp_stats()


class DeathKnight(WarriorUndead, CursedUndead):
    '''
    Models Death Knight undead

    Double inheritance from warrior and cursed undead.
    '''

    MIN_HEALTH = 30
    MAX_HEALTH = 200
    MIN_POWER = 30
    MAX_POWER = 160
    HEALTH_PER_LEVEL = 20
    POWER_PER_LEVEL = 10
    STARTING_HEALTH = 100
    STARTING_POWER = 80

    def __init__(self, id, name="Death Knight", health=None, power=None):
        super().__init__(
            id, name,
            self.STARTING_HEALTH if health is None else health,
            self.STARTING_POWER if power is None else power,
        )
        self._clamp_stats()

    def combat_style(self):
        return super().combat_style()

    def compare_combat_styles(self):
        return (f"{WarriorUndead.combat_style(self)} At the same time, "
                f"{CursedUndead.combat_style(self)}")

    def command(self):
        return super().command() + " Knight."


if __name__ == "__main__":

    death_knight = DeathKnight(5, "Death Knight")
    print(death_knight)

    # Test multiple inheritance
    print(isinstance(death_knight, WarriorUndead))
    print(isinstance(death_knight, CursedUndead))
    print(isinstance(death_knight, Undead))

    # MRO
    print(DeathKnight.mro())

    # Test combat_style()
    print(death_knight.combat_style())

    # Test explicit parent-class calls
    print(death_knight.compare_combat_styles())

    # Test inherited command() behaviour
    print(death_knight.command())

    # Test inherited level_up() behaviour
    death_knight.level_up()
    print(death_knight)

    # Level up several more times
    for _ in range(8):
        death_knight.level_up()

    print(death_knight)
