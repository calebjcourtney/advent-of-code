from utils import get_line_data
from utils import timeit


def parse_data(data):
    return sorted([tuple(map(int, line.split("-"))) for line in data], key=lambda x: x[0])


@timeit
def part_one(data):
    current_min = data[0][0]
    current_max = data[0][1]
    for start, end in data[1:]:
        if start <= current_max + 1:
            current_max = max(current_max, end)
        else:
            return current_max + 1

    return current_max + 1


@timeit
def part_two(data):
    total = 0
    current_min = data[0][0]
    current_max = data[0][1]
    for start, end in data[1:]:
        if start <= current_max + 1:
            current_max = max(current_max, end)
        else:
            total += start - current_max - 1
            current_min = start
            current_max = end

    return total


@timeit
def main():
    data = get_line_data("20")
    data = parse_data(data)

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
