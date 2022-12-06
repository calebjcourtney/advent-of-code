import re
from typing import List, Tuple, Set

from utils import get_line_data


def parse_line(line: str) -> Tuple[Set, Set]:
    s1, e1, s2, e2 = map(int, re.findall(r"\d+", line))
    sec1 = set([x for x in range(s1, e1 + 1)])
    sec2 = set([x for x in range(s2, e2 + 1)])
    return sec1, sec2


def part_one(data: List[Tuple[Set, Set]]) -> int:
    return sum(
        s1 >= s2 or s2 >= s1
        for (s1, s2) in data
    )


def part_two(data: List[Tuple[Set, Set]]) -> int:
    return sum(
        bool(s1 & s2)
        for (s1, s2) in data
    )


if __name__ == '__main__':
    data = get_line_data("04")
    data = [parse_line(line) for line in data]

    print(part_one(data))
    print(part_two(data))
