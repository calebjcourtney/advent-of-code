from utils import get_line_data
from utils import chunks

import string


def val(x):
    mapping = string.ascii_lowercase + string.ascii_uppercase
    return mapping.index(x) + 1


def overlap_char(line):
    first, second = line[:len(line) // 2], line[len(line) // 2:]
    return list(set(first) & set(second))[0]


def part_one(data):
    return sum(map(val, map(overlap_char, data)))


def get_common_group_letter(group):
    return list(set(group[0]) & set(group[1]) & set(group[2]))[0]


def part_two(groups):
    return sum(map(val, map(get_common_group_letter, groups)))


if __name__ == '__main__':
    data = get_line_data("03")

    p1_result = part_one(data)
    print(p1_result)

    groups = chunks(data, 3)
    p2_result = part_two(groups)
    print(p2_result)
