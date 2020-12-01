import numpy
import itertools


def prod_of_sum(data: list, i: int):
    for a in itertools.permutations(data, i):
        if sum(a) == 2020:
            return numpy.prod(a)


if __name__ == '__main__':
    data = list(map(int, open("input01.txt").read().split()))
    # part 1
    print(prod_of_sum(data, 2))
    # part 2
    print(prod_of_sum(data, 3))
