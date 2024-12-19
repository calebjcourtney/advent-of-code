from utils import get_data
from utils import get_line_data
from utils import get_int_data
from utils import parse_grid
from utils import timeit

from tqdm import tqdm
from functools import lru_cache


@lru_cache
def solve(towels, pattern):
    count = 0

    for towel in towels:
        l = len(towel)
        if towel == pattern:
            count += 1
        elif pattern[:l] == towel:
            sub_count = solve(towels, pattern[l:])
            if sub_count:
                count += sub_count

    return count


def parse_data(data):
    towels, patterns = data.split("\n\n")
    towels = towels.split(", ")
    patterns = patterns.split("\n")

    return towels, patterns


@timeit
def main(towels, patterns):
    designs = []
    for p in patterns:
        sub = [t for t in towels if t in p]
        sub.sort(key=lambda x: len(x), reverse=True)
        sub = tuple(sub)
        designs.append(solve(sub, p))

    print(sum(1 for d in designs if d))
    print(sum(designs))


if __name__ == '__main__':
    data = get_data("19")
    towels, patterns = parse_data(data)

    main(towels, patterns)
