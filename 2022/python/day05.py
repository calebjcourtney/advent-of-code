from typing import Tuple
import re

from utils import get_data


def parse_crate_from_line(line: str):
    results = re.findall(r'\[(\w|\s)\]', line)
    return [
        x.strip("[").strip("]")
        for x in results
    ]


def build_stacks(stack_data):
    stacks = {k: Stack([]) for k in range(1, 10)}
    for line in stack_data.split("\n"):
        crates = parse_crate_from_line(line)
        for index, crate in enumerate(crates, 1):
            if crate == " ":
                continue
            stacks[index].insert(crate)

    return stacks


def parse_instructions(line: str) -> Tuple[int, int, int]:
    results = re.findall(r'\d+', line)
    return tuple(map(int, results))


class Stack(object):
    def __init__(self, crates):
        self.crates = crates

    def add(self, c: list):
        self.crates += c

    def insert(self, c: str):
        self.crates = [c] + self.crates

    def drop(self, c: int):
        out = self.crates[-c:]
        self.crates = self.crates[:-c]
        return out

    def top(self):
        return self.crates[-1]


def part_one(stacks, instructions):
    for line in instructions.split("\n"):
        count, source, target = parse_instructions(line)

        crates = stacks[source].drop(count)
        crates = crates[::-1]
        stacks[target].add(crates)

    return "".join(stacks[i].top() for i in range(1, len(stacks) + 1))


def part_two(stacks, instructions):
    for line in instructions.split("\n"):
        count, source, target = parse_instructions(line)

        crates = stacks[source].drop(count)
        stacks[target].add(crates)

    return "".join(stacks[i].top() for i in range(1, len(stacks) + 1))


if __name__ == '__main__':
    data = get_data("05")

    stack_data, instructions = data.split("\n\n")
    stacks = build_stacks(stack_data)

    p1_result = part_one(stacks, instructions)
    print(p1_result)

    stacks = build_stacks(stack_data)
    p2_result = part_two(stacks, instructions)
    print(p2_result)
