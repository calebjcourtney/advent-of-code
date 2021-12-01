from typing import List

from more_itertools import windowed

from utils import get_int_data


def part_one(data: List[int]) -> int:
    count = 0
    for x, y in windowed(data, 2):
        if x < y:
            count += 1

    return count


def part_two(data: List[int]) -> int:
    count = 0
    first = data[:2]
    for second in windowed(data[1:], 3):
        if sum(first) < sum(second):
            count += 1

        first = second

    return count


if __name__ == '__main__':
    data = get_int_data("01")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
