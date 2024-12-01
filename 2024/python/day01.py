from collections import Counter

from utils import get_line_data
from utils import get_nums
from utils import timeit


def parse_data(data):
    lefts = []
    rights = []
    for line in data:
        left, right = get_nums(line)
        lefts.append(left)
        rights.append(right)

    return lefts, rights


@timeit
def part_one(lefts: list[str], rights: list[str]) -> int:
    lefts = list(map(int, lefts))
    rights = list(map(int, rights))

    lefts.sort()
    rights.sort()

    output = 0

    for left, right in zip(lefts, rights):
        output += abs(left - right)

    return output


@timeit
def part_two(lefts: list[str], rights: list[str]):
    lefts = Counter(lefts)
    rights = Counter(rights)

    output = 0
    for x in set(lefts.keys()) | set(rights.keys()):
        output += int(x) * lefts[x] * rights[x]

    return output

if __name__ == '__main__':
    data = get_line_data("01")
    lefts, rights = parse_data(data)
    print(part_one(lefts, rights))
    print(part_two(lefts, rights))
