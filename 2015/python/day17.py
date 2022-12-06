from utils import get_int_data

import itertools
from collections import defaultdict


def part_one(data):
    amount = 150
    found = 0
    for x in range(1, len(data) + 1):
        for nums in itertools.combinations(data, x):
            found += int(sum(nums) == amount)

    return found


def part_two(data):
    amount = 150
    found = defaultdict(int)
    for x in range(1, len(data) + 1):
        for nums in itertools.combinations(data, x):
            if sum(nums) == amount:
                found[len(nums)] += 1

    return max(value for key, value in found.items() if key == min(found.keys()))


if __name__ == '__main__':
    data = get_int_data("17")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
