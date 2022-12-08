from utils import get_line_data

import numpy as np


class Grid:
    def __init__(self, data):
        self.data = data

    def north_visible(self, x: int, y: int) -> bool:
        r = [self.data[yi][x] for yi in range(y)]
        return True if not r else self.data[y][x] > max(r)

    def south_visible(self, x: int, y: int) -> bool:
        r = [self.data[yi][x] for yi in range(y + 1, len(self.data))]
        return True if not r else self.data[y][x] > max(r)

    def west_visible(self, x: int, y: int) -> bool:
        r = [self.data[y][xi] for xi in range(x)]
        return True if not r else self.data[y][x] > max(r)

    def east_visible(self, x: int, y: int) -> bool:
        r = [self.data[y][xi] for xi in range(x + 1, len(self.data[0]))]
        return True if not r else self.data[y][x] > max(r)

    def is_visible(self, x: int, y: int) -> bool:
        return any([
            self.north_visible(x, y),
            self.south_visible(x, y),
            self.west_visible(x, y),
            self.east_visible(x, y),
        ])

    def visible_trees(self) -> int:
        return sum([
            self.is_visible(x, y)
            for y in range(len(self.data))
            for x in range(len(self.data[y]))
        ])

    def north_count(self, x: int, y: int) -> int:
        count = 0
        for yi in range(y - 1, -1, -1):
            count += 1
            if self.data[yi][x] >= self.data[y][x]:
                break

        return count

    def south_count(self, x: int, y: int) -> int:
        count = 0
        for yi in range(y + 1, len(data)):
            count += 1
            if self.data[yi][x] >= self.data[y][x]:
                break

        return count

    def west_count(self, x: int, y: int) -> int:
        count = 0
        for xi in range(x - 1, -1, -1):
            count += 1
            if self.data[y][xi] >= self.data[y][x]:
                break

        return count

    def east_count(self, x: int, y: int) -> int:
        count = 0
        for xi in range(x + 1, len(data[y])):
            count += 1
            if self.data[y][xi] >= self.data[y][x]:
                break

        return count

    def scenic_score(self, x: int, y: int) -> int:
        return np.prod([
            self.north_count(x, y),
            self.south_count(x, y),
            self.east_count(x, y),
            self.west_count(x, y)
        ])

    def best_scenic_score(self) -> int:
        top_score = 0
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                temp = self.scenic_score(x, y)
                top_score = temp if temp > top_score else top_score

        return top_score


if __name__ == '__main__':
    data = get_line_data("08")
    grid = Grid([list(map(int, row)) for row in data])

    print(grid.visible_trees())
    print(grid.best_scenic_score())
