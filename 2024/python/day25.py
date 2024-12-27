from utils import get_data
from utils import parse_grid
from utils import timeit
from utils import Point

from collections import Counter

def parse_data(data):
    records = data.split("\n\n")

    keys: list[Counter] = []
    locks: list[Counter] = []

    for record in records:
        grid = parse_grid(record, keep_values="#")

        heights = Counter(point.x for point in grid.keys())

        if Point(0, 0) in grid:
            keys.append(heights)
        else:
            locks.append(heights)

    return keys, locks


def no_overlap(key, lock):
    for x in range(6):
        if key[x] + lock[x] > 7:
            return False

    return True


@timeit
def part_one(keys, locks):
    output = 0
    for key in keys:
        for lock in locks:
            output += no_overlap(key, lock)

    return output


if __name__ == '__main__':
    data = get_data("25")
    keys, locks = parse_data(data)

    p1_result = part_one(keys, locks)
    print(p1_result)
