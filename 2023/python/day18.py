from utils import get_line_data
from utils import timeit
from utils import Point
from utils import N as D
from utils import S as U
from utils import E as R
from utils import W as L

import numpy as np

from typing import NamedTuple


MAPPING = {'R': R, 'L': L, 'U': U, 'D': D}


class Instruction(NamedTuple):
    direction: Point
    distance: int


def parse_data(line: str, part_one: bool = True) -> Instruction:
    direction, dist, rgb_hex = line.split()
    if part_one:
        direction = MAPPING[direction]
        dist = int(dist)
    else:
        direction = MAPPING["RDLU"[int(rgb_hex[-2])]]
        dist = int(rgb_hex[2:-2], 16)

    return Instruction(direction, dist)


@timeit
def combined(data, part_one=True):
    x = []
    y = []
    circumference = 0
    current = Point(0, 0)
    for line in data:
        instruction = parse_data(line, part_one)
        current += instruction.direction * instruction.distance
        x.append(current.x)
        y.append(current.y)
        circumference += instruction.distance

    left = sum(np.multiply(x[:-1], y[1:]))
    right = sum(np.multiply(y[:-1], x[1:]))

    return abs(left - right) // 2 + circumference // 2 + 1


if __name__ == '__main__':
    data = get_line_data("18")

    p1_result = combined(data)
    print(p1_result)

    p2_result = combined(data, False)
    print(p2_result)
