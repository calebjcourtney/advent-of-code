from utils import get_line_data

from collections import Counter


class Point:
    def __init__(self, coords):
        self.x = int(coords.split(",")[0])
        self.y = int(coords.split(",")[1])


class Line:
    def __init__(self, line):
        self.start = Point(line.split(" -> ")[0])
        self.end = Point(line.split(" -> ")[1])

    def points_covered(self):
        output = set()

        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y

        for i in range(1 + max(abs(dx), abs(dy))):
            x = self.start.x + (1 if dx > 0 else (-1 if dx < 0 else 0)) * i
            y = self.start.y + (1 if dy > 0 else (-1 if dy < 0 else 0)) * i
            output.add((x, y))

        return output


def part_one(data):
    points = []
    for row in data:
        line = Line(row)
        if line.start.x == line.end.x or line.start.y == line.end.y:
            points += line.points_covered()

    c = Counter(points)

    return len([x for x in c.values() if x >= 2])


def part_two(data):
    points = []
    for row in data:
        line = Line(row)
        points += line.points_covered()

    c = Counter(points)

    return len([x for x in c.values() if x >= 2])


if __name__ == '__main__':
    data = get_line_data("05")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
