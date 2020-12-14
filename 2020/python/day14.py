from utils import get_line_data

import collections
from typing import List, Generator


def run_mask(value: int, mask: str) -> int:
    value |= int(mask.replace('X', '0'), 2)
    value &= int(mask.replace('X', '1'), 2)
    return value


def part_one(data: List[str]) -> int:
    mask = None
    memory = collections.defaultdict(int)
    for line in data:
        op, arg = line.split(' = ')

        if op == 'mask':
            mask = arg

        else:
            mem_pos = int(op[4:-1])
            memory[mem_pos] = run_mask(int(arg), mask)

    return sum(memory.values())


def run_masks(mem_pos: int, mask: str) -> Generator:
    if not mask:
        yield 0

    else:
        # yay recursion again
        for m in run_masks(mem_pos // 2, mask[:-1]):
            if mask[-1] == '0':
                yield 2 * m + mem_pos % 2
            elif mask[-1] == '1':
                yield 2 * m + 1
            elif mask[-1] == 'X':
                yield 2 * m + 0
                yield 2 * m + 1


def part_two(data: List[str]) -> int:
    mask = None
    memory = collections.defaultdict(int)
    for line in data:
        op, arg = line.split(' = ')

        if op == 'mask':
            mask = arg

        else:
            mem_pos = int(op[4:-1])

            # the only difference for part 2
            for m in run_masks(mem_pos, mask):
                memory[m] = int(arg)

    return sum(memory.values())


if __name__ == '__main__':
    data = get_line_data("14")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
