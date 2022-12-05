from utils import get_line_data

import re
import numpy as np


def parse_line(line):
    instruction = "toggle"
    if line.startswith("turn"):
        instruction = "on" if "on" in line else "off"

    start_x, start_y, end_x, end_y = map(int, re.findall(r"\d+", line))

    return instruction, start_x, start_y, end_x, end_y


def part_one(data):
    output = np.zeros((1000, 1000), dtype=int)
    for line in data:
        instruction, start_x, start_y, end_x, end_y = parse_line(line)

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if instruction == "on":
                    output[x][y] = 1

                if instruction == "off":
                    output[x][y] = 0

                if instruction == "toggle":
                    output[x][y] ^= 1

    return output.sum()


def part_two(data):
    output = np.zeros((1000, 1000), dtype=int)
    for line in data:
        instruction, start_x, start_y, end_x, end_y = parse_line(line)

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if instruction == "on":
                    output[x][y] += 1

                if instruction == "off":
                    output[x][y] -= 1
                    output[x][y] = max(output[x][y], 0)

                if instruction == "toggle":
                    output[x][y] += 2

    return output.sum()


if __name__ == '__main__':
    data = get_line_data("06")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
