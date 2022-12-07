from utils import get_line_data

from copy import deepcopy


class Grid:
    def __init__(self, data):
        self.data = data

    def get_neighbors(self, x, y):
        x_range = range(max(0, x - 1), min(len(self.data), x + 2))
        y_range = range(max(0, y - 1), min(len(self.data), y + 2))

        points = []
        for xi in x_range:
            for yi in y_range:
                if xi == x and yi == y:
                    continue

                yield (yi, xi)

        return points

    def sum_neighbors(self, x, y):
        return sum([
            self.data[yi][xi]
            for (yi, xi) in self.get_neighbors(x, y)
        ])

    def step(self):
        temp_data = deepcopy(self.data)

        for x in range(len(temp_data)):
            for y in range(len(temp_data[0])):
                ns = self.sum_neighbors(x, y)
                if temp_data[y][x] == 1 and ns not in [2, 3]:
                    temp_data[y][x] = 0

                elif temp_data[y][x] == 0 and ns == 3:
                    temp_data[y][x] = 1

        self.data = temp_data[:][:]

    def sum(self):
        return sum(sum(x for x in y) for y in self.data)

    def corners(self):
        return [
            (0, 0),
            (0, len(self.data) - 1),
            (len(self.data) - 1, 0),
            (len(self.data) - 1, len(self.data) - 1)
        ]

    def __repr__(self):
        return "\n".join(
            "".join(["#" if x == 1 else "." for x in y])
            for y in self.data
        )

    def __str__(self):
        return self.__repr__()


def part_one(data):
    for _ in range(100):
        data.step()

    return data.sum()


def part_two(data):
    for y, x in data.corners():
        data.data[y][x] = 1
    for _ in range(100):
        data.step()

        for y, x in data.corners():
            data.data[y][x] = 1

    return data.sum()


if __name__ == '__main__':
    data = get_line_data("18")

    grid = Grid([
        [1 if x == "#" else 0 for x in line]
        for line in data
    ])

    p1_result = part_one(grid)
    print(p1_result)

    grid = Grid([
        [1 if x == "#" else 0 for x in line]
        for line in data
    ])

    p2_result = part_two(grid)
    print(p2_result)
