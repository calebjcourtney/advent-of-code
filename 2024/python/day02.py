from utils import get_line_data
from utils import get_nums


def is_safe(record) -> bool:
    return all([
        # is ascending or descending
        any([
            sorted(record) == record,
            sorted(record, reverse=True) == record,
        ]),
        all([
            1 <= abs(b - a) <= 3
            for a, b in zip(record, record[1:])
        ]),
    ])


def part_two(record) -> bool:
    return any([
        is_safe(record[:i] + record[i + 1:])
        for i in range(len(record))
    ])


if __name__ == '__main__':
    data = get_line_data("02")
    data = [list(map(int, get_nums(line))) for line in data]

    print("part 1:", sum(is_safe(record) for record in data))
    print("part 2:", sum(part_two(record) for record in data))
