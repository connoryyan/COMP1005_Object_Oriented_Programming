from necromancer import Necromancer
from ritual import SummoningRitual


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
        }
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
        }
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
        }
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
        }
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

    print("\n=== Final Necromancer ===")
    print(necromancer)


if __name__ == "__main__":
    main()