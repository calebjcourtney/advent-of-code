from utils import get_line_data
from utils import timeit
from utils import Point
from utils import N as D
from utils import S as U
from utils import E as R
from utils import W as L

from collections import deque

from typing import NamedTuple

from tqdm import tqdm


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
    dig_points = deque([])
    current = Point(0, 0)
    for line in tqdm(data):
        instruction = parse_data(line, part_one)
        for _ in range(instruction.distance):
            current += instruction.direction
            dig_points.append(current)

    x = [point.x for point in dig_points]
    y = [point.y for point in dig_points]

    left = sum(a * b for a, b in zip(x, y[1:]))
    right = sum(a * b for a, b in zip(y, x[1:]))
    return abs(left - right) // 2 + len(dig_points) // 2 + 1


if __name__ == '__main__':
    data = get_line_data("18")

    p1_result = combined(data)
    print(p1_result)

    p2_result = combined(data, False)
    print(p2_result)
