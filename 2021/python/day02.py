from utils import get_line_data


class Instruction:
    def __init__(self, row):

        info = row.split()
        self.direction = info[0]
        self.magnitude = int(info[1])


def part_one(instructions):
    horizontal = 0
    vertical = 0
    for instruction in instructions:
        if "forward" == instruction.direction:
            horizontal += instruction.magnitude

        elif "down" == instruction.direction:
            vertical += instruction.magnitude
        elif "up" == instruction.direction:
            vertical -= instruction.magnitude

    return horizontal * vertical


class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.vertical = 0
        self.aim = 0

    def add_instruction(self, instruction):
        if "forward" == instruction.direction:
            self.horizontal += instruction.magnitude
            self.vertical += self.aim * instruction.magnitude

        elif "down" == instruction.direction:
            self.aim += instruction.magnitude

        elif "up" == instruction.direction:
            self.aim -= instruction.magnitude

    def position(self):
        return self.horizontal * self.vertical


def part_two(data):
    submarine = Submarine()
    for line in data:
        submarine.add_instruction(line)

    return submarine.position()


if __name__ == '__main__':
    data = get_line_data("02")
    data = [Instruction(line) for line in data]

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
