from utils import get_int_data

import numpy
import itertools


def prod_of_sum(data: list, i: int) -> int:
    for a in itertools.permutations(data, i):
        if sum(a) == 2020:
            return numpy.prod(a)


if __name__ == '__main__':
    data = get_int_data("01")

    print(prod_of_sum(data, 2))
    print(prod_of_sum(data, 3))
