from utils import get_data
from collections import defaultdict
from typing import List, Set, Dict

from utils import (
    Point,
    N, S, E, W,
    NW, NE, SW, SE,
    parse_grid
)


CHECK_DIRECTIONS = [
    [[S, SE, SW], S],
    [[N, NE, NW], N],
    [[W, NW, SW], W],
    [[E, NE, SE], E],
]


def parse_data(data: str) -> Set[Point]:
    full_grid = parse_grid(data)
    grid = set([point for point, value in full_grid.items() if value == "#"])

    return grid


def min_max_xy(points: List[Point]):
    if len(points) == 0:
        return None, None, None, None

    return (
        min(p.x for p in points),
        max(p.x for p in points),
        min(p.y for p in points),
        max(p.y for p in points),
    )


def count_empty_spaces(board):
    min_x, max_x, min_y, max_y = min_max_xy(board)
    blanks = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            p = Point(x, y)
            if p not in board:
                blanks += 1

    return blanks


def combined(grid):
    for i in range(100000):
        elf_proposals: Dict[Point, List] = defaultdict(list)
        for point in grid:
            # no other Elves are in one of those eight positions
            if not any(n in grid for n in point.neighbors_8()):
                continue

            # the Elf looks in each of four directions
            for d in range(4):
                checks, direction = CHECK_DIRECTIONS[(i + d) % len(CHECK_DIRECTIONS)]
                if any(c in grid for c in checks):
                    continue

                elf_proposals[point + direction].append(point)
                break

        # only one elf wants to move to the location
        for new_loc, elf_moves in elf_proposals.items():
            if len(elf_moves) == 1:
                grid.remove(elf_moves[0])
                grid.add(new_loc)

        # part one
        if i == 9:
            p1 = count_empty_spaces(grid)
            print(p1)

        # part two
        if len(elf_proposals) == 0:
            return p1, i + 1


if __name__ == '__main__':
    data = get_data("23")

    grid = parse_data(data)
    p1, p2 = combined(grid)

    print(p1)
    print(p2)
