from typing import List

from utils import get_int_data, nwise


def count_increasing(num_list: List):
    return sum(x < y for x, y in nwise(num_list, 2))


if __name__ == '__main__':
    data = get_int_data("01")

    p1_result = count_increasing(data)
    print(p1_result)

    p2_result = count_increasing([sum(x) for x in nwise(data, 3)])
    print(p2_result)
