from utils import get_line_data, find_parentheses


def eval_part_one(line: str) -> int:
    # eval in order
    evals = line.split()

    # eval three ops at a time
    cur = evals[0]
    for index in range(2, len(evals), 2):
        cur = eval("".join([str(cur)] + evals[index - 1:index + 1]))

    return cur


def part_one(line: str) -> int:
    parentheses_locs = find_parentheses(line)

    while len(parentheses_locs) > 0:
        new_line = ""
        start, end = parentheses_locs[0]

        new_line = line[:start]

        new_val = eval_part_one(line[start + 1: end])
        new_line += str(new_val)

        new_line += line[end + 1:]

        line = new_line[:]
        parentheses_locs = find_parentheses(line)

    return eval_part_one(line)


def eval_part_two(line: str) -> int:
    evals = line.split()

    # evaluate the plus signs first
    while "+" in evals:
        first_plus = evals.index("+")

        new_evals = evals[:first_plus - 1]

        new_val = eval("".join(evals[first_plus - 1:first_plus + 2]))
        new_evals.append(str(new_val))

        new_evals += evals[first_plus + 2:]

        evals = new_evals[:]

    # then we can just eval the mults
    return eval("".join(evals))


def part_two(line: str) -> int:
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

    return eval_part_two(line)


if __name__ == '__main__':
    data = get_line_data("18")

    # combine all the lines into one
    data = "(" + ") + (".join(data) + ")"

    print(part_one(data))
    print(part_two(data))
