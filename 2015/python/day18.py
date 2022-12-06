from utils import get_line_data


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

                points.append((xi, yi))

        return points

    def step(self):
        temp_data = self.data[:][:]

        for x in range(len(temp_data)):
            for y in range(len(temp_data[0])):
                neighbors = self.get_neighbors(x, y)
                if temp_data[x][y] == 1:
                    if sum(self.data[x][y] for (x, y) in neighbors) not in [2, 3]:
                        temp_data[x][y] = 0

                elif temp_data[x][y] == 0:
                    if sum(self.data[x][y] for (x, y) in neighbors) == 3:
                        temp_data[x][y] = 1

        self.data = temp_data[:][:]

    def __repr__(self):
        return "\n".join(
            "".join(["#" if x == 1 else "." for x in row])
            for row in self.data
        )


def test_grid():
    data = """.#.#.#
...##.
#....#
..#...
#.#..#
####..""".split("\n")

    grid = Grid([
        [1 if x == "#" else 0 for x in line]
        for line in data
    ])

    neighbors = grid.get_neighbors(1, 0)
    assert neighbors == [(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)]
    print(neighbors)


def part_one(data):
    for _ in range(4):
        data.step()

    return sum(sum(row) for row in data.data)


def part_two(data):
    for line in data:
        pass


if __name__ == '__main__':
    test_grid()
    data = get_line_data("18")
    data = """.#.#.#
...##.
#....#
..#...
#.#..#
####..""".split("\n")

    grid = Grid([
        [1 if x == "#" else 0 for x in line]
        for line in data
    ])

    p1_result = part_one(grid)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
