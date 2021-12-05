from utils import get_data

from collections import Counter


def part_one(data):
    c = Counter(data)
    return c["("] - c[")"]


def part_two(data):
    current = 0
    for i, char in enumerate(data, 1):
        current += (1 if char == "(" else -1)

        if current < 0:
            return i


if __name__ == '__main__':
    data = get_data("01")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
