from utils import get_data

import numpy
import itertools
from collections import Counter, defaultdict


class Fish:
    def __init__(self, timer):
        self.timer = timer

    def add_day(self):
        if self.timer == 0:
            self.timer = 6

        else:
            self.timer -= 1


def part_one(data):
    fish = []
    for num in data:
        f = Fish(num)
        fish.append(f)

    for _ in range(80):
        new_fish = []
        for f in fish:
            if f.timer == 0:
                new_fish.append(Fish(8))

            f.add_day()

        fish += new_fish

    return len(fish)


# def part_two(data):
#     fish = []
#     for num in data:
#         f = Fish(num)
#         fish.append(f)

#     for _ in range(256):
#         new_fish = []
#         for f in fish:
#             if f.timer == 0:
#                 new_fish.append(Fish(8))

#             f.add_day()

#         fish += new_fish

#         print(len(fish), end = "\r")

#     return len(fish)


def part_two(fish_counter):
    for day in range(256):
        new_fish = defaultdict(int)
        for fish_time, count in fish_counter.items():
            if fish_time == 0:
                new_fish[6] += count
                new_fish[8] += count

            else:
                new_fish[fish_time - 1] += count

        fish_counter = new_fish

    return sum([v for k, v in fish_counter.items()])


if __name__ == '__main__':
    data = get_data("06")
    nums = list(map(int, data.split(",")))
    # nums = [3, 4, 3, 1, 2]

    p1_result = part_one(nums)
    print(p1_result)

    c = Counter(list(map(int, data.split(","))))

    p2_result = part_two(c)
    print(p2_result)
