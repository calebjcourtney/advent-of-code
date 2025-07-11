import itertools

from utils import get_int_data
from utils import timeit


@timeit
def part_one(data):
    return sum(data)


@timeit
def part_two(data):
    frequencies = set()
    current_frequency = 0
    for num in itertools.cycle(data):
        current_frequency += num
        if current_frequency in frequencies:
            return current_frequency
        frequencies.add(current_frequency)


if __name__ == '__main__':
    data = get_int_data("01")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
