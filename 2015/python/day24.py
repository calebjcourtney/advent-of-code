from utils import get_int_data

import math
import itertools


def get_groups_sum_to(target, nums):
    nums.sort(reverse=True)
    groups = []
    for x in range(target // max(nums) + 1, len(nums)):
        if groups:
            break

        for group in itertools.combinations(nums, x):
            if sum(group) == target:
                groups.append(group)

    return groups


def main(val, data):
    return min(
        math.prod(g)
        for g in get_groups_sum_to(sum(data) // val, data)
    )


if __name__ == '__main__':
    data = get_int_data("24")

    p1_result = main(3, data)
    print(p1_result)

    p2_result = main(4, data)
    print(p2_result)
