from utils import get_line_data

from collections import Counter
from itertools import combinations_with_replacement
import re


def parse_line(line):
    p = re.match(
        r"(?P<name>\w+): capacity (?P<capacity>-?\d+), durability (?P<durability>-?\d+), flavor (?P<flavor>-?\d+), texture (?P<texture>-?\d+), calories (?P<calories>-?\d+)",
        line
    )

    return p.groupdict()["name"], {key: int(value) for key, value in p.groupdict().items() if key != "name"}


def parse_data(data):
    output = {}
    for line in data:
        name, info = parse_line(line)
        output[name] = info

    return output


def p1_calculate(combo, data):
    total_score = 1
    for prop in ["capacity", "durability", "flavor", "texture"]:
        prop_score = 0
        for key, value in combo.items():
            prop_score += value * data[key][prop]

        if prop_score <= 0:
            return 0

        total_score *= prop_score

    return total_score


def part_one(data):
    names = list(data.keys())
    best_score = 0
    for combo in combinations_with_replacement(names, 100):
        c = Counter(combo)
        if len(c) != len(names):
            continue

        score = p1_calculate(c, data)

        if score > best_score:
            best_score = score

    return best_score


def check_calories(combo, data):
    calories = sum([value * data[key]["calories"] for key, value in combo.items()])
    return calories == 500


def part_two(data):
    names = list(data.keys())
    best_score = 0
    for combo in combinations_with_replacement(names, 100):
        c = Counter(combo)
        if not check_calories(c, data):
            continue

        score = p1_calculate(c, data)

        if score > best_score:
            best_score = score

    return best_score


if __name__ == '__main__':
    data = get_line_data("15")
    data = parse_data(data)

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
