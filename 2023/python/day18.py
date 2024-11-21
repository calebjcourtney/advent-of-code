from utils import get_line_data
from utils import timeit
from utils import Point
from utils import N as D
from utils import S as U
from utils import E as R
from utils import W as L
from utils import manhattan

from utils import Point, N, S, E, W


DIR_MAPPING = {
    # part one
    'U': N,
    'D': S,
    'L': W,
    'R': E,
    # part two
    '0': E,
    '1': S,
    '2': W,
    '3': N,
}


def area(points):
    # shoelace formula
    area = 0

    for a, b in zip(points, points[1:] + [points[0]]):
        area += (b.x + a.x) * (b.y - a.y)

    area = int(abs(area / 2.0))

    # perimeter
    perimeter = sum(manhattan(a, b) for a, b in zip(points, points[1:] + [points[0]]))

    # outer strip
    return area + (perimeter // 2) + 1


def part_one(data):
    pos = Point(0, 0)
    points = [pos]

    for line in data:
        direction, distance, hex_code = line.split()
        direction = DIR_MAPPING[direction]
        dist = int(distance)

        pos += direction * dist

        points.append(pos)

    return area(points)



def part_two(data):
    pos = Point(0, 0)
    points = [pos]

    for line in data:
        direction, distance, hex_code = line.split()

        direction = DIR_MAPPING[hex_code[-2]]
        dist = int(hex_code[2:-2], 16)

        pos += direction * dist

        points.append(pos)

    return area(points)



if __name__ == '__main__':
    data = get_line_data("18")

    print(part_one(data))
    print(part_two(data))
