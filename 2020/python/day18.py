from utils import get_line_data


# Modified from here: https://scipython.com/blog/parenthesis-matching-in-python/
# Might add this to my utils later
def find_parentheses(line):
    stack = []
    parentheses_locs = []
    for i, c in enumerate(line):
        if c == '(':
            stack.append(i)
        elif c == ')':
            try:
                parentheses_locs.append((stack.pop(), i))
            except IndexError:
                raise IndexError('Too many close parentheses at index {}'.format(i))
    if stack:
        raise IndexError('No matching close parenthesis to open parenthesis '
                         'at index {}'.format(stack.pop()))

    return parentheses_locs


def eval_expression(line):
    # eval in order
    if len(line.split()) == 3:
        return int(eval(line))

    evals = line.split()

    if len(evals) == 3:
        return eval(line)

    cur = None
    for index in range(2, len(evals), 2):
        if cur is None:
            cur = int(eval(" ".join(evals[index - 2:index + 1])))

        else:
            cur = int(eval(" ".join([str(cur)] + evals[index - 1:index + 1])))

    return int(cur)


def part_one(data):
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


def eval_part_two(line):
    evals = line.split()

    if len(evals) == 3:
        return eval(line)

    while "+" in evals:
        first_plus = evals.index("+")

        new_evals = evals[:first_plus - 1]

        new_val = int(eval(" ".join(evals[first_plus - 1:first_plus + 2])))
        new_evals.append(str(new_val))

        new_evals += evals[first_plus + 2:]

        evals = new_evals[:]

    while "*" in evals:
        first_mult = evals.index("*")

        new_evals = evals[:first_mult - 1]

        new_val = int(eval(" ".join(evals[first_mult - 1:first_mult + 2])))
        new_evals.append(str(new_val))

        new_evals += evals[first_mult + 2:]

        evals = new_evals[:]

    return int(evals[0])


def part_two(data):
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
