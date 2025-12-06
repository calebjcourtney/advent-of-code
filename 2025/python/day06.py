from utils import get_line_data
from utils import timeit
from utils import get_nums
from utils import rotated
from utils import mult

from typing import NamedTuple

class Problem(NamedTuple):
    numbers: list[int]
    operator: str

    def solve(self):
        if self.operator == '+':
            return sum(self.numbers)
        elif self.operator == '*':
            return mult(self.numbers)


@timeit
def part_one(data):
    nums_data = []
    for line in data:
        nums = get_nums(line)
        if nums:
            nums_data.append(nums)
        else:
            operators = line.split()

    rotated_data = rotated(nums_data)
    problems = [Problem(numbers=numbers, operator=operator) for numbers, operator in zip(rotated_data, operators)]

    return sum(problem.solve() for problem in problems)


@timeit
def part_two(data):
    operators = data[-1].split()[::-1]
    num_rows = data[:-1]
    rotated_data = rotated(rotated(rotated(num_rows)))
    problems = []
    current_operator = operators.pop(0)
    group_idx = 0
    while True:
        group_numbers = []
        while group_idx < len(rotated_data):
            if all(char.strip() == '' for char in rotated_data[group_idx]):
                group_idx += 1
                break
            else:
                group_numbers.append(int(''.join(x for x in rotated_data[group_idx] if x.isdigit())))
                group_idx += 1

        problems.append(Problem(numbers=group_numbers, operator=current_operator))
        if operators:
            current_operator = operators.pop(0)
        else:
            break

    return sum(problem.solve() for problem in problems)


@timeit
def main():
    data = get_line_data("06")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
