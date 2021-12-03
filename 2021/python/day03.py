from utils import get_line_data


def most_common(data, column, flip):
    oxygen = 0
    co2 = 0

    for row in data:
        if row[column] == "1":
            oxygen += 1
        else:
            co2 += 1

    if oxygen == co2:
        return "0" if flip else "1"

    if flip:
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


def part_two(data):
    # oxygen
    tmp = data[:]
    i = 0
    while len(tmp) != 1:
        common_val = most_common(tmp, i, False)
        tmp = [line for line in tmp if line[i] == common_val]
        i += 1

    oxy = tmp[0]

    # co2
    tmp = data[:]
    i = 0
    while len(tmp) != 1:
        common_val = most_common(tmp, i, True)
        tmp = [line for line in tmp if line[i] == common_val]
        i += 1

    co2 = tmp[0]

    return int(oxy, 2) * int(co2, 2)


if __name__ == '__main__':
    data = get_line_data("03")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
