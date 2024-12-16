from utils import get_data
from utils import timeit
from utils import Point

import re


a_pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
b_pattern = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
p_pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")

def parse_line(line):
    a_match = a_pattern.match(line)
    b_match = b_pattern.match(line)
    p_match = p_pattern.match(line)

    if a_match:
        return "A", int(a_match.group(1)), int(a_match.group(2))
    elif b_match:
        return "B", int(b_match.group(1)), int(b_match.group(2))
    elif p_match:
        return "P", int(p_match.group(1)), int(p_match.group(2))
    else:
        raise ValueError(f"Could not parse line: {line}")


def solve(p: Point, a: Point, b: Point) -> int:
    total = 0
    ca = (p.x * b.y - p.y * b.x) / (a.x * b.y - a.y * b.x)
    cb = (p.x - a.x * ca) / b.x
    if int(ca) == ca and int(cb) == cb:
        total += int(ca * 3 + cb)

    return total


@timeit
def main(machines):
    p1 = 0
    p2 = 0
    for machine in machines:
        a = Point(machine[0][1], machine[0][2])
        b = Point(machine[1][1], machine[1][2])
        p = Point(machine[2][1], machine[2][2])

        p1 += solve(p, a, b)

        p = Point(p.x + 10000000000000, p.y + 10000000000000)
        p2 += solve(p, a, b)

    print(p1)
    print(p2)


if __name__ == '__main__':
    data = get_data("13")
    machines = data.split("\n\n")
    machines = [
        [
            parse_line(line)
            for line in machine.split("\n")
            if line.strip() != ""
        ]
        for machine in machines
    ]

    main(machines)
