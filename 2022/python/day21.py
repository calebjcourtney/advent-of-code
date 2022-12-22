from utils import get_line_data, get_nums, Point, get_line

from collections import deque
from copy import deepcopy


OP_KEY = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "=": lambda x, y: x == y
}


def eval_line(line, info):
    nums = get_nums(line)
    if nums:
        key = line.split(":")[0]
        if key not in info:
            info[key] = nums[0]

        return True, info

    key, expression = line.split(": ")
    v1, op, v2 = expression.split()
    if v1 not in info or v2 not in info:
        return False, info

    info[key] = OP_KEY[op](info[v1], info[v2])

    return True, info


def run(data: deque, info: dict = dict(), return_key: list = ["root"]):
    while data:
        line = data.popleft()
        success, info = eval_line(line, info)

        if not success:
            data.append(line)

    return [info[x] for x in return_key]


def part_one(data: deque) -> int:
    return int(run(data)[0])


def get_whole_values(data):
    wholes = []
    for x in range(1, 100000):
        if len(wholes) >= 2:
            return wholes

        temp = deepcopy(data)
        output = run(temp, {"humn": x})[0]

        if output == int(output):
            wholes.append(int(output))

    return wholes


def part_two(data: deque):
    humn_1, humn_2 = get_whole_values(data)

    dependencies = [x for x in data if x.startswith("root:")][0]
    _, d1, _, d2 = dependencies.split()

    temp = deepcopy(data)
    x1, y1 = run(temp, {"humn": humn_1}, [d1, d2])

    humn_2 = 11
    temp = deepcopy(data)
    x2, y2 = run(temp, {"humn": humn_2}, [d1, d2])

    slope, constant = get_line(
        Point(humn_1, x1),
        Point(humn_2, x2)
    )

    humn = (y2 - constant) / slope

    for i in range(len(data)):
        if "root:" in data[i]:
            data[i] = data[i].replace("+", "=")

    assert run(data, {"humn": humn})[0]

    return int(humn)


if __name__ == '__main__':
    data = deque(get_line_data("21"))
    data = deque(data)

    p1_result = part_one(data)
    print(p1_result)

    data = deque(get_line_data("21"))
    data = deque(data)
    p2_result = part_two(data)
    print(p2_result)
