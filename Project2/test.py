from resource import Resource, ResourceManager
from ritual import SummoningRitual
from undead import Undead


def test_resource():
    print("Testing Resource...")

    resource = Resource(
        "Bone Runes",
        "Used for skeletal summons.",
        10
    )

    assert resource.name == "Bone Runes"
    assert resource.description == "Used for skeletal summons."
    assert resource.quantity == 10

    # Default quantity
    resource = Resource(
        "Bone Runes",
        "Used for skeletal summons."
    )

    assert resource.quantity == 0

    # Invalid quantity
    resource = Resource(
        "Bone Runes",
        "Used for skeletal summons.",
        -5
    )

    assert resource.quantity == 0

    # Add quantity
    resource.add_quantity(10)
    assert resource.quantity == 10

    resource.add_quantity(5)
    assert resource.quantity == 15

    # Subtract quantity
    resource.add_quantity(-5)
    assert resource.quantity == 10

    # Cannot become negative
    resource.add_quantity(-20)
    assert resource.quantity == 10

    # Invalid quantity
    resource.add_quantity(1.5)
    assert resource.quantity == 10

    # String
    result = str(resource)

    assert "Bone Runes" in result
    assert "10" in result
    assert "Used for skeletal summons." in result

    print("Resource tests passed.")


def test_resource_manager():
    print("Testing ResourceManager...")

    manager = ResourceManager(
        10,
        20,
        30,
        40,
        50
    )

    # Initial quantities
    assert manager.resources["necrotic_runes"].quantity == 10
    assert manager.resources["spirit_runes"].quantity == 20
    assert manager.resources["bone_runes"].quantity == 30
    assert manager.resources["flesh_runes"].quantity == 40
    assert manager.resources["ectoplasm"].quantity == 50

    # Collect using tuple
    manager.collect_resources(
        (1, 2, 3, 4, 5)
    )

    assert manager.resources["necrotic_runes"].quantity == 11
    assert manager.resources["spirit_runes"].quantity == 22
    assert manager.resources["bone_runes"].quantity == 33
    assert manager.resources["flesh_runes"].quantity == 44
    assert manager.resources["ectoplasm"].quantity == 55

    # Collect using dictionary
    manager.collect_resources({
        "bone_runes": 10,
        "ectoplasm": 5
    })

    assert manager.resources["bone_runes"].quantity == 43
    assert manager.resources["ectoplasm"].quantity == 60

    # Check sufficient resources
    assert manager.has_resources({
        "bone_runes": 20,
        "ectoplasm": 10
    }) is True

    # Check insufficient resources
    assert manager.has_resources({
        "bone_runes": 100
    }) is False

    # Spend resources
    result = manager.spend_resources({
        "bone_runes": 10,
        "ectoplasm": 5
    })

    assert result is True
    assert manager.resources["bone_runes"].quantity == 33
    assert manager.resources["ectoplasm"].quantity == 55

    # Insufficient resources should fail
    result = manager.spend_resources({
        "bone_runes": 100,
        "ectoplasm": 100
    })

    assert result is False

    # State must not change
    assert manager.resources["bone_runes"].quantity == 33
    assert manager.resources["ectoplasm"].quantity == 55

    # Invalid tuple length
    result = manager.has_resources((1, 2, 3))

    assert result is False

    # Invalid resource key
    result = manager.has_resources({
        "invalid_resource": 10
    })

    assert result is False

    # Invalid collection should not change state
    old_bone = manager.resources["bone_runes"].quantity

    manager.collect_resources({
        "bone_runes": 10,
        "invalid_resource": 5
    })

    assert manager.resources["bone_runes"].quantity == old_bone

    print("ResourceManager tests passed.")


def test_undead():
    print("Testing Undead...")

    undead = Undead(
        1,
        "Skeleton Warrior",
        50,
        30
    )

    # Initial state
    assert undead.id == 1
    assert undead.name == "Skeleton Warrior"
    assert undead.health == 50
    assert undead.power == 30
    assert undead.level == 1

    # Level up
    undead.level_up()

    assert undead.level == 2
    assert undead.health == 60
    assert undead.power == 35

    # Multiple level ups
    undead.level_up()
    undead.level_up()

    assert undead.level == 4
    assert undead.health == 80
    assert undead.power == 45

    # Health and power cannot exceed maximum
    undead = Undead(
        2,
        "Powerful Undead",
        95,
        98
    )

    undead.level_up()

    assert undead.health == Undead.MAX_HEALTH
    assert undead.power == Undead.MAX_POWER

    # Level cannot exceed maximum
    undead = Undead(
        3,
        "Skeleton",
        10,
        10
    )

    for _ in range(20):
        undead.level_up()

    assert undead.level == Undead.MAX_LEVEL

    # No changes after maximum level
    old_health = undead.health
    old_power = undead.power
    old_level = undead.level

    undead.level_up()

    assert undead.health == old_health
    assert undead.power == old_power
    assert undead.level == old_level

    # String
    result = str(undead)

    assert "3" in result
    assert "Skeleton" in result
    assert "Level" in result
    assert "Health" in result
    assert "Power" in result

    print("Undead tests passed.")


def test_ritual():
    print("Testing SummoningRitual...")

    ritual = SummoningRitual(
        "Skeleton Ritual",
        "Skeleton Warrior",
        50,
        30,
        {
            "necrotic_runes": 2,
            "spirit_runes": 1,
            "bone_runes": 5,
            "flesh_runes": 0,
            "ectoplasm": 3
        }
    )

    # Basic information
    assert ritual.name == "Skeleton Ritual"
    assert ritual.undead_name == "Skeleton Warrior"
    assert ritual.starting_health == 50
    assert ritual.starting_power == 30

    # Costs
    assert ritual.costs == {
        "necrotic_runes": 2,
        "spirit_runes": 1,
        "bone_runes": 5,
        "flesh_runes": 0,
        "ectoplasm": 3
    }

    # Can perform
    manager = ResourceManager(
        5,
        5,
        10,
        5,
        5
    )

    assert ritual.can_perform(manager) is True

    # Cannot perform when resources are insufficient
    manager = ResourceManager(
        5,
        5,
        2,
        5,
        5
    )

    assert ritual.can_perform(manager) is False

    # Invalid ResourceManager
    assert ritual.can_perform(None) is False
    assert ritual.can_perform("invalid") is False

    # Perform ritual
    manager = ResourceManager(
        5,
        5,
        10,
        5,
        5
    )

    result = ritual.perform(manager)

    assert result is True

    assert manager.resources["necrotic_runes"].quantity == 3
    assert manager.resources["spirit_runes"].quantity == 4
    assert manager.resources["bone_runes"].quantity == 5
    assert manager.resources["flesh_runes"].quantity == 5
    assert manager.resources["ectoplasm"].quantity == 2

    # Failed ritual should not consume anything
    manager = ResourceManager(
        5,
        5,
        2,
        5,
        5
    )

    result = ritual.perform(manager)

    assert result is False

    assert manager.resources["necrotic_runes"].quantity == 5
    assert manager.resources["spirit_runes"].quantity == 5
    assert manager.resources["bone_runes"].quantity == 2
    assert manager.resources["flesh_runes"].quantity == 5
    assert manager.resources["ectoplasm"].quantity == 5

    # Summon
    undead = ritual.summon(100)

    assert isinstance(undead, Undead)
    assert undead.id == 100
    assert undead.name == "Skeleton Warrior"
    assert undead.health == 50
    assert undead.power == 30
    assert undead.level == 1

    print("SummoningRitual tests passed.")


def run_tests():
    test_resource()
    test_resource_manager()
    test_undead()
    test_ritual()

    print()
    print("All tests passed!")


run_tests()