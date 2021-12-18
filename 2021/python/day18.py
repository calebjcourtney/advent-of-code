from utils import get_line_data

import json
from copy import deepcopy
import itertools


def is_list(lst):
    return isinstance(lst, list)


def magnitude(lst):
    l1, l2 = lst
    if is_list(l1):
        l1 = magnitude(l1)

    if is_list(l2):
        l2 = magnitude(l2)

    return 3 * l1 + 2 * l2


def reduce(array):
    array = deepcopy(array)

    cont = True

    # explode
    while cont:

        cont = False

        # this has been used so often for the last several days
        stack = [(0, array, [])]

        while stack:
            depth, value, p = stack.pop()

            if not is_list(value):
                continue

            # depth is greater than 4
            if depth >= 4:
                for a, index in p:

                    # get the right-most number to the left of the exploding value
                    if index > 0:
                        while is_list(a[index - 1]):
                            a = a[index - 1]
                            index = len(a)

                        # add the value
                        a[index - 1] += value[0]

                        break

                # get the left-most number to the right of the exploding value
                for a, index in p:
                    if index < len(a) - 1:
                        while is_list(a[index + 1]):
                            a = a[index + 1]
                            index = -1

                        # add the value
                        a[index + 1] += value[1]

                        break

                p[0][0][p[0][1]] = 0
                cont = True

                break

            else:
                # add index and value bakck into the stack
                for i, sub in list(enumerate(value))[::-1]:
                    stack.append((depth + 1, sub, [[value, i]] + p))

        if cont:
            continue

        # split
        stack = [(0, array, None, None)]
        while stack:
            depth, value, sub_value, index = stack.pop()
            if not is_list(value):

                if value >= 10:

                    # split into two pieces
                    sub_value[index] = [value // 2, (value + 1) // 2]
                    cont = True

                    break

            else:
                # add back to the stack
                for i, sub_value in list(enumerate(value))[::-1]:
                    stack.append((depth + 1, sub_value, value, i))

    return array


def add(a, b):
    return reduce([a, b])


def part_one(data):
    current = data[0]

    for i in data[1:]:
        current = add(current, i)

    return magnitude(current)


def part_two(data):
    max_val = -1

    for a, b in itertools.product(data, repeat = 2):
        val = magnitude(add(a, b,))
        max_val = max([max_val, val])

    return max_val


if __name__ == '__main__':
    data = get_line_data("18")
    data = [json.loads(x) for x in data]

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
