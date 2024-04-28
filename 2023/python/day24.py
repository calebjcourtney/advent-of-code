from utils import get_line_data
from utils import timeit
from utils import get_nums

import itertools
import math
from typing import Generator

from z3 import Real, Solver


MIN = 200000000000000
MAX = 400000000000000


class Coord:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, n: int):
        return Coord(self.x * n, self.y * n, self.z * n)

    def __repr__(self):
        return f"Coord({self.x}, {self.y}, {self.z})"


class Hailstone:
    def __init__(self, location: Coord, velocity: Coord):
        self.location = location
        self.velocity = velocity

    def __hash__(self):
        return hash((self.location, self.velocity))

    def __repr__(self):
        return f"Hailstone({self.location}, {self.velocity})"

    @property
    def slope(self):
        return self.velocity.y / self.velocity.x


def parse_data(data) -> Generator[Hailstone, None, None]:
    for line in data:
        x, y, z, dx, dy, dz = get_nums(line)
        yield Hailstone(Coord(x, y, z), Coord(dx, dy, dz))


def find_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
        (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    )
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
        (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    )
    return [px, py]


@timeit
def part_one(data) -> int:
    output = 0
    for a, b in itertools.combinations(data, 2):
        a_start = a.slope * MIN + a.location.y - (a.slope * a.location.x)
        a_end = a.slope * MAX + a.location.y - (a.slope * a.location.x)

        b_start = b.slope * MIN + b.location.y - (b.slope * b.location.x)
        b_end = b.slope * MAX + b.location.y - (b.slope * b.location.x)

        try:
            px, py = find_intersection(
                MIN, a_start, MAX, a_end, MIN, b_start, MAX, b_end
            )
        except:
            # Parallel lines.
            continue

        # Intersection in A's past
        if a.velocity.x > 0 and px < a.location.x:
            continue
        elif a.velocity.x < 0 and px > a.location.x:
            continue

        # Intersection in B's past
        if b.velocity.x > 0 and px < b.location.x:
            continue
        elif b.velocity.x < 0 and px > b.location.x:
            continue

        # Good intersection in zone.
        if MIN <= px <= MAX and MIN <= py <= MAX:
            output += 1

    return output


@timeit
def part_two(data: list[Hailstone]) -> int:
    mx = Real("mx")
    my = Real("my")
    mz = Real("mz")
    mxv = Real("mxv")
    myv = Real("myv")
    mzv = Real("mzv")
    c = [Real(f"c{n}") for n in range(len(data))]

    s = Solver()

    for i, hailstone in enumerate(data):
        s.add(c[i] >= 0)
        s.add(mx + c[i] * mxv == hailstone.location.x + c[i] * hailstone.velocity.x)
        s.add(my + c[i] * myv == hailstone.location.y + c[i] * hailstone.velocity.y)
        s.add(mz + c[i] * mzv == hailstone.location.z + c[i] * hailstone.velocity.z)

    s.check()
    m = s.model()

    return m[mx].as_long() + m[my].as_long() + m[mz].as_long()


if __name__ == "__main__":
    data = get_line_data("24")
    data = list(parse_data(data))

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
