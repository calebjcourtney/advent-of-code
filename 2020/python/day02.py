from utils import get_line_data


def parse_line(record):
    r, letter, password = record.split()
    letter = letter[0]

    start, end = r.split("-")
    start = int(start)
    end = int(end)

    return start, end, letter, password


def part_1(data):
    valid = 0
    for record in data:
        if len(record) < 1:
            continue

        start, end, letter, password = parse_line(record)

        if password.count(letter) >= start and password.count(letter) <= end:
            valid += 1

    return valid


def part_2(data):
    valid = 0
    for record in data:
        if len(record) < 1:
            continue

        start, end, letter, password = parse_line(record)

        if (password[start - 1] == letter) ^ (password[end - 1] == letter):
            valid += 1

    return valid


if __name__ == '__main__':
    data = get_line_data("02")

    print(part_1(data))
    print(part_2(data))
