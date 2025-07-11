from collections import Counter
from itertools import combinations

from utils import get_line_data
from utils import timeit

from Levenshtein import distance


@timeit
def part_one(data):
    twos = 0
    threes = 0
    for line in data:
        c = Counter(line)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1

    return twos * threes


@timeit
def part_two(data):
    for a, b in combinations(data, 2):
        if distance(a, b) == 1:
            return "".join(a[i] for i in range(len(a)) if a[i] == b[i])


if __name__ == '__main__':
    data = get_line_data("02")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
