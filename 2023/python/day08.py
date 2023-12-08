from utils import get_data
from utils import timeit

import re
import math


def parse_data(data):
    instructions, directions = data.split("\n\n")
    directions = directions.split("\n")

    instructions = instructions.replace("L", "0").replace("R", "1")
    instructions = list(map(int, instructions))

    mapping = {}
    for line in directions:
        source, left, right = re.findall(r"(\w+) = \((\w+), (\w+)\)", line)[0]
        mapping[source] = (left, right)

    return instructions, mapping


def get_steps(instructions, mapping, starting_point="AAA", part_one=True):
    instruction_index = 0
    current = starting_point
    while True:
        current = mapping[current][instructions[instruction_index % len(instructions)]]
        instruction_index += 1

        if part_one and current == "ZZZ":
            break

        elif not part_one and current.endswith("Z"):
            break

    return instruction_index


@timeit
def part_one(instructions, mapping):
    return get_steps(instructions, mapping)


@timeit
def part_two(instructions, mapping):
    steps = []
    starting_points = [key for key in mapping.keys() if key.endswith("A")]
    for starting_point in starting_points:
        steps.append(get_steps(instructions, mapping, starting_point, part_one=False))

    return math.lcm(*steps)


if __name__ == '__main__':
    data = get_data("08")
    instructions, mapping = parse_data(data)

    print(part_one(instructions, mapping))

    p2_result = part_two(instructions, mapping)
    print(p2_result)
