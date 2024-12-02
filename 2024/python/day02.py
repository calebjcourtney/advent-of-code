from utils import get_line_data
from utils import get_nums


def is_order_correct(record: list[int]) -> bool:
    return any([
        sorted(record) == record,
        sorted(record, reverse=True) == record,
    ])


def numbers_gap(record: list[int]):
    for a, b in zip(record, record[1:]):
        if not (1 <= abs(b - a) <= 3):
            return False

    return True

def part_one(record):
    return all([
        is_order_correct(record),
        numbers_gap(record),
    ])


def part_two(record):
    if part_one(record):
        return True

    for i in range(len(record)):
        if part_one(record[:i] + record[i+1:]):
            return True

    return False


if __name__ == '__main__':
    data = get_line_data("02")
    data = [list(map(int, get_nums(line))) for line in data]

    print(sum(part_one(record) for record in data))
    print(sum(part_two(record) for record in data))
