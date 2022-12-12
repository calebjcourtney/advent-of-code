import operator
import os
import re
from typing import List, Tuple, NamedTuple
from more_itertools import windowed
from functools import reduce

from aocd.models import Puzzle


def get_data(day: str) -> str:
    input_dir = "/".join(os.getcwd().split("/")[:-1])
    try:
        data = open("{}/inputs/input{}.txt".format(input_dir, day), "r").read().rstrip()
    except FileNotFoundError:
        puzzle = Puzzle(year=2022, day=int(day))
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
    return lst[n:] + lst[:n]


def array_right_rotate(lst, n=1):
    return lst[-n:] + lst[:-n]


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
    return reduce(operator.mul, lst, 1)


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

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def neighbors(self):
        return [self + p for p in DIRS]

    def neighbors_8(self):
        return [self + p for p in DIRS_8]


DIRS = [
    Point(0, 1),   # north
    Point(1, 0),   # east
    Point(0, -1),  # south
    Point(-1, 0),  # west
]


DIRS_8 = [
    Point(0, 1),    # N
    Point(1, 1),    # NE
    Point(1, 0),    # E
    Point(1, -1),   # SE
    Point(0, -1),   # S
    Point(-1, -1),  # SW
    Point(-1, 0),   # W
    Point(-1, 1),   # NW
]
