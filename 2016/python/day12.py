from utils import get_line_data
from utils import timeit


def run(data, registers):
    index = 0
    while index < len(data):
        line = data[index].strip()
        if line.startswith("cpy"):
            _, val, reg = line.split()
            if val in "abcd":
                registers[reg] = registers[val]
            else:
                assert val.isnumeric()
                registers[reg] = int(val)

            index += 1

        elif line.startswith("inc"):
            _, reg = line.split()
            registers[reg] += 1
            index += 1

        elif line.startswith("dec"):
            _, reg = line.split()
            registers[reg] -= 1
            index += 1

        elif line.startswith("jnz"):
            _, reg, val = line.split()
            if reg.isnumeric():
                if int(reg) != 0:
                    index += int(val)
            elif registers[reg] != 0:
                index += int(val)
            else:
                index += 1

        else:
            raise ValueError(f"Unknown instruction: {line}")

    return registers["a"]


@timeit
def part_one(data):
    return run(data, {"a": 0, "b": 0, "c": 0, "d": 0})


@timeit
def part_two(data):
    return run(data, {"a": 0, "b": 0, "c": 1, "d": 0})


if __name__ == '__main__':
    data = get_line_data("12")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
