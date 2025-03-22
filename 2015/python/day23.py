from utils import get_line_data


def part_one(data):
    registers = {"a": 0, "b": 0}
    i = 0
    while 0 <= i < len(data):
        instructions = data[i].split()
        op = instructions[0]
        next_i = i + 1

        if op == "hlf":
            registers[instructions[1]] //= 2
        elif op == "tpl":
            registers[instructions[1]] *= 3
        elif op == "inc":
            registers[instructions[1]] += 1
        elif op == "jmp":
            next_i = i + int(instructions[1])
        elif op == "jie":
            if registers[instructions[1].strip(',')] % 2 == 0:
                next_i = i + int(instructions[2])
        elif op == "jio":
            if registers[instructions[1].strip(',')] == 1:
                next_i = i + int(instructions[2])

        i = next_i

    return registers["b"]


def part_two(data):
    registers = {"a": 1, "b": 0}
    i = 0
    while 0 <= i < len(data):
        instructions = data[i].split()
        op = instructions[0]
        next_i = i + 1

        if op == "hlf":
            registers[instructions[1]] //= 2
        elif op == "tpl":
            registers[instructions[1]] *= 3
        elif op == "inc":
            registers[instructions[1]] += 1
        elif op == "jmp":
            next_i = i + int(instructions[1])
        elif op == "jie":
            if registers[instructions[1].strip(',')] % 2 == 0:
                next_i = i + int(instructions[2])
        elif op == "jio":
            if registers[instructions[1].strip(',')] == 1:
                next_i = i + int(instructions[2])

        i = next_i

    return registers["b"]


if __name__ == '__main__':
    data = get_line_data("23")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
