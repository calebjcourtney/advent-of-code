from utils import get_int_data


def part_one(cap):
    data = [0] * (cap // 10)
    for x in range(1, len(data)):
        for index in range(x, len(data), x):
            data[index] += x * 10

        if data[x] >= cap:
            return x

    assert False


def part_two(cap):
    data = [0] * (cap // 10)
    for x in range(1, len(data)):
        for index in range(x, min(x * 50 + 1, len(data)), x):
            data[index] += x * 11

        if data[x] >= cap:
            return x

    assert False


if __name__ == '__main__':
    data = get_int_data("20")[0]

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
