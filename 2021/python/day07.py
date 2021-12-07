from utils import get_data


def part_one(data):
    min_distance = None
    for x in range(min(data), max(data) + 1):
        cur_dist = 0
        for num in data:
            cur_dist += abs(num - x)

        if min_distance is None or cur_dist < min_distance:
            min_distance = cur_dist

    return min_distance


def part_two(data):
    min_distance = None
    for x in range(min(data), max(data) + 1):
        cur_dist = 0
        for num in data:
            cur_dist += sum(range(abs(num - x) + 1))

        if min_distance is None or cur_dist < min_distance:
            min_distance = cur_dist

    return min_distance


if __name__ == '__main__':
    data = get_data("07")
    data = list(map(int, data.split(",")))

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
