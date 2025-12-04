from utils import get_data
from utils import parse_grid
from utils import timeit
from utils import Point
from utils import DIRS_8

import numpy
import itertools
import collections
import re


@timeit
def part_one(grid):
    total = 0
    for point in grid.keys():
        count = 0
        for neighbor in DIRS_8:
            if grid.get(point + neighbor) and grid[point + neighbor] == "@":
                count += 1

        if count < 4:
            total += 1

    return total


@timeit
def part_two(grid):
    total = 0
    changed = True
    while changed:
        changed = False
        for point in grid.keys():
            count = 0
            for neighbor in DIRS_8:
                if grid.get(point + neighbor) and grid[point + neighbor] == "@":
                    count += 1

            if count < 4:
                total += 1
                changed = True
                grid[point] = "."
        
        grid = {key: value for key, value in grid.items() if value == "@"}

    return total


@timeit
def main():
    data = get_data("04")
#     data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""
    grid = parse_grid(data)
    grid = {key: value for key, value in grid.items() if value == "@"}

    p1_result = part_one(grid)
    print(p1_result)

    p2_result = part_two(grid)
    print(p2_result)
