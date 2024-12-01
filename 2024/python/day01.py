from collections import Counter

from utils import get_line_data
from utils import get_nums
from utils import timeit


@timeit
def part_one(data: tuple[str, str]) -> int:
    lefts = sorted(list(map(int, [x[0] for x in data])))
    rights = sorted(list(map(int, [x[1] for x in data])))

    return sum([abs(x - y) for x, y in zip(lefts, rights)])


@timeit
def part_two(data: tuple[str, str]):
    lefts = Counter([x[0] for x in data])
    rights = Counter([x[1] for x in data])

    return sum([
        int(x) * lefts[x] * rights[x]
        for x in set(lefts.keys()) | set(rights.keys())
    ])


if __name__ == '__main__':
    data = [get_nums(line) for line in get_line_data("01")]
    print(part_one(data))
    print(part_two(data))
