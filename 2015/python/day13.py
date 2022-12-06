from utils import get_line_data

from itertools import permutations
from collections import defaultdict

import re


def parse_line(line):
    p1 = line.split()[0]
    p2 = line.split()[-1].replace(".", "")
    modifier = "gain" if "gain" in line else "lose"
    amount = int(re.findall(r"\d+", line)[0])

    return p1, p2, (-amount if modifier == "lose" else amount)


def parse_data(data):
    output = defaultdict(lambda: defaultdict(int))
    for line in data:
        p1, p2, amount = parse_line(line)
        output[p1][p2] = amount

    return output


def solve(data):
    names = list(data.keys())
    best = -100000
    for people in permutations(names, len(names)):
        temp = 0
        for p1, p2 in zip(people, list(people[1:]) + [people[0]]):
            temp += data[p1][p2]
            temp += data[p2][p1]

        if temp > best:
            best = temp

    return best


if __name__ == '__main__':
    data = get_line_data("13")
    data = parse_data(data)

    p1_result = solve(data)
    print(p1_result)

    names = list(data.keys())
    for name in names:
        data["me"][name] = 0
        data[name]["me"] = 0

    p2_result = solve(data)
    print(p2_result)
