from utils import get_data


def part_one(data):
    median = sorted(data)[int(len(data) / 2)]
    return sum((abs(num - median) for num in data))


def part_two(data):
    mean = int(sum(data) / len(data))
    return sum(sum(range(abs(num - mean) + 1)) for num in data)


if __name__ == '__main__':
    data = get_data("07")
    data = list(map(int, data.split(",")))

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
