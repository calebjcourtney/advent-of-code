from utils import get_data

import re
import json


def part_one(data):
    return sum(map(int, re.findall(r"-?\d+", data)))


def part_two(x):
    s = 0

    if isinstance(x, list):
        for y in x:
            if isinstance(y, int):
                s += y
            else:
                s += part_two(y)
    elif isinstance(x, dict):
        for k in x.keys():
            if x[k] == 'red':
                return 0
            s += part_two(x[k])
    elif isinstance(x, int):
        return x

    return s


if __name__ == '__main__':
    data = get_data("12")

    # data = """{"e":86,"c":23,"a":{"a":[120,169,"green","red","orange"],"b":"red"}}"""

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(json.loads(data))
    print(p2_result)
