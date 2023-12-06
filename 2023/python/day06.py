from math import prod

from utils import get_line_data


def solve(time, record):
    # quadratic
    upper_limit = (time + (time ** 2 - 4 * record) ** 0.5) // 2
    lower_limit = (time - (time ** 2 - 4 * record) ** 0.5) // 2

    # handle the rounding issues
    for x in range(int(lower_limit) - 2, int(lower_limit) + 2):
        if x * (time - x) > record:
            lb = x
            break

    for x in range(int(upper_limit) - 2, int(upper_limit) + 2):
        if x * (time - x) < record:
            ub = x
            break

    return ub - lb


def part_one(data):
    times = list(map(int, data[0].split(":")[1].split()))
    records = list(map(int, data[1].split(":")[1].split()))

    return prod(solve(t, d) for t, d in zip(times, records))


def part_two(data):
    time = int("".join(data[0].split(":")[1].strip().split()))
    record = int("".join(data[1].split(":")[1].strip().split()))

    return solve(time, record)


if __name__ == '__main__':
    data = get_line_data("06")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
