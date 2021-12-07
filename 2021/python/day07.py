from utils import get_data


def part_one(data):
    median = sorted(data)[len(data) // 2]
    return min(sum((abs(num - x) for num in data)) for x in range(median - 1, median + 2))


def part_two(data):
    mean = sum(data) // len(data)
    return min(sum(sum(range(abs(num - x) + 1)) for num in data) for x in range(mean - 1, mean + 2))


if __name__ == '__main__':
    data = get_data("07")
    data = list(map(int, data.split(",")))

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
