"""Regression tests for summoning, ownership and multiple inheritance."""

import pytest

from Project2.test import (
    test_resource, test_resource_manager, test_undead,
    test_undead_hierarchy, test_ritual,
)
from necromancer import Necromancer
from resource import ResourceManager
from ritual import SummoningRitual
from undead import DeathKnight, WarriorUndead, CursedUndead, Undead


@pytest.fixture
def necromancer():
    return Necromancer("Test", 100, 100, 100, 100, 100)


@pytest.fixture
def ritual():
    return SummoningRitual("Knight", "Death Knight", 100, 80,
                           (8, 8, 8, 8, 8), DeathKnight)


def quantities(necromancer):
    return {key: resource.quantity for key, resource
            in necromancer.resources.resources.items()}


def test_death_knight_lifecycle(necromancer, ritual):
    before = quantities(necromancer)
    knight = necromancer.summon(ritual)
    assert isinstance(knight, (DeathKnight,))
    assert isinstance(knight, WarriorUndead)
    assert isinstance(knight, CursedUndead)
    assert isinstance(knight, Undead)
    assert quantities(necromancer) == {k: v - 8 for k, v in before.items()}
    assert (knight.level, knight.health, knight.power) == (1, 100, 80)
    assert knight.combat_style() == WarriorUndead.combat_style(knight)
    assert CursedUndead.combat_style(knight) in knight.compare_combat_styles()
    assert "awaits your command" in necromancer.command(knight.id)
    assert DeathKnight.mro().count(Undead) == 1
    for _ in range(20):
        assert necromancer.level_up(knight.id)
    assert knight.level == knight.MAX_LEVEL
    assert knight.health == knight.MAX_HEALTH
    assert knight.power == knight.MAX_POWER
    external = necromancer.undead
    external.clear()
    assert len(necromancer.undead) == 1
    assert necromancer.dismiss(knight.id)
    assert not necromancer.dismiss(knight.id)
    assert not necromancer.level_up(knight.id)
    assert necromancer.command(knight.id) is None
    assert necromancer.summon(ritual).id == 2


def test_failed_summons_preserve_resources(necromancer, ritual):
    before = quantities(necromancer)
    assert necromancer.summon(None) is None
    empty = Necromancer("Empty")
    assert empty.summon(ritual) is None
    for _ in range(necromancer.MAX_UNDEAD):
        assert necromancer.summon(ritual) is not None
    full = quantities(necromancer)
    assert necromancer.summon(ritual) is None
    assert quantities(necromancer) == full
    assert before != full


def test_factory_failure_does_not_spend(necromancer, ritual, monkeypatch):
    def broken_factory(identifier):
        raise TypeError("Unsupported summon constructor")
    before = quantities(necromancer)
    monkeypatch.setattr(ritual, "create_summon", broken_factory)
    assert necromancer.summon(ritual) is None
    assert quantities(necromancer) == before
    assert necromancer.undead == []


def test_partial_costs_require_ectoplasm():
    ritual = SummoningRitual("Partial", "Undead", 10, 10,
                             {"bone_runes": 2})
    assert ritual.costs["ectoplasm"] > 0
    assert set(ritual.costs) == set(ResourceManager.KEYS)
    assert not ritual.can_perform(ResourceManager())


def test_invalid_resource_operations_are_atomic():
    from resource import Resource
    resource = Resource(None, None, -1)
    assert resource.quantity == 0
    manager = ResourceManager(1, 1, 1, 1, 1)
    assert not manager.has_resources(None)
    assert not manager.spend_resources(None)
    assert manager.resources["ectoplasm"].quantity == 1
    manager.collect_resources(None)
    assert manager.resources["ectoplasm"].quantity == 1


def test_invalid_ritual_data_and_concrete_stat_limits():
    ritual = SummoningRitual(None, None, -1, -1, None)
    summon = ritual.create_summon(1)
    assert summon.health == Undead.MIN_HEALTH
    assert summon.power == Undead.MIN_POWER
    strong = SummoningRitual("Strong", "Knight", 150, 120,
                             {"ectoplasm": 1}, DeathKnight)
    knight = strong.create_summon(2)
    assert knight.health == 150
    assert knight.power == 120


def test_factory_invalid_result_and_spending_failure(
        necromancer, ritual, monkeypatch):
    before = quantities(necromancer)
    factory = ritual.create_summon
    monkeypatch.setattr(ritual, "create_summon", lambda identifier: None)
    assert necromancer.summon(ritual) is None
    monkeypatch.setattr(ritual, "create_summon", factory)
    monkeypatch.setattr(ritual, "perform", lambda resources: False)
    assert necromancer.summon(ritual) is None
    assert quantities(necromancer) == before
    assert necromancer.undead == []


def test_necromancer_demonstration(capsys):
    from Project2.main import main
    main()
    output = capsys.readouterr().out
    assert "Death Knight" in output
    assert "MRO:" in output
    unnamed = Necromancer(None)
    assert unnamed.name == "Unknown"
    assert "Unknown" in str(unnamed)
