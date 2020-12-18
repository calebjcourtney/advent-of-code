from utils import get_line_data

from typing import List, Tuple


# Might add this to my utils later
def find_parentheses(line: str) -> List[Tuple[int, int]]:
    stack = []
    parentheses_locs = []
    for index, character in enumerate(line):
        if character == '(':
            stack.append(index)
        elif character == ')':
            parentheses_locs.append((stack.pop(), index))

    return parentheses_locs


def eval_expression(line: str) -> int:
    # eval in order
    if len(line.split()) == 3:
        return int(eval(line))

    evals = line.split()

    if len(evals) == 3:
        return eval(line)

    cur = evals[0]
    for index in range(2, len(evals), 2):
        cur = int(eval("".join([str(cur)] + evals[index - 1:index + 1])))

    return int(cur)


def part_one(data: List[str]) -> int:
    total = 0
    for line in data:
        parentheses_locs = find_parentheses(line)

        while len(parentheses_locs) > 0:
            new_line = ""
            start, end = parentheses_locs[0]

            new_line = line[:start]

            new_val = eval_expression(line[start + 1: end])
            new_line += str(new_val)

            new_line += line[end + 1:]

            line = new_line[:]
            parentheses_locs = find_parentheses(line)

        total += eval_expression(line)

    return total


def eval_part_two(line: str) -> int:
    evals = line.split()

    if len(evals) == 3:
        return eval(line)

    # evaluate the plus signs first
    while "+" in evals:
        first_plus = evals.index("+")

        new_evals = evals[:first_plus - 1]

        new_val = int(eval("".join(evals[first_plus - 1:first_plus + 2])))
        new_evals.append(str(new_val))

        new_evals += evals[first_plus + 2:]

        evals = new_evals[:]

    # then we can just eval the mults
    return int(eval("".join(evals)))


def part_two(data: List[str]) -> int:
    total = 0
    for line in data:
        parentheses_locs = find_parentheses(line)

        while len(parentheses_locs) > 0:
            new_line = ""
            start, end = parentheses_locs[0]

            new_line = line[:start]

            new_val = eval_part_two(line[start + 1: end])
            new_line += str(new_val)

            new_line += line[end + 1:]

            line = new_line[:]
            parentheses_locs = find_parentheses(line)

        total += eval_part_two(line)

    return total


if __name__ == '__main__':
    data = get_line_data("18")

    p1_result = part_one(data)
    print(f"Part 1: {p1_result}")

    p2_result = part_two(data)
    print(f"Part 2: {p2_result}")
