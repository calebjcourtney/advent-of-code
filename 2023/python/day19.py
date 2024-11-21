from utils import get_data
from utils import timeit
from utils import mult

import re
from collections import deque
import copy


class Part:
    def __init__(self, line: str):
        pattern = re.compile(r"(\w+)=(\d+)")
        matches = pattern.findall(line)
        self.x = int(matches[0][1])
        self.m = int(matches[1][1])
        self.a = int(matches[2][1])
        self.s = int(matches[3][1])

    @property
    def value(self):
        return self.x + self.m + self.a + self.s


class Workflow:
    def __init__(self, line: str):
        self.name, rule = line.split(r"{")
        self.rule = rule[:-1]

    def get_destination(self, part: Part):
        rules = self.rule.split(",")
        el = rules[-1]

        for rule in rules[:-1]:
            r, destination = rule.split(":")
            if eval(r, {}, {"x": part.x, "m": part.m, "a": part.a, "s": part.s}):
                return destination

        return el

    @property
    def rules(self):
        return self.rule.split(",")


def part_is_accepted(part, workflows: dict[str, Workflow]):
    current = "in"
    while current not in ["A", "R"]:
        wf = workflows[current]
        current = wf.get_destination(part)

    return current == "A"


@timeit
def part_one(parts: list[Part], workflows: dict[str, Workflow]):
    return sum([part.value for part in parts if part_is_accepted(part, workflows)])


@timeit
def part_two(rules):
    INITIAL_HYPERCUBE = {k: [1, 4000] for k in "xmas"}
    horizon = [("in", INITIAL_HYPERCUBE)]

    ACCEPTED = deque([])

    while horizon:
        curr, intervals = horizon.pop()

        if curr == "A":
            ACCEPTED.append(intervals)
            continue
        elif curr == "R":
            continue

        for rule in rules[curr].rules:
            if isinstance(rule, str):
                horizon.append((rule, intervals))
                break

            reg, cond, val, next_rule = rule
            if cond == "<":
                if intervals[reg][0] >= val:
                    continue

                curr_bound = intervals[reg][1]
                new_intervals = copy.deepcopy(intervals)
                new_intervals[reg][1] = min(val - 1, curr_bound)
                horizon.append((next_rule, copy.deepcopy(new_intervals)))

                # Propagate the inverse state to the next case in the rule.
                curr_bound = intervals[reg][0]
                inverse_intervals = copy.deepcopy(intervals)
                inverse_intervals[reg][0] = max(val, curr_bound)
                intervals = inverse_intervals

            elif cond == ">":
                if intervals[reg][1] <= val:
                    continue

                curr_bound = intervals[reg][0]
                new_intervals = copy.deepcopy(intervals)
                new_intervals[reg][0] = max(val + 1, curr_bound)
                horizon.append((next_rule, copy.deepcopy(new_intervals)))

                # Propagate the inverse state to the next case in the rule.
                curr_bound = intervals[reg][1]
                inverse_intervals = copy.deepcopy(intervals)
                inverse_intervals[reg][1] = min(val, curr_bound)
                intervals = inverse_intervals

    return sum(mult(b - a + 1 for a, b in interval.values()) for interval in ACCEPTED),


if __name__ == "__main__":
    wf, parts = get_data("19").split("\n\n")

    parts = [Part(line) for line in parts.split("\n")]
    workflows = {line.split("{")[0]: Workflow(line) for line in wf.split("\n")}

    p1_result = part_one(parts, workflows)
    print(p1_result)

    p2_result = part_two(workflows)
    print(p2_result)
