from utils import get_data
from utils import timeit

from collections import defaultdict
import hashlib
import re
from functools import lru_cache
from typing import Callable


@lru_cache
def generate_md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()


@lru_cache
def stretched_md5(salt):
    h = generate_md5_hash(salt)
    for _ in range(2016):
        h = generate_md5_hash(h)

    return h


def has_three_peat(h):
    res = re.search(r'(.)\1{2}', h)
    return None if res is None else res.group(0)[0]


def has_five_peat(h):
    return set(re.findall(r'(.)\1{4}', h))


def has_repeaters(h, count=3):
    return {3: has_three_peat, 5: has_five_peat}[count](h)


def valid_key_indexes(threes: set[int], fives: set[int]) -> set[int]:
    output = set()
    for x in threes:
        for y in fives:
            if 1 <= y - x <= 1000:
                output.add(x)
                continue

    return output


@timeit
def run(data, func: Callable):
    three_peats = defaultdict(set)
    five_peats = defaultdict(set)
    for x in range(100000):
        h = func(f"{data}{x}")
        l = has_repeaters(h)
        if l is not None:
            three_peats[l].add(x)

        for l in has_repeaters(h, 5):
            five_peats[l].add(x)

    keys = set()
    for key in three_peats.keys():
        keys |= valid_key_indexes(three_peats[key], five_peats.get(key, set()))

    keys = list(keys)
    keys.sort()

    return keys[63]


if __name__ == '__main__':
    data = get_data("14")

    p1_result = run(data, generate_md5_hash)
    print(p1_result)

    p2_result = run(data, stretched_md5)
    print(p2_result)
