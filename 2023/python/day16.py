from utils import get_line_data
from utils import timeit
from utils import parse_grid
from utils import Point

from utils import N as S
from utils import S as N
from utils import E, W
from utils import min_max_xy

from collections import deque
from typing import NamedTuple


MAPPING = {
    N: {"-": [W, E], "|": [N], "/": [E], "\\": [W], ".": [N]},
    S: {"-": [W, E], "|": [S], "/": [W], "\\": [E], ".": [S]},
    E: {"-": [E], "|": [N, S], "/": [N], "\\": [S], ".": [E]},
    W: {"-": [W], "|": [N, S], "/": [S], "\\": [N], ".": [W]},
}


class Beam(NamedTuple):
    location: Point
    direction: Point


def get_energized_tiles(start, direction, grid):
    beam = Beam(start, direction)
    beams_visited = set()

    stack = deque([beam])
    while stack:
        beam = stack.popleft()
        if beam in beams_visited:
            continue

        cur_val = grid.get(beam.location)
        if cur_val is None:
            continue

        beams_visited.add(beam)

        for next_direction in MAPPING[beam.direction][cur_val]:
            stack.append(Beam(beam.location + next_direction, next_direction))

    return len(set([b.location for b in beams_visited]))


@timeit
def part_one(data):
    return get_energized_tiles(Point(0, 0), E, data)


@timeit
def part_two(data):
    min_x, max_x, min_y, max_y = min_max_xy(data)
    possible_starting_points = []
    for x in range(min_x, max_x + 1):
        possible_starting_points.append((Point(x, min_y), S))
        possible_starting_points.append((Point(x, max_y), N))

    for y in range(min_y, max_y + 1):
        possible_starting_points.append((Point(min_x, y), E))
        possible_starting_points.append((Point(max_x, y), W))

    for direction in (N, S, E, W):
        for point in (
            Point(min_x, min_y),
            Point(min_x, max_y),
            Point(max_x, min_y),
            Point(max_x, max_y),
        ):
            possible_starting_points.append((point, direction))

    return max([get_energized_tiles(*p, data) for p in possible_starting_points])


if __name__ == "__main__":
    aoc_data = get_line_data("16")
    aoc_grid = parse_grid(aoc_data)

    p1_result = part_one(aoc_grid)
    print(p1_result)

    p2_result = part_two(aoc_grid)
    print(p2_result)
