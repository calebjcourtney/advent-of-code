from utils import get_line_data

import collections


def run_mask(value, mask):
    value |= int(mask.replace('X', '0'), 2)
    value &= int(mask.replace('X', '1'), 2)
    return value


def part_one(data):
    mask = None
    mem = collections.defaultdict(int)
    for line in data:
        op, arg = line.split(' = ')

        if op == 'mask':
            mask = arg

        else:
            pos = int(op[4:-1])
            mem[pos] = run_mask(int(arg), mask)

    return sum(mem.values())


def allmasks(pos, mask):
    if not mask:
        yield 0

    else:
        # yay recursion again
        for m in allmasks(pos // 2, mask[:-1]):
            if mask[-1] == '0':
                yield 2 * m + pos % 2
            if mask[-1] == '1':
                yield 2 * m + 1
            if mask[-1] == 'X':
                yield 2 * m + 0
                yield 2 * m + 1


def part_two(data):
    mask = None
    mem = collections.defaultdict(int)
    for line in data:
        op, arg = line.split(' = ')

        if op == 'mask':
            mask = arg

        else:
            pos = int(op[4:-1])

            # the only difference for part 2
            for m in allmasks(pos, mask):
                mem[m] = int(arg)

    return sum(mem.values())


if __name__ == '__main__':
    data = get_line_data("14")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
