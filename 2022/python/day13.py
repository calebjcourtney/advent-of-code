import json
from typing import List, Tuple, Any
from functools import cmp_to_key

from utils import get_data


def parse_data(data) -> List[Tuple[Any]]:
    output = []
    for pair in data.strip().split("\n\n"):
        p1, p2 = pair.split("\n")
        output.append((json.loads(p1), json.loads(p2)))

    return output


def compare_ints(p1: int, p2: int) -> int:
    if p1 < p2:
        return -1

    if p1 == p2:
        return 0

    return 1


def compare_lists(p1: list, p2: list) -> int:
    for s1, s2 in zip(p1, p2):
        c = compare(s1, s2)
        if c == -1:
            return -1

        if c == 1:
            return 1

    if len(p1) < len(p2):
        return -1

    if len(p1) > len(p2):
        return 1

    return 0


def compare(p1: Any, p2: Any) -> int:
    if isinstance(p1, int) and isinstance(p2, int):
        return compare_ints(p1, p2)

    if isinstance(p1, list) and isinstance(p2, list):
        return compare_lists(p1, p2)

    if isinstance(p1, int) and isinstance(p2, list):
        return compare_lists([p1], p2)

    if isinstance(p2, int) and isinstance(p1, list):
        return compare_lists(p1, [p2])


def part_two(data: List[Tuple[Any]]) -> int:
    flat_data = [[[2]], [[6]]]
    for p1, p2 in data:
        flat_data.append(p1)
        flat_data.append(p2)

    flat_data.sort(key=cmp_to_key(lambda p1, p2: compare(p1, p2)))
    output = 1
    for index, p in enumerate(flat_data, 1):
        if p == [[2]] or p == [[6]]:
            output *= index

    return output


if __name__ == '__main__':
    data = get_data("13")
    data = parse_data(data)

    print(sum(index for index, (p1, p2) in enumerate(data, 1) if compare(p1, p2) < 1))

    p2_result = part_two(data)
    print(p2_result)
