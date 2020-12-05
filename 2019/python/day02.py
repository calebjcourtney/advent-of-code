import sys

from utils import get_data

data = list(map(int, get_data("02").split(",")))


class IntCoder(object):
    """docstring for IntCoder"""

    def __init__(self, program):
        self.program = program
        self.pos = 0

    def run(self):
        while True:
            opcode = self.program[self.pos]

            if opcode == 1:
                self.add(self.pos + 1, self.pos + 2, self.pos + 3)
                self.pos += 4

            elif opcode == 2:
                self.multiply(self.pos + 1, self.pos + 2, self.pos + 3)
                self.pos += 4

            elif opcode == 99:
                return self.output()

            else:
                raise ValueError(f"Ran into unknown opcode `{self.pos}`")

    def add(self, first, last, position):
        self.program[self.program[position]] = self.program[self.program[first]] + self.program[self.program[last]]

    def multiply(self, first, last, position):
        self.program[self.program[position]] = self.program[self.program[first]] * self.program[self.program[last]]

    def output(self):
        return self.program[0]


def part_1():
    # part 1
    data[1] = 12
    data[2] = 2
    coder = IntCoder(data)
    coder.run()

    return coder.output()


def part_2():
    for noun in range(100):
        for verb in range(100):
            data = list(map(int, get_data("02").split(",")))

            data[1] = noun
            data[2] = verb

            coder = IntCoder(data)
            coder.run()

            if coder.output() == 19690720:
                return 100 * noun + verb


if __name__ == '__main__':
    print(part_1())
    print(part_2())
