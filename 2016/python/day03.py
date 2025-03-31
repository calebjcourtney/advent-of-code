from utils import get_line_data
from utils import get_nums
from utils import timeit


def is_valid_triangle(vals):
    a, b, c = vals
    return (a + b > c) and (a + c > b) and (b + c > a)


@timeit
def part_one(data):
    return sum(
        is_valid_triangle(get_nums(line))
        for line in data
    )


def parse_p2(data):
    out = []
    for i in range(0, len(data), 3):
        first = get_nums(data[i])
        second = get_nums(data[i + 1])
        third = get_nums(data[i + 2])

        out.extend([
            [first[0], second[0], third[0]],
            [first[1], second[1], third[1]],
            [first[2], second[2], third[2]],
        ])

    return out


@timeit
def part_two(data):
    p2_data = parse_p2(data)
    return sum(
        is_valid_triangle(line)
        for line in p2_data
    )

if __name__ == '__main__':
    data = get_line_data("03")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
