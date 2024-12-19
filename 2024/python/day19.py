from functools import lru_cache

from utils import get_data
from utils import timeit


@lru_cache
def solve(towels: list[str], pattern: str) -> int:
    count = 0
    for towel in towels:
        if towel == pattern:
            count += 1
        elif pattern[:len(towel)] == towel:
            count += solve(towels, pattern[len(towel):])

    return count


@timeit
def main(towels: list[str], patterns: list[str]) -> None:
    designs = [solve(tuple(t for t in towels if t in p), p) for p in patterns]
    print("Part 1:", sum(1 for d in designs if d))
    print("Part 2:", sum(designs))


if __name__ == '__main__':
    data = get_data("19")
    towels, patterns = data.split("\n\n")
    towels = towels.split(", ")
    patterns = patterns.split("\n")

    main(towels, patterns)
