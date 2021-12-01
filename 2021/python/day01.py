from typing import List

from utils import get_int_data


def part_one(data: List[int]) -> int:
    count = 0
    for x, y in zip(data, data[1:]):
        if y > x:
            count += 1

    return count


def part_two(data: List[int]) -> int:
    count = 0
    first = data[0], data[1], data[2]
    for second in zip(data[1:], data[2:], data[3:]):
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
