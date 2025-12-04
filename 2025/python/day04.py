from utils import get_data
from utils import parse_grid
from utils import timeit
from utils import DIRS_8


def count_neighbors(grid, point):
    return sum(1 for direction in DIRS_8 if grid.get(point + direction) is not None)


@timeit
def part_one(grid):
    return sum(1 for point in grid if grid[point] < 4)


@timeit
def part_two(grid):
    total_removed = 0
    prev_grid = grid
    while True:
        points = [key for key in grid if grid[key] < 4]
        if len(points) == 0:
            return total_removed

        total_removed += len(points)
        for point in points:
            del grid[point]
            for neighbor in DIRS_8:
                if grid.get(point + neighbor) is not None:
                    grid[point + neighbor] -= 1


@timeit
def main():
    data = get_data("04")
    grid = parse_grid(data, keep_values="@")
    grid = {key: count_neighbors(grid, key) for key in grid}

    p1_result = part_one(grid)
    print(p1_result)

    p2_result = part_two(grid)
    print(p2_result)
