from utils import get_data
from utils import parse_grid
from utils import timeit
from utils import DIRS_8


def count_neighbors(grid, point):
    return sum(1 for direction in DIRS_8 if grid.get(point + direction) is not None)


@timeit
def part_one(grid):
    total = 0
    for point in grid:
        neighbor_count = count_neighbors(grid, point)
        if neighbor_count < 4:
            total += 1

    return total


@timeit
def part_two(grid):
    total_removed = 0
    changed = True

    while changed:
        changed = False
        for point in grid:
            neighbor_count = count_neighbors(grid, point)
            if neighbor_count < 4:
                grid[point] = None
                total_removed += 1
                changed = True

        grid = {key: value for key, value in grid.items() if value}

    return total_removed


@timeit
def main():
    data = get_data("04")
    grid = parse_grid(data, keep_values="@")

    p1_result = part_one(grid)
    print(p1_result)

    p2_result = part_two(grid)
    print(p2_result)
