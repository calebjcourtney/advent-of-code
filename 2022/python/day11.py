import copy
from collections import defaultdict
from typing import List, Any

from utils import get_data, get_nums, mult


def parse_monkeys(data: str) -> List[Any]:
    monkeys = []
    for monkey in data.split("\n\n"):
        m = monkey.splitlines()
        items = get_nums(m[1])
        operation = m[2].split(': ')[1]
        divisor = get_nums(m[3])[0]
        if_true = get_nums(m[4])[0]
        if_false = get_nums(m[5])[0]
        monkeys.append([items, operation, divisor, if_true, if_false])

    return monkeys


def run(monkeys: List[Any], num_turns: int, func) -> int:
    monkeys = copy.deepcopy(monkeys)
    counts = defaultdict(int)

    for turn in range(num_turns):
        for i, (items, operation, divisor, if_true, if_false) in enumerate(monkeys):
            for _ in range(len(items)):
                counts[i] += 1
                item = monkeys[i][0].pop(0)
                op, val = operation.split()[-2:]
                if val == 'old':
                    val = item
                else:
                    val = int(val)

                if op == "*":
                    item *= val
                elif op == "+":
                    item += val

                item = func(item)

                next_monkey = if_true if item % divisor == 0 else if_false
                monkeys[next_monkey][0].append(item)

    inspections = list(sorted(counts.values()))
    return inspections[-2] * inspections[-1]


if __name__ == '__main__':
    # Parse input.
    data = get_data("11")

    monkeys = parse_monkeys(data)

    # Solve problem.
    print("Part 1:", run(monkeys, 20, lambda x: x // 3))
    print("Part 2:", run(
        monkeys, 10000,
        lambda x: x % mult(m[2] for m in monkeys)
    ))
