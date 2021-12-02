from utils import get_line_data


class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.vertical = 0
        self.aim = 0

    def add_instruction(self, line):
        direction, magnitude = line.split()
        magnitude = int(magnitude)

        if "forward" == direction:
            self.horizontal += int(line.split()[1])
            self.vertical += self.aim * int(line.split()[1])

        elif "down" == direction:
            self.aim += int(line.split()[1])

        elif "up" == direction:
            self.aim -= int(line.split()[1])

    def position(self):
        return self.horizontal * self.vertical


def part_one(data):
    horizontal = 0
    vertical = 0
    for line in data:
        if "forward" in line:
            horizontal += int(line.split()[1])

        elif "down" in line:
            vertical += int(line.split()[1])
        elif "up" in line:
            vertical -= int(line.split()[1])

    return horizontal * vertical


def part_two(data):
    submarine = Submarine()
    for line in data:
        submarine.add_instruction(line)

    return submarine.position()


if __name__ == '__main__':
    data = get_line_data("02")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
