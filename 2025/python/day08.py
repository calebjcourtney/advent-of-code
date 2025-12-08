from utils import get_line_data
from utils import timeit
from utils import get_nums
import math

from typing import NamedTuple
from itertools import combinations
from collections import Counter

TARGET_PAIRS = 1000

class Point(NamedTuple):
    x: int
    y: int
    z: int

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)


def parse_data(data):
    points = set[Point]()
    for line in data:
        x, y, z = get_nums(line)
        points.add(Point(x, y, z))

    return points


class CircuitConnector:
    def __init__(self, points):
        self.points = points
        self.parent = {point: point for point in points}

    def find(self, point):
        if self.parent[point] != point:
            self.parent[point] = self.find(self.parent[point])
        return self.parent[point]

    def union(self, p1, p2):
        root1 = self.find(p1)
        root2 = self.find(p2)
        if root1 != root2:
            self.parent[root1] = root2
            return True
        return False

    def count_circuits(self):
        return len(set(self.find(point) for point in self.points))

    def get_circuit_sizes(self):
        return sorted(Counter(self.find(point) for point in self.points).values(), reverse=True)

    def solve(self):
        pairs = []
        for p1, p2 in combinations(self.points, 2):
            dist = p1.distance(p2)
            pairs.append((dist, p1, p2))

        pairs.sort(key=lambda x: x[0])
        part_one_result = part_two_result = None

        for i, (dist, p1, p2) in enumerate(pairs):
            was_connected = self.union(p1, p2)

            if i == TARGET_PAIRS - 1:
                sizes = self.get_circuit_sizes()
                part_one_result = sizes[0] * sizes[1] * sizes[2]

            if was_connected:
                if self.count_circuits() == 1:
                    part_two_result = p1.x * p2.x

            if part_one_result is not None and part_two_result is not None:
                return part_one_result, part_two_result


@timeit
def main():
    data = get_line_data("08")
    points = parse_data(data)

    connector = CircuitConnector(points)
    p1_result, p2_result = connector.solve()
    print(p1_result)
    print(p2_result)
