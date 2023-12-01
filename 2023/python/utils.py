import os
import re
from typing import List, Tuple, NamedTuple
from numbers import Number
from more_itertools import windowed
import math

from aocd.models import Puzzle

from numpy import ones, vstack
from numpy.linalg import lstsq

YEAR = 2023


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
        yield lst[i:i + n]


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

    def neighbors(self):
        return [self + p for p in DIRS]

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


def parse_grid(data):
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
    for x in range(center.x, center.x + distance + 1):
        for y in range(center.y, center.y + distance + 1):
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
