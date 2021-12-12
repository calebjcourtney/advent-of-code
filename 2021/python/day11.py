from utils import get_line_data


class Octopus:
    def __init__(self, arg):
        self.energy = arg
        self.flash_stepped = False
        self.neighbors = []

        self.flashes = 0

    def add_one(self):
        self.energy += 1

        if not self.flash_stepped and self.energy >= 10:
            self.flashes += 1
            self.flash_stepped = True

            for octopus in self.neighbors:
                octopus.add_one()

    def reset_energy(self):
        if self.flash_stepped:
            self.energy = 0
            self.flash_stepped = False


def build_octopi(data):
    octopi = [[] for _ in range(len(data))]

    for row_index in range(len(data)):
        for col_index in range(len(data[0])):
            octopus = Octopus(data[row_index][col_index])

            octopi[row_index].append(octopus)

    for row_index in range(len(data)):
        for col_index in range(len(data[0])):
            octopus = octopi[row_index][col_index]
            points = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]
            for dr, dc in points:
                rr = dr + row_index
                cc = dc + col_index

                if 0 <= rr < len(data) and 0 <= cc < len(data[0]):
                    octopus.neighbors.append(octopi[rr][cc])

    return octopi


def part_one(data):
    octopi = build_octopi(data)

    for _ in range(100):
        for row in octopi:
            for octopus in row:
                octopus.add_one()

        for row in octopi:
            for octopus in row:
                octopus.reset_energy()

    total = 0
    for row in octopi:
        for col in row:
            total += col.flashes

    return total


def all_octopi_flashed(octopi):
    for row in octopi:
        for octopus in row:
            if not octopus.flash_stepped:
                return False

    return True


def part_two(data):
    octopi = build_octopi(data)

    steps = 0

    while True:
        for row in octopi:
            for octopus in row:
                octopus.add_one()

        steps += 1

        if all_octopi_flashed(octopi):
            return steps

        for row in octopi:
            for octopus in row:
                octopus.reset_energy()


if __name__ == '__main__':
    data = get_line_data("11")

    data = [list(map(int, list(line))) for line in data]

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
