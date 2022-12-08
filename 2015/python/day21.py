from typing import List
from itertools import combinations

from utils import get_data, get_nums


class Equipment:
    def __init__(self, cost, damage, armor):
        self.cost = cost
        self.damage = damage
        self.armor = armor


class Character:
    def __init__(self, health, damage, armor, equipment=[]):
        self.health: int = health
        self.damage: int = damage
        self.armor: int = armor
        self.equipment: List[Equipment] = equipment

    def total_damage(self) -> int:
        return sum([x.damage for x in self.equipment]) + self.damage

    def total_armor(self) -> int:
        return sum([x.armor for x in self.equipment]) + self.armor


WEAPONS = [Equipment(8, 4, 0), Equipment(10, 5, 0), Equipment(25, 6, 0), Equipment(40, 7, 0), Equipment(74, 8, 0)]
ARMOR = [Equipment(0, 0, 0), Equipment(13, 0, 1), Equipment(31, 0, 2), Equipment(53, 0, 3), Equipment(75, 0, 4), Equipment(102, 0, 5)]
RINGS = [Equipment(0, 0, 0), Equipment(25, 1, 0), Equipment(50, 2, 0), Equipment(100, 3, 0), Equipment(20, 0, 1), Equipment(40, 0, 2), Equipment(80, 0, 3)]


def success(hero, boss) -> bool:
    hero_damage = max(1, hero.total_damage() - boss.total_armor())
    boss_dmg = max(1, boss.total_damage() - hero.total_armor())
    rounds_to_kill_boss = (hero.health // boss_dmg) + (1 if hero.health % boss_dmg != 0 else 0)

    return boss.health <= hero_damage * rounds_to_kill_boss


def data_to_character(data) -> Character:
    health, damage, armor = get_nums(data)
    return Character(health, damage, armor)


def part_one(data) -> int:
    success_total = 1e9
    for weapon in WEAPONS:
        for armor in ARMOR:
            for r1, r2 in combinations(RINGS, 2):
                items_cost = sum(item.cost for item in [weapon, armor, r1, r2])
                boss = data_to_character(data)
                hero = Character(
                    health=100,
                    damage=0,
                    armor=0,
                    equipment=[
                        weapon, armor, r1, r2
                    ]
                )

                if success(hero, boss) and items_cost < success_total:
                    success_total = items_cost

    return success_total


def part_two(data) -> int:
    success_total = 0
    for weapon in WEAPONS:
        for armor in ARMOR:
            for r1, r2 in combinations(RINGS, 2):
                items_cost = sum(item.cost for item in [weapon, armor, r1, r2])
                boss = data_to_character(data)
                hero = Character(health=100, damage=0, armor=0, equipment=[weapon, armor, r1, r2])

                if not success(hero, boss) and items_cost > success_total:
                    success_total = items_cost

    return success_total


if __name__ == '__main__':
    data = get_data("21")

    print(part_one(data))
    print(part_two(data))
