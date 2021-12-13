from utils import get_data


class Grid:
    def __init__(self, data):
        self.data = data

    def vertical_fold(self, axis):
        g1 = Grid([[row[x] for x in range(axis)] for row in self.data])
        g2 = Grid([[row[x] for x in range(axis + 1, min([len(row), axis + axis + 1]))] for row in self.data])

        assert len(g2.data) == len(g1.data)
        assert len(g2.data[0]) == len(g1.data[0])

        g2.vertical_reverse()

        new_data = []
        for i in range(len(g1.data)):
            new_data.append([max([x, y]) for x, y in zip(g1.data[i], g2.data[i])])

        self.data = new_data

    def horizontal_fold(self, axis):
        g1 = Grid(self.data[:axis])
        g2 = Grid(self.data[axis + 1: min([len(self.data), axis + axis + 1])])

        assert len(g2.data) == len(g1.data)
        assert len(g2.data[0]) == len(g1.data[0])

        g2.horizontal_reverse()

        new_data = []
        for i in range(len(g1.data)):
            new_data.append([max([x, y]) for x, y in zip(g1.data[i], g2.data[i])])

        self.data = new_data

    def count_dots(self):
        return sum(sum(row) for row in self.data)

    def horizontal_reverse(self):
        self.data = self.data[:: -1]

    def vertical_reverse(self):
        self.data = [row[::-1] for row in self.data]

    def pprint(self):
        for row in self.data:
            print(*["#" if x == 1 else " " for x in row])


def initiate_grid(location_data):
    max_x = max(x[0] for x in location_data)
    max_y = max(y[1] for y in location_data)

    return [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]


def part_one(location_data, fold_instructions):
    g = initiate_grid(location_data)

    for x, y in location_data:
        g[y][x] = 1

    g = Grid(g)

    for direction, val in fold_instructions:
        if direction == "y":
            g.horizontal_fold(val)

        elif direction == "x":
            g.vertical_fold(val)

        else:
            raise ValueError(f"unknown value `{direction}`")

    return g.count_dots()


def part_two(location_data, fold_instructions):
    g = initiate_grid(location_data)

    for x, y in location_data:
        g[y][x] = 1

    g = Grid(g)

    for direction, val in fold_instructions:
        if direction == "y":
            g.horizontal_fold(val)

        elif direction == "x":
            g.vertical_fold(val)

        else:
            raise ValueError(f"unknown value `{direction}`")

    return g


if __name__ == '__main__':
    data = get_data("13")

    # parse the location data
    location_data = data.split("\n\n")[0]
    location_data = [tuple(map(int, x.split(","))) for x in location_data.split("\n")]

    # format the fold instructions
    fold_data = data.split("\n\n")[1]
    fold_instructions = []
    for row in fold_data.split("\n"):
        row = row.lstrip("fold along ")
        direction, val = row.split("=")
        fold_instructions.append((direction, int(val)))

    p1_result = part_one(location_data, fold_instructions[:1])
    print(p1_result)

    p2_result = part_two(location_data, fold_instructions)
    p2_result.pprint()
