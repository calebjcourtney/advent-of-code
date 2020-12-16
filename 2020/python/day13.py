from utils import get_line_data

import numpy
from typing import List, Tuple


def part_one(timestamp: int, busses: List[int]) -> int:
    # keep track of all the busses and where they are
    mapping = [0] * (max(busses) + 1)

    for bus in busses:
        x = 0
        while True:
            if x >= timestamp:
                mapping[bus] = x - timestamp
                break

            x += bus

    return min([x for x in mapping if x != 0]) * mapping.index(min([x for x in mapping if x != 0]))


def is_valid(trb: Tuple[int, int, int]) -> bool:
    time, remainder, bus = trb
    return ((time + remainder) % bus) == 0


def get_base_time(first_val: int) -> int:
    x = 100000000000000
    while x % first_val != 0:
        x += 1

    return x


def fun_brute_force(pairs: List[Tuple[int, int]]):
    mult = pairs[0][1]
    time = get_base_time(mult)

    missing = False
    while not missing:
        print(time, end = "\r")
        time += mult

        missing = all(map(is_valid, [(time, remainder, bus) for remainder, bus in pairs]))

    return time


def part_two(pairs: List[Tuple[int, int]]) -> int:
    # chinese remainder theorem

    # max - product of all the busses
    # convert to int because numpy ints are stupid and was throwing my results off
    N = int(numpy.prod([bus for remainder, bus in pairs]))

    total = 0
    for remainder, bus in pairs:
        # the base for the modular inverse
        base = N // bus

        # the actual modular inverse
        total += remainder * base * (pow(base, bus - 2) % bus)

        # modulo of the product
        total %= N

    return total


if __name__ == '__main__':
    data = get_line_data("13")

    timestamp = int(data[0])
    busses = [int(x) for x in data[1].split(",") if x != "x"]

    p1_result = part_one(timestamp, busses)
    print(p1_result)

    # remainder and the bus id
    busses = [(int(bus) - index, int(bus)) for index, bus in enumerate(data[1].split(",")) if bus != "x"]

    p2_result = part_two(busses)
    print(p2_result)

    pairs = [(index, int(bus)) for index, bus in enumerate(data[1].split(",")) if bus != "x"]
    fun_result = fun_brute_force(pairs)
    print(fun_result)
