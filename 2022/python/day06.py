from utils import get_data


def part_one(data):
    count = 0
    for c in data:
        count += 1
        if count >= 4:
            if len(set(data[count - 4:count])) == 4:
                return count


def part_two(data):
    count = 0
    for c in data:
        count += 1

        if count >= 14:
            if len(set(data[count - 14:count])) == 14:
                return count


if __name__ == '__main__':
    data = get_data("06")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
