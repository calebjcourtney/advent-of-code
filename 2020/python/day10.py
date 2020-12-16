from typing import List

from utils import get_int_data


def part_one(data: List[str]) -> int:
    """
    A shorter solution, but more difficult to comprehend at first glance:
        processed = [data[x] - data[x - 1] for x in range(len(data))] + [3]
        return processed.count(1) * processed.count(3)
    """

    ones = 1
    threes = 1
    for x in range(1, len(data)):
        if data[x] - data[x - 1] == 1:
            ones += 1

        elif data[x] - data[x - 1] == 3:
            threes += 1

        else:
            raise ValueError("You did something wrong. There should only be ones and threes.")

    return ones * threes


# props to AltNyx for this elegant solution
def part_two(data: List[str]) -> int:
    # there's always at least one way to do this (so we start with 1)
    # also, from the example, the length of each arrangment is shorter than the max (last) value in the list
    points = [1] + [0] * (data[-1])

    # as we go through the numbers, we can track the number of distinct times the individual branch is used as part of the previous branches
    # then we use those values to add to the next branch
    for r in data:
        points[r] = points[r - 1] + points[r - 2] + points[r - 3]

    # the last value will be the result
    return points[-1]


if __name__ == '__main__':
    data = get_int_data("10")

    # both parts assume the data is in sorted order
    data.sort()

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
