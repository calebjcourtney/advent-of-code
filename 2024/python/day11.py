from utils import get_data
from utils import get_nums
from utils import timeit

from collections import Counter


def get_new(num: int):
    if num == 0:
        return 1, None
    elif len(str(num)) % 2 == 0:
        return int(str(num)[:len(str(num))//2]), int(str(num)[len(str(num))//2:])
    else:
        return num * 2024, None


@timeit
def solve(counter, cycles):
    for _ in range(cycles):
        tmp = Counter()
        for key, value in counter.items():
            f, s = get_new(key)
            tmp[f] += value
            if s:
                tmp[s] += value

        counter = tmp

    return counter


if __name__ == '__main__':
    data = get_data("11")
    nums = get_nums(data)
    counter = Counter(nums)

    counter = solve(counter, 25)
    print(sum(counter.values()))

    counter = solve(counter, 50)
    print(sum(counter.values()))
