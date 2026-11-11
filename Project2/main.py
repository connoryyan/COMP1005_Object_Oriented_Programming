from necromancer import Necromancer
from ritual import SummoningRitual
from undead import (
    CursedUndead,
    DeathKnight,
    PhantomGuardian,
    PutridZombie,
    SkeletonWarrior,
    Undead,
    VengefulGhost,
    WarriorUndead
)


def main() -> None:
    """
    Demonstrate the connected necromancy summoning system.
    """

    necromancer = Necromancer(
        "Connor",
        necrotic_quant=10,
        spirit_quant=10,
        bone_quant=10,
        flesh_quant=10,
        ectoplasm_quant=10
    )

    skeleton_ritual = SummoningRitual(
        "Skeleton Ritual",
        "Undead Skeleton Warrior",
        50,
        30,
        {
            "necrotic_runes": 1,
            "spirit_runes": 1,
            "bone_runes": 5,
            "flesh_runes": 0,
            "ectoplasm": 2
        },
        summon_class=SkeletonWarrior
    )

    ghost_ritual = SummoningRitual(
        "Vengeful Ghost Ritual",
        "Vengeful Ghost",
        40,
        45,
        {
            "necrotic_runes": 2,
            "spirit_runes": 6,
            "bone_runes": 0,
            "flesh_runes": 0,
            "ectoplasm": 3
        },
        summon_class=VengefulGhost
    )

    zombie_ritual = SummoningRitual(
        "Putrid Zombie Ritual",
        "Putrid Zombie",
        70,
        25,
        {
            "necrotic_runes": 2,
            "spirit_runes": 0,
            "bone_runes": 2,
            "flesh_runes": 6,
            "ectoplasm": 3
        },
        summon_class=PutridZombie
    )

    guardian_ritual = SummoningRitual(
        "Phantom Guardian Ritual",
        "Phantom Guardian",
        90,
        70,
        {
            "necrotic_runes": 4,
            "spirit_runes": 5,
            "bone_runes": 3,
            "flesh_runes": 0,
            "ectoplasm": 6
        },
        summon_class=PhantomGuardian
    )

    print("=== Initial Necromancer ===")
    print(necromancer)

    print("\n=== Successful Summons ===")

    skeleton = necromancer.summon(skeleton_ritual)
    print(skeleton)

    ghost = necromancer.summon(ghost_ritual)
    print(ghost)

    zombie = necromancer.summon(zombie_ritual)
    print(zombie)

    print("\n=== Attempting Phantom Guardian ===")

    guardian = necromancer.summon(guardian_ritual)

    if guardian is None:
        print("Phantom Guardian could not be summoned.")
    else:
        print(guardian)

    print("\n=== Collecting More Resources ===")

    necromancer.resources.collect_resources({
        "necrotic_runes": 5,
        "spirit_runes": 5,
        "bone_runes": 5,
        "flesh_runes": 5,
        "ectoplasm": 5
    })

    print(necromancer.resources)

    print("\n=== Attempting Phantom Guardian Again ===")

    guardian = necromancer.summon(guardian_ritual)

    if guardian is None:
        print("Phantom Guardian could not be summoned.")
    else:
        print(guardian)

    print("\n=== Specialised Undead Hierarchy ===")

    print("Summon class declared by each ritual:")

    for ritual in (skeleton_ritual, ghost_ritual, zombie_ritual,
                   guardian_ritual):
        print(f"  {ritual.name}: {ritual.summon_class.__name__}")

    print("\nSummoned undead and their behaviour:")

    for undead in (skeleton, ghost, zombie, guardian):
        if undead is None:
            continue

        print(f"\n{undead}")
        print(f"  class: {type(undead).__name__}")
        print(f"  isinstance Undead: {isinstance(undead, Undead)}")
        print(f"  isinstance WarriorUndead: "
              f"{isinstance(undead, WarriorUndead)}")
        print(f"  isinstance CursedUndead: "
              f"{isinstance(undead, CursedUndead)}")
        print(f"  stat limits: health {undead.MIN_HEALTH}-"
              f"{undead.MAX_HEALTH}, power {undead.MIN_POWER}-"
              f"{undead.MAX_POWER}")
        print(f"  command(): {undead.command()}")

    print("\nLevelling a summon with the inherited level_up():")

    if guardian is not None:
        print(f"  before: {guardian}")

        necromancer.level_up(guardian.id)
        necromancer.level_up(guardian.id)

        print(f"  after:  {guardian}")

    print("\n=== Level Up ===")

    if skeleton is not None:
        print("Before:")
        print(skeleton)

        necromancer.level_up(skeleton.id)

        print("After:")
        print(skeleton)

    print("\n=== Dismiss Undead ===")

    if ghost is not None:
        print(f"Dismissing undead with ID {ghost.id}...")

        success = necromancer.dismiss(ghost.id)

        print(f"Dismiss successful: {success}")

    print("\n=== Death Knight: Multiple Inheritance ===")
    necromancer.resources.collect_resources((20, 20, 20, 20, 20))
    death_ritual = SummoningRitual(
        "Death Knight Ritual", "Death Knight",
        DeathKnight.STARTING_HEALTH, DeathKnight.STARTING_POWER,
        (8, 8, 8, 8, 8), summon_class=DeathKnight,
    )
    knight = necromancer.summon(death_ritual)
    assert isinstance(knight, DeathKnight)
    assert isinstance(knight, WarriorUndead)
    assert isinstance(knight, CursedUndead)
    assert isinstance(knight, Undead)
    print(knight)
    print("MRO:", [cls.__name__ for cls in DeathKnight.mro()])
    print(knight.combat_style())
    print(knight.compare_combat_styles())
    print(necromancer.command(knight.id))
    assert necromancer.level_up(knight.id)
    print("After levelling:", knight)

    print("\n=== Final Necromancer ===")
    print(necromancer)


if __name__ == "__main__":
    main()
