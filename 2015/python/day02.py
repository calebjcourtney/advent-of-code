from utils import get_line_data

from itertools import combinations


class Box:
    def __init__(self, arg):
        self.l, self.w, self.h = map(int, arg.split("x"))

    def surface_area(self):
        vals = [x * y * 2 for x, y in combinations([self.l, self.w, self.h], 2)]
        return sum(vals) + min(vals) / 2

    def ribbon_length(self):
        vals = [x * 2 + y * 2 for x, y in combinations([self.l, self.w, self.h], 2)]
        return self.l * self.w * self.h + min(vals)


def part_one(data):
    return int(sum([box.surface_area() for box in map(Box, data)]))


def part_two(data):
    return int(sum([box.ribbon_length() for box in map(Box, data)]))


if __name__ == '__main__':
    data = get_line_data("02")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
