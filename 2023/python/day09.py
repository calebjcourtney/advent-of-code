from utils import get_line_data
from utils import timeit


def extrapolate_vals(nums: list[int]):
    diff_vals = [nums]
    while sum(diff_vals[-1]) != 0:
        diff_vals.append([diff_vals[-1][i] - diff_vals[-1][i - 1] for i in range(1, len(diff_vals[-1]))])

    return sum(row[-1] for row in diff_vals)


@timeit
def part_one(data):
    return sum(extrapolate_vals(row) for row in data)


@timeit
def part_two(data):
    return sum(extrapolate_vals(row[::-1]) for row in data)


if __name__ == '__main__':
    data = get_line_data("09")
    data = [list(map(int, line.split())) for line in data]

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
