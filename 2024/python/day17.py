from utils import get_data
from utils import timeit
from utils import get_nums

from tqdm import tqdm


def get_combo_value(operand, a, b, c):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    raise ValueError(f"unknown value {operand}")


class Program:
    def __init__(self, registers, instructions):
        self.index = 0
        self.instructions = instructions
        self.A = registers[0]
        self.B = registers[1]
        self.C = registers[2]

    def process_opcode(self, opcode, operand, outputs: list[int]):
        if opcode == 0:
            combo_value = get_combo_value(operand, self.A, self.B, self.C)
            assert combo_value == 3
            num = self.A >> combo_value
            self.A = num
            self.index += 2

        elif opcode == 1:
            self.B = self.B ^ operand
            self.index += 2

        elif opcode == 2:
            combo_value = get_combo_value(operand, self.A, self.B, self.C)
            self.B = combo_value % 8
            self.index += 2

        elif opcode == 3:
            if self.A != 0:
                self.index = operand
            else:
                self.index += 2

        elif opcode == 4:
            self.B = self.B ^ self.C
            self.index += 2

        elif opcode == 5:
            combo_value = get_combo_value(operand, self.A, self.B, self.C)
            outputs.append(combo_value % 8)
            self.index += 2

        elif opcode == 6:
            num = self.A >> get_combo_value(operand, self.A, self.B, self.C)
            self.B = num
            self.index += 2

        elif opcode == 7:
            num = self.A >> get_combo_value(operand, self.A, self.B, self.C)
            self.C = num
            self.index += 2

    def run(self):
        outputs = []
        while self.index < len(self.instructions) or len(outputs) == 0:
            opcode, operand = self.instructions[self.index], self.instructions[self.index + 1]
            self.process_opcode(opcode, operand, outputs)

        return outputs

    def get_first_out(self):
        outputs = []

        while self.index < len(self.instructions) - 2:
            opcode, operand = self.instructions[self.index], self.instructions[self.index + 1]
            self.process_opcode(opcode, operand, outputs)
            if len(outputs) == 1:
                return outputs[0]

        return outputs


@timeit
def part_one(registers, program):
    prog = Program(registers, program)
    output = prog.run()
    return ",".join(map(str, output))


def find(target, ans):
    if target == []: return ans
    for t in range(8):
        a = ans << 3 | t
        b = 0
        c = 0
        output = None

        for pointer in range(0, len(program) - 2, 2):
            ins = program[pointer]
            operand = program[pointer + 1]
            if ins == 1:
                b ^= operand
            elif ins == 2:
                b = get_combo_value(operand, a, b, c) % 8
            elif ins == 4:
                b ^= c
            elif ins == 5:
                output = get_combo_value(operand, a, b, c) % 8
            elif ins == 7:
                c = a >> get_combo_value(operand, a, b, c)

            if output == target[-1]:
                new = find(target[:-1], a)
                if new is None:
                    continue

                return new


@timeit
def part_two(program):
    return find(program, 0)


if __name__ == '__main__':
    data = get_data("17")

    registers, program = data.split("\n\n")
    registers = get_nums(registers)
    program = get_nums(program)

    p1_result = part_one(registers, program)
    print(p1_result)

    p2_result = part_two(program)
    print(p2_result)
