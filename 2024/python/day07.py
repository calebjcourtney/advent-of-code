from utils import get_line_data
from utils import timeit
from utils import get_nums

from collections import deque

from typing import NamedTuple


class Record(NamedTuple):
    test_value: int
    values: list[int]

    def part_one(self):
        eval_options = ["+", "*"]
        options = deque([(self.values[0], 1)])
        while options:
            val, index = options.popleft()
            if val == self.test_value and index == len(self.values):
                return True

            if index >= len(self.values):
                continue

            for ev in eval_options:
                if ev == "+":
                    temp = val + self.values[index]
                elif ev == "*":
                    temp = val * self.values[index]

                options.append((temp, index + 1))

        return False

    def part_two(self):
        eval_options = ["+", "*", "||"]
        options = deque([(self.values[0], 1)])
        while options:
            val, index = options.popleft()
            if val == self.test_value and index == len(self.values):
                return True

            if index >= len(self.values):
                continue

            for ev in eval_options:
                if ev == "+":
                    temp = val + self.values[index]
                elif ev == "*":
                    temp = val * self.values[index]
                elif ev == "||":
                    temp = int(str(val) + str(self.values[index]))

                options.append((temp, index + 1))

        return False


def parse_data(record: str) -> list[Record]:
    nums = get_nums(record)
    return Record(nums[0], nums[1:])


@timeit
def part_one(data: list[Record]):
    return sum(record.test_value for record in data if record.part_one())


@timeit
def part_two(data):
    return sum(record.test_value for record in data if record.part_two())


if __name__ == '__main__':
    data = list(map(parse_data, get_line_data("07")))

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
