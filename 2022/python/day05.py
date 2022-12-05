from typing import Dict, List, Tuple
import re

from utils import get_data


def parse_crate_from_line(line: str) -> List[str]:
    results = re.findall(r'\[(\w|\s)\]', line)
    return [
        x.strip("[").strip("]")
        for x in results
    ]


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


def build_stacks(stack_data) -> Dict[int, Stack]:
    stacks = {k: Stack([]) for k in range(1, 10)}
    for line in stack_data.split("\n"):
        crates = parse_crate_from_line(line)
        for index, crate in enumerate(crates, 1):
            if crate == " ":
                continue
            stacks[index].insert(crate)

    return stacks


def part_one(stacks: Dict[int, Stack], instructions: str) -> str:
    for (count, source, target) in instructions:
        crates = stacks[source].drop(count)
        crates = crates[::-1]
        stacks[target].add(crates)

    return "".join(stacks[i].top() for i in range(1, len(stacks) + 1))


def part_two(stacks: Dict[int, Stack], instructions: Tuple[int, int, int]) -> str:
    for (count, source, target) in instructions:
        crates = stacks[source].drop(count)
        stacks[target].add(crates)

    return "".join(stacks[i].top() for i in range(1, len(stacks) + 1))


if __name__ == '__main__':
    data = get_data("05")

    stack_data, instructions = data.split("\n\n")
    instructions = [parse_instructions(line) for line in instructions.split("\n")]
    stacks = build_stacks(stack_data)

    p1_result = part_one(stacks, instructions)
    print(p1_result)

    stacks = build_stacks(stack_data)
    p2_result = part_two(stacks, instructions)
    print(p2_result)
