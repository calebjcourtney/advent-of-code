from utils import get_data
from utils import timeit

import re

pattern = re.compile(r"mul\((\d+),(\d+)\)")
remove = re.compile(r"don\'t\(\).*?do\(\)")



@timeit
def get_muls(record: str):
    return sum([
        int(match.group(1)) * int(match.group(2))
        for match in pattern.finditer(record)
    ])


def part_two(data):
    data = remove.sub("", data)
    if "don't" in data:
        data = data[:data.index("don't")]

    return get_muls(data)


if __name__ == '__main__':
    # new lines are dumb
    data = get_data("03").replace("\n", "")

    print(get_muls(data))

    p2_result = part_two(data)
    print(p2_result)
