from utils import get_data
from utils import timeit

from collections import deque
from typing import NamedTuple


class Rule(NamedTuple):
    key1: str
    op: str
    key2: str
    out: str


def parse_data(data):
    wires = {}
    rules = deque([])

    highest_z = "z00"
    data = data.split("\n")
    for line in data:
        if ":" in line:
            wire, value = line.split(": ")
            wires[wire] = int(value)
        elif "->" in line:
            key1, op, key2, _, out = line.split(" ")
            rules.append(Rule(key1, op, key2, out))
            if out.startswith("z") and int(out[1:]) > int(highest_z[1:]):
                highest_z = out

    return wires, rules, highest_z


def process(op, op1, op2):
    if op == "AND":
        return op1 & op2
    elif op == "OR":
        return op1 | op2
    elif op == "XOR":
        return op1 ^ op2


@timeit
def main(wires, rules, highest_z):
    wrong = set()
    for rule in rules:
        if rule.out[0] == "z" and rule.op != "XOR" and rule.out != highest_z:
            wrong.add(rule.out)
        if all([
            rule.op == "XOR",
            rule.out[0] not in ["x", "y", "z"],
            rule.key1[0] not in ["x", "y", "z"],
            rule.key2[0] not in ["x", "y", "z"],
        ]):
            wrong.add(rule.out)

        if rule.op == "AND" and "x00" not in [rule.key1, rule.key2]:
            for sub in rules:
                if (rule.out == sub.key1 or rule.out == sub.key2) and sub.op != "OR":
                    wrong.add(rule.out)

        if rule.op == "XOR":
            for sub in rules:
                if (rule.out == sub.key1 or rule.out == sub.key2) and sub.op == "OR":
                    wrong.add(rule.out)

    while rules:
        rule = rules.popleft()
        if rule.key1 in wires and rule.key2 in wires:
            wires[rule.out] = process(rule.op, wires[rule.key1], wires[rule.key2])
        else:
            rules.append(Rule(rule.key1, rule.op, rule.key2, rule.out))

    bits = [str(wires[wire]) for wire in sorted(wires, reverse=True) if wire[0] == "z"]
    print(int("".join(bits), 2))
    print(",".join(sorted(wrong)))


if __name__ == '__main__':
    data = get_data("24")
    wires, rules, highest_z = parse_data(data)
    main(wires, rules, highest_z)
