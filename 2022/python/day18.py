from utils import get_line_data, get_nums

from typing import NamedTuple
from typing import Set
from typing import Tuple

from collections import deque


class Point(NamedTuple):
    x: int
    y: int
    z: int

    def __eq__(self, point):
        return all([point.x == self.x, point.y == self.y, point.z == self.z])

    def neighbors(self):
        for (x, y, z) in [
            (-1, 0, 0),
            (1, 0, 0),
            (0, -1, 0),
            (0, 1, 0),
            (0, 0, -1),
            (0, 0, 1),
        ]:
            yield Point(self.x + x, self.y + y, self.z + z)


def part_one(points: Set[Point]) -> int:
    total = 0
    for point in points:
        for neighbor in point.neighbors():
            if neighbor not in points:
                total += 1

    return total


def min_max_xyz(points: Set[Point]) -> Tuple[Point, Point]:
    min_x = min(point.x for point in points)
    max_x = max(point.x for point in points)

    min_y = min(point.y for point in points)
    max_y = max(point.y for point in points)

    min_z = min(point.z for point in points)
    max_z = max(point.z for point in points)

    return Point(min_x, min_y, min_z), Point(max_x, max_y, max_z)


def outside(point: Point, min_point: Point, max_point: Point) -> bool:
    x = min_point.x <= point.x < max_point.x
    y = min_point.y <= point.y < max_point.y
    z = min_point.z <= point.z < max_point.z
    return not (x and y and z)


# I hate this
INTERNALS = set()


def is_internal(point: Point, min_point: Point, max_point: Point) -> bool:
    seen = set()
    horizon = deque([point])

    while horizon:
        point = horizon.popleft()
        if point in seen:
            continue

        if point in INTERNALS:
            return True

        if outside(point, min_point, max_point):
            return False

        seen.add(point)

        for neighbor in point.neighbors():
            if neighbor in points:
                continue

            horizon.append(neighbor)

    for point in seen:
        INTERNALS.add(point)

    return True


def part_two(data: Set[Point]) -> int:
    total = 0
    min_point, max_point = min_max_xyz(data)
    for point in data:
        for neighbor in point.neighbors():
            if neighbor not in data and not is_internal(neighbor, min_point, max_point):
                total += 1

    return total


if __name__ == "__main__":
    data = get_line_data("18")
    points = set(Point(*get_nums(line)) for line in data)

    p1_result = part_one(points)
    print(p1_result)

    p2_result = part_two(points)
    print(p2_result)
