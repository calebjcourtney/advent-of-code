from collections import deque
import hashlib

from utils import get_data
from utils import timeit
from utils import Point
from utils import N, S, E, W


GRID = {
    Point(x, y)
    for x in range(4)
    for y in range(4)
}

DIRECTIONS = {
    "D": N,
    "U": S,
    "R": E,
    "L": W,
}

RECIPROCALS = {
    "D": "U",
    "U": "D",
    "R": "L",
    "L": "R",
}


def md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()


@timeit
def part_one(data):
    start = Point(0, 0)
    end = Point(3, 3)
    horizon = deque([(start, data)])

    while horizon:
        current, path = horizon.popleft()
        if current == end:
            return "".join(c for c in path if c in DIRECTIONS)

        h = md5_hash(path)
        # up
        if (h[0] in "bcdef" and current + DIRECTIONS["U"] in GRID) or path[-1] == "D":
            horizon.append((current + DIRECTIONS["U"], path + "U"))
        # down
        if (h[1] in "bcdef" and current + DIRECTIONS["D"] in GRID) or path[-1] == "U":
            horizon.append((current + DIRECTIONS["D"], path + "D"))
        # left
        if (h[2] in "bcdef" and current + DIRECTIONS["L"] in GRID) or path[-1] == "R":
            horizon.append((current + DIRECTIONS["L"], path + "L"))
        # right
        if (h[3] in "bcdef" and current + DIRECTIONS["R"] in GRID) or path[-1] == "L":
            horizon.append((current + DIRECTIONS["R"], path + "R"))


@timeit
def part_two(data):
    for line in data:
        pass


if __name__ == '__main__':
    data = get_data("17")
    data = "hijkl"

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
