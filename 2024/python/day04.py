from utils import get_line_data
from utils import parse_grid
from utils import timeit
from utils import Point
from utils import DIRS_8
from utils import NE, SE


@timeit
def part_one(grid: dict[Point, str]):
    output = 0
    for p, value in grid.items():
        if value != "X":
            continue

        for direction in DIRS_8:
            if (
                grid.get(p + direction) == "M" and
                grid.get(p + direction * 2) == "A" and
                grid.get(p + direction * 3) == "S"
            ):
                output += 1

    return output


@timeit
def part_two(grid):
    output = 0

    for p, value in grid.items():
        if value != "A":
            continue

        if (
            {grid.get(p + NE), grid.get(p - NE)} == {"M", "S"} and
            {grid.get(p + SE), grid.get(p - SE)} == {"M", "S"}
        ):
            output += 1

    return output


if __name__ == '__main__':
    grid = parse_grid(get_line_data("04"))

    print(part_one(grid))
    print(part_two(grid))
