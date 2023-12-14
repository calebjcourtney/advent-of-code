from utils import get_line_data
from utils import timeit
from utils import parse_grid
from utils import N, S, E, W
from utils import min_max_xy
from utils import Point

from itertools import product


class Grid:
    def __init__(self, data):
        self.grid = parse_grid(data)
        self.min_x, self.max_x, self.min_y, self.max_y = min_max_xy(self.grid.keys())

    def tilt(self, direction):
        if direction == N:
            for x, y in product(range(self.max_x + 1), range(1, self.max_y + 1)):
                p = Point(x, y)
                if self.grid[p] != 'O':
                    continue

                while p.y > 0:
                    np = p + S
                    if self.grid[np] == '.':
                        self.grid[p], self.grid[np] = '.', 'O'
                    else:
                        break
                    p = np

        elif direction == S:
            for x, y in product(range(self.max_x + 1), range(self.max_y - 1, -1, -1)):
                p = Point(x, y)
                if self.grid[p] != 'O':
                    continue

                while p.y < self.max_y:
                    np = p + N
                    if self.grid[np] == '.':
                        self.grid[p], self.grid[np] = '.', 'O'
                    else:
                        break
                    p = np

        elif direction == E:
            for x, y in product(range(self.max_x, -1, -1), range(self.max_y + 1)):
                p = Point(x, y)
                if self.grid[p] != 'O':
                    continue

                while p.x < self.max_x:
                    np = p + E
                    if self.grid[np] == '.':
                        self.grid[p], self.grid[np] = '.', 'O'
                    else:
                        break
                    p = np

        elif direction == W:
            for x, y in product(range(1, self.max_x + 1), range(self.max_y + 1)):
                p = Point(x, y)
                if self.grid[p] != 'O':
                    continue

                while p.x > 0:
                    np = p + W
                    if self.grid[np] == '.':
                        self.grid[p], self.grid[np] = '.', 'O'
                    else:
                        break
                    p = np

    def load(self):
        return sum(self.max_y - point.y + 1 for point, value in self.grid.items() if value == "O")

    def cycle(self):
        for direction in (N, W, S, E,):
            self.tilt(direction)

    @property
    def pattern(self):
        output = ""

        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                output += self.grid[Point(x, y)]
            output += "\n"

        return output.strip()


@timeit
def part_one(data):
    data.tilt(N)
    return data.load()


@timeit
def part_two(data):
    seen_grids = {}

    cycles = 1
    while True:
        data.cycle()

        pattern = data.pattern
        if pattern in seen_grids:
            break
        else:
            seen_grids[pattern] = cycles

        cycles += 1

    cycle_len = cycles - seen_grids[pattern]

    while cycles % cycle_len != 1000000000 % cycle_len:
        data.cycle()
        cycles += 1

    return data.load()


if __name__ == '__main__':
    data = get_line_data("14")
    grid = Grid(data)

    p1_result = part_one(grid)
    print(p1_result)

    grid = Grid(data)
    p2_result = part_two(grid)
    print(p2_result)
