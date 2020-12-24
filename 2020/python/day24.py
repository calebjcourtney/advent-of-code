from utils import get_line_data

import re
from collections import defaultdict

from typing import List, Tuple


DIRECTIONS = {
    'e': (1, 0),
    'se': (0, -1),
    'sw': (-1, -1),
    'w': (-1, 0),
    'nw': (0, 1),
    'ne': (1, 1),
}


def parse_directions(line: str) -> Tuple[int, int]:
    matches = re.findall('e|se|sw|w|nw|ne', line)
    x, y = 0, 0

    for match in matches:
        coord = DIRECTIONS[match]

        x += coord[0]
        y += coord[1]

    return (x, y)


def parse_layout(data: List[str]) -> defaultdict:
    layout = defaultdict(int)
    for line in data:
        x, y = parse_directions(line)

        layout[(x, y)] += 1

    return layout


def part_one(data: List[str]) -> int:
    layout = parse_layout(data)
    return sum(flip_count % 2 for flip_count in layout.values())


class Floor:
    def __init__(self, layout: defaultdict):
        self.layout = layout

    def run_day(self):
        adjacent_blacks = defaultdict(int)

        for point, value in self.layout.items():
            if value % 2 == 0:
                continue

            adjacents = [
                (1, 0),
                (0, 1),
                (0, -1),
                (-1, 0),
                (-1, -1),
                (1, 1)
            ]

            for adj in adjacents:
                nearby_point = (point[0] + adj[0], point[1] + adj[1])
                adjacent_blacks[nearby_point] += 1

        new_layout = {}
        for point, value in self.layout.items():
            if value % 2 == 1:
                if adjacent_blacks.get(point, 0) not in [1, 2]:
                    pass

                else:
                    new_layout[point] = 1

        for point, value in adjacent_blacks.items():
            if value == 2 and self.layout.get(point, 0) % 2 == 0:
                new_layout[point] = 1

        self.layout = new_layout


def part_two(data: List[str]) -> int:
    layout = parse_layout(data)
    floor = Floor(layout)

    for _ in range(100):
        floor.run_day()

    return sum(1 for value in floor.layout.values() if value % 2 == 1)


if __name__ == '__main__':
    data = get_line_data("24")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
