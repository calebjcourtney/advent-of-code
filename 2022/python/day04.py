from typing import List, Tuple

from utils import get_line_data


class Section():
    def __init__(self, arg: str):
        self.start, self.end = map(int, arg.split("-"))
        self.seats = set([x for x in range(self.start, self.end + 1)])


def parse_line(line: str) -> Tuple[Section, Section]:
    s1, s2 = map(Section, line.split(","))
    return s1, s2


def part_one(data: List[Tuple[Section, Section]]) -> int:
    return sum(
        s1.seats >= s2.seats or s2.seats >= s1.seats
        for (s1, s2) in data
    )


def part_two(s1: Section, s2: Section) -> int:
    return sum(
        bool(s1.seats & s2.seats)
        for (s1, s2) in data
    )


if __name__ == '__main__':
    data = get_line_data("04")
    data = [parse_line(line) for line in data]

    print(part_one(data))
    print(part_two(data))
