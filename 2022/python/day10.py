from utils import get_line_data


def parse_line(line):
    instructions = line.split()
    statement = instructions[0]
    amount = None if len(instructions) == 1 else int(instructions[1])

    return statement, amount


def parse_instructions(data):
    x = 1
    output = [0]

    for line in data:
        statement, value = parse_line(line)
        if statement == "noop":
            output += [x]

        else:
            output += [x, x]
            x += value

    return output


def part_one(instructions):
    return sum(x * y for x, y in enumerate(instructions) if x % 40 == 20)


def part_two(instructions):
    for i in range(1, len(instructions), 40):
        for j in range(40):
            print(end="##" if abs(instructions[i + j] - j) <= 1 else "  ")
        print()


if __name__ == '__main__':
    data = get_line_data("10")
    instructions = parse_instructions(data)

    p1_result = part_one(instructions)
    print(p1_result)

    part_two(instructions)
