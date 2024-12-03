from utils import get_data
from utils import timeit

import re

pattern = re.compile(r"mul\((\d+),(\d+)\)")
remove = re.compile(r"don\'t\(\).*?do\(\)")


def get_muls(record: str):
    return sum([
        int(match.group(1)) * int(match.group(2))
        for match in pattern.finditer(record)
    ])


@timeit
def main(data: str):
    print("Part 1:", get_muls(data))
    data = remove.sub("", data)
    if "don't" in data:
        data = data[:data.index("don't")]

    print("Part 2:", get_muls(data))


if __name__ == '__main__':
    data = get_data("03").replace("\n", "")
    main(data)
