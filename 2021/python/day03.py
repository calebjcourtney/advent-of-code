from utils import get_line_data

from collections import Counter


def most_common(data, index, invert):
    c = Counter(row[index] for row in data)

    oxygen = c["1"]
    co2 = c["0"]

    if oxygen == co2:
        return "0" if invert else "1"

    if invert:
        oxygen, co2 = co2, oxygen

    return "1" if oxygen >= co2 else "0"


def part_one(data):
    epsilon = ""
    gamma = ""
    for i in range(len(data[0])):
        common_val = most_common(data, i, False)
        uncommon_val = "1" if common_val == "0" else "0"

        gamma += common_val
        epsilon += uncommon_val

    return int(gamma, 2) * int(epsilon, 2)


def filter_data(data, invert):
    i = 0
    while len(data) != 1:
        common_val = most_common(data, i, invert)
        data = [line for line in data if line[i] == common_val]
        i += 1

    val = data[0]

    return val


def part_two(data):
    oxygen = filter_data(data, False)
    co2 = filter_data(data, True)

    return int(oxygen, 2) * int(co2, 2)


if __name__ == '__main__':
    data = get_line_data("03")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
