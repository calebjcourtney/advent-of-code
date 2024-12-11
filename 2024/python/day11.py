from utils import get_data
from utils import get_nums
from utils import timeit

from collections import deque
from collections import Counter
from tqdm import tqdm

from functools import lru_cache


def get_new(num: int):
    output = deque([])
    if num == 0:
        output.append(1)
    elif len(str(num)) % 2 == 0:
        output.append(int(str(num)[:len(str(num))//2]))
        output.append(int(str(num)[len(str(num))//2:]))
    else:
        output.append(num * 2024)

    return output


@timeit
def solve(counter, cycles):
    for _ in range(cycles):
        tmp = Counter()
        for key, value in counter.items():
            new_nums = get_new(key)
            for n in new_nums:
                tmp[n] += value

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
