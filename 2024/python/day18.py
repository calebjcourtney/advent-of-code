from utils import get_data
from utils import get_line_data
from utils import parse_grid
from utils import timeit
from utils import get_nums
from utils import Point
from utils import DIRS

from collections import deque


def build_grid():
    grid = {}
    for x in range(71):
        for y in range(71):
            grid[Point(x, y)] = "."

    return grid


def solve(data):
    grid = build_grid()
    for point in data:
        grid[point] = "#"

    end_point = Point(70, 70)

    steps: dict[Point, int] = {Point(0, 0): 0}

    queue = deque([Point(0, 0)])
    while queue:
        current = queue.popleft()
        if current == end_point:
            return steps[current]

        for direction in DIRS:
            new_point = current + direction
            if new_point not in grid or grid[new_point] == "#":
                continue

            if new_point not in steps or steps[new_point] > steps[current] + 1:
                steps[new_point] = steps[current] + 1
                queue.append(new_point)

    return steps[end_point]


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
