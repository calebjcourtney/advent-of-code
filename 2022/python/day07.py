from utils import get_line_data

from collections import defaultdict


def parse_data(data):
    sizes = defaultdict(int)
    path = []
    for line in data:
        tokens = line.strip().split()
        if tokens[1] == 'cd':
            if tokens[2] == '..':
                path.pop()

            else:
                path.append(tokens[2])

        elif tokens[0].isnumeric():
            size = int(tokens[0])
            for i in range(1, len(path) + 1):
                sizes['/'.join(path[:i])] += size

    return sizes


def part_one(data):
    total = 0
    for k, v in data.items():
        if v <= 100000:
            total += v

    return total


def part_two(data):
    total = 1e9
    max_used = 70000000 - 30000000
    total_used = data['/']
    need_to_free = total_used - max_used
    for k, v in data.items():
        if v >= need_to_free:
            total = min(total, v)

    return total


if __name__ == '__main__':
    data = get_line_data("07")
    data = parse_data(data)

    print(part_one(data))
    print(part_two(data))
