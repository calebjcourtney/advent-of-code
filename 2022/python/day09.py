from typing import Set, Tuple

from utils import get_line_data

DIRECTIONS = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0)
}


def parse_line(line):
    direction, count = line.strip().split()
    return direction, int(count)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rope:
    def __init__(self, rope_len):
        self.knots = [Point(0, 0) for point in range(rope_len)]
        self.tail_visits: Set[Tuple[int, int]] = set((0, 0))

    def move_head(self, direction):
        x, y = DIRECTIONS[direction]
        self.knots[0].x += x
        self.knots[0].y += y

    def distance(self, index):
        return Point(
            self.knots[index - 1].x - self.knots[index].x,
            self.knots[index - 1].y - self.knots[index].y
        )

    def move_index(self, index, direction):
        dist = self.distance(index)
        if abs(dist.x) < 2 and abs(dist.y) < 2:
            return

        x = 0 if dist.x == 0 else abs(dist.x) / dist.x
        y = 0 if dist.y == 0 else abs(dist.y) / dist.y

        self.knots[index].x += x
        self.knots[index].y += y

        if index == len(self.knots) - 1:
            self.tail_visits.add((self.knots[index].x, self.knots[index].y))

    def move(self, direction, count):
        for _ in range(count):
            self.move_head(direction)
            for index in range(1, len(self.knots)):
                self.move_index(index, direction)


def part_one(data):
    rope = Rope(2)

    for line in data:
        direction, count = parse_line(line)
        rope.move(direction, count)

    return len(rope.tail_visits)


def part_two(data):
    rope = Rope(10)

    for line in data:
        direction, count = parse_line(line)
        rope.move(direction, count)

    return len(rope.tail_visits)


if __name__ == '__main__':
    data = get_line_data("09")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
