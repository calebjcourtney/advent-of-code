from utils import get_line_data
from utils import timeit
from utils import get_nums
from utils import Point
from utils import DIRS
from utils import get_distances

from collections import deque


def build_grid(data):
    grid = {}
    for x in range(71):
        for y in range(71):
            if Point(x, y) in data:
                continue

            grid[Point(x, y)] = "."

    return grid


def solve(data):
    grid = build_grid(data)
    end_point = Point(70, 70)
    distances = get_distances(grid, Point(0, 0))

    return distances[Point(70, 70)]


@timeit
def part_one(data):
    return solve(data[:1024])


def binary_search(arr: list[Point], low: int, high: int) -> Point:
    if high == low:
        return arr[low - 1]

    while high > low:
        mid = (high + low) // 2

        try:
            solve(arr[:mid])
        except KeyError:
            high = mid - 1
        else:
            low = mid + 1

    return arr[low - 1]


@timeit
def part_two(data):
    p = binary_search(data, 1024, len(data))
    return f"{p.x},{p.y}"


if __name__ == '__main__':
    data = get_line_data("18")
    data = [Point(*get_nums(line)) for line in data]

    print(part_one(data))
    print(part_two(data))
