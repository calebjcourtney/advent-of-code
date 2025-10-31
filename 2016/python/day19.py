from utils import get_data
from utils import timeit

from collections import deque



@timeit
def part_one(data):
    elves = deque(range(1, data + 1))
    while len(elves) > 1:
        elves.rotate(-1)
        elves.popleft()

    return elves[0]


@timeit
def part_two(data):
    left_elves = deque(range(1, (data // 2) + 1))
    right_elves = deque(range((data // 2) + 1, data + 1))

    while len(left_elves) + len(right_elves) > 1:
        right_elves.popleft()
        right_elves.append(left_elves.popleft())
        if len(right_elves) - len(left_elves) == 2:
            left_elves.append(right_elves.popleft())

    return right_elves[0]


@timeit
def main():
    data = int(get_data("19"))

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
