from utils import get_line_data


def part_one(seat_ids):
    return max(seat_ids)


def part_two(seat_ids):
    for x in range(min(seat_ids), max(seat_ids)):
        if x not in seat_ids:
            return x


if __name__ == '__main__':
    data = get_line_data("05")

    t = str.maketrans({'B': '1', 'R': '1', 'F': '0', 'L': '0'})
    seat_ids = [int(line.translate(t), 2) for line in data]

    print(part_one(seat_ids))
    print(part_two(seat_ids))
