import math
import os
import re
import time
from collections import deque
from numbers import Number
from pathlib import Path
from typing import Any, Callable, Generator, List, NamedTuple, Tuple

import numpy as np
from aocd.models import Puzzle
from more_itertools import windowed
from numpy import ones, vstack
from numpy.linalg import lstsq

YEAR = int(Path.cwd().parent.name)


def get_data(day: str) -> str:
    input_dir = "/".join(os.getcwd().split("/")[:-1])
    try:
        data = open("{}/inputs/input{}.txt".format(input_dir, day), "r").read().rstrip()
    except FileNotFoundError:
        puzzle = Puzzle(year=YEAR, day=int(day))
        with open("{}/inputs/input{}.txt".format(input_dir, day), "w+") as saveFile:
            saveFile.write(puzzle.input_data)

        data = open("{}/inputs/input{}.txt".format(input_dir, day), "r").read().rstrip()

    return data


def get_line_data(day: str):
    data = get_data(day)
    return [x for x in data.split("\n") if x != ""]


def get_int_data(day: str):
    data = get_line_data(day)
    return list(map(int, data))


def re_split(val: str, chars: str) -> list:
    # splits along any of the chars provided in the list
    return re.split("[{}]".format(chars), val)


def special_split(line: str, patterns: List[str]) -> List[str]:
    # splits along any of the patters provided in the list
    return re.split("|".join(patterns), line)


def add_vector(point: Tuple[int], vector: Tuple[int]) -> Tuple[int]:
    return tuple(x + y for x, y in zip(point, vector))


def find_corresponding_chars(line: str, start: str, end: str) -> List[Tuple[int, int]]:
    # finds matching figures in a string and returns the indices
    stack = []
    parentheses_locs = []
    for index, character in enumerate(line):
        if character == start:
            stack.append(index)
        elif character == end:
            parentheses_locs.append((stack.pop(), index))

    return parentheses_locs


def find_parentheses(line: str) -> List[Tuple[int, int]]:
    return find_corresponding_chars(line, "(", ")")


def nwise(iterable, n=2):
    return windowed(iterable, n)


# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def array_left_rotate(lst, n=1):
    if isinstance(lst, list):
        return lst[n:] + lst[:n]

    raise ValueError("if you're using a deque, use the .rotate() method")


def array_right_rotate(lst, n=1):
    if isinstance(lst, list):
        return lst[-n:] + lst[:-n]

    raise ValueError("if you're using a deque, use the .rotate() method")


def rotate_text(text: str) -> str:
    """
    Assuming a multi-line, rectangular blob of text, rotate 90 degrees
    """
    # each row is the same length
    rows = [line for line in text.split("\n")]
    max_row = max([len(x) for x in rows])
    for row in rows:
        assert len(row) == max_row

    row_count = len(text.split("\n"))
    col_count = len(text.split("\n")[0])

    output = []
    for c in range(col_count):
        temp = ""
        for r in range(row_count):
            temp += rows[r][c]

    return "\n".join(output)


def get_nums(line, signed=True, num_type=int):
    # gets all the numbers in a line of text
    pattern = re.compile(r"-?\d+") if signed else re.compile(r"\d+")
    return list(map(num_type, pattern.findall(line)))


def mult(lst: list):
    return math.prod(lst)


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __div__(self, n):
        return Point(self.x / n, self.y / n)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    @property
    def neighbors(self):
        return [self + p for p in DIRS]

    @property
    def neighbors_8(self):
        return [self + p for p in DIRS_8]


N = Point(0, 1)
NE = Point(1, 1)
E = Point(1, 0)
SE = Point(1, -1)
S = Point(0, -1)
SW = Point(-1, -1)
W = Point(-1, 0)
NW = Point(-1, 1)


DIRS = [N, S, E, W]
DIRS_8 = [N, NE, E, SE, S, SW, W, NW]


def parse_grid(data, keep_values: list[any] | str | None = None):
    # convert the data to a grid format
    grid = {}
    if isinstance(data, list):
        for y in range(len(data)):
            for x in range(len(data[y])):
                grid[Point(x, y)] = data[y][x]

    elif isinstance(data, str) and "\n" in data:
        lines = data.split("\n")
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                grid[Point(x, y)] = lines[y][x]

    if keep_values is not None:
        grid = {k: v for k, v in grid.items() if v in keep_values}

    return grid


def iterate_grid(grid: dict[Point, Any]) -> Generator[Point, None, None]:
    # iterate over values in the grid in ascending order of row and column
    for point in sorted(grid.keys(), key=lambda p: (p.y, p.x)):
        yield point


def print_grid(grid: dict[Point, str], fill: str = None) -> None:
    min_x, max_x, min_y, max_y = min_max_xy(grid.keys())

    output = ""

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if Point(x, y) not in grid and fill is not None:
                print(fill, end="")
                output += fill
            else:
                print(grid[Point(x, y)], end="")
                output += grid[Point(x, y)]
        print()
        output += "\n"

    return output.strip()


def grid_rotate_row_right(grid: dict[Point, Any], row: int, count: int):
    pairs = [(key, value) for key, value in grid.items() if key.y == row]
    pairs.sort(key=lambda x: x[0].x)

    values = [v for _, v in pairs]
    values = array_right_rotate(values, count)

    for i in range(len(values)):
        grid[pairs[i][0]] = values[i]

    return grid


def grid_rotate_column_down(grid: dict[Point, Any], col: int, count: int):
    pairs = [(key, value) for key, value in grid.items() if key.x == col]
    pairs.sort(key=lambda x: x[0].y)

    values = [v for _, v in pairs]
    values = array_right_rotate(values, count)

    for i in range(len(values)):
        grid[pairs[i][0]] = values[i]

    return grid


def points_between(p1, p2):
    # points in a straight line between two different points
    assert p1.x == p2.x or p1.y == p2.y

    output = {p1, p2}
    if p1.x != p2.x:
        step = (p1.x - p2.x) // abs(p1.x - p2.x)
        for x in range(p1.x, p2.x, step):
            output.add(Point(x, p1.y))

    if p1.y != p2.y:
        step = (p1.y - p2.y) // abs(p1.y - p2.y)
        for y in range(p1.y, p2.y, step):
            output.add(Point(p1.x, y))

    return output


def manhattan(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def euclidean_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def max_row_col(p1, p2):
    return max(abs(p1.x - p2.x), abs(p1.y - p2.y))


def surrounding_points(center, distance, func=manhattan):
    output = set()
    for x in range(center.x - distance, center.x + distance + 1):
        for y in range(center.y - distance, center.y + distance + 1):
            if func(center, Point(x, y)) <= distance:
                output.add(Point(x, y))

    return output


def get_line(p1: Point, p2: Point) -> Tuple[Number, Number]:
    x_coords = p1.x, p2.x
    y_coords = p1.y, p2.y

    A = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords, rcond=None)[0]
    return m, c


def min_max_xy(points: List[Point]):
    if len(points) == 0:
        return None, None, None, None

    return (
        min(p.x for p in points),
        max(p.x for p in points),
        min(p.y for p in points),
        max(p.y for p in points),
    )


def rotated(matrix: List[List]) -> List[List]:
    """Returns the given matrix rotated 90 degrees clockwise."""
    return [list(r) for r in zip(*matrix[::-1])]


def firsts(matrix: List[List]) -> List[List]:
    """Like matrix[0], but for the first column."""
    return rotated(matrix)[0]


def lasts(matrix):
    """Like matrix[-1], but for the last column."""
    return rotated(matrix)[-1]


def timeit(func):
    """Decorator that reports the execution time."""

    def wrap(*args, **kwargs):
        start = time.monotonic()
        result = func(*args, **kwargs)
        end = time.monotonic()

        print(f"Time taken for {func.__name__}: {round(end - start, 4)}")
        return result

    return wrap


def memoize(f: Callable):
    """Simple dictionary-based memoization decorator"""
    cache = {}

    def _mem_fn(*args):
        hargs = ",".join(str(x) for x in args)
        if hargs not in cache:
            cache[hargs] = f(*args)
        return cache[hargs]

    _mem_fn.cache = cache
    return _mem_fn


def poly_area(points: list[Point]):
    x = [p.x for p in points]
    y = [p.y for p in points]

    left = sum(np.multiply(x[:-1], y[1:]))
    right = sum(np.multiply(y[:-1], x[1:]))

    return abs(left - right) // 2


def range_intersect(r1, r2):
    if r1.step != 1 or r2.step != 1:
        raise ValueError("range_intersect only works with step=1")

    return range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None


def solve_quadratic(a, b, c):
    # solve the quadratic equation
    d = b**2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        return (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)


def get_distances(grid: dict[Point, Any], start: Point) -> dict[Point, int]:
    distances = {start: 0}
    queue = deque([start])

    while queue:
        pos = queue.popleft()
        for direction in DIRS:
            new = pos + direction
            if new in grid and new not in distances:
                distances[new] = distances[pos] + 1
                queue.append(new)

    return distances
