from utils import get_line_data


from typing import Tuple


def parse_line(record: str) -> Tuple[int, int, str, str]:
    r, letter, password = record.split()
    letter = letter[0]

    start, end = r.split("-")
    start = int(start)
    end = int(end)

    return start, end, letter, password


def part_1(record: str) -> int:
    if len(record) < 1:
        return 0

    start, end, letter, password = parse_line(record)

    if password.count(letter) >= start and password.count(letter) <= end:
        return 1

    return 0


def part_2(record: str) -> int:
    if len(record) < 1:
        return 0

    start, end, letter, password = parse_line(record)

    if (password[start - 1] == letter) ^ (password[end - 1] == letter):
        return 1

    return 0


if __name__ == '__main__':
    data = get_line_data("02")

    print(sum(map(part_1, data)))
    print(sum(map(part_2, data)))
