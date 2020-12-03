from utils import get_line_data


data = get_line_data("03")


def part_one(data):
    trees = 0
    for x in range(len(data)):
        if data[x][(x * 3) % len(data[0])] == "#":
            trees += 1

    return trees


def part_two(data):
    trees = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        temp = 0
        for x in range(len(data)):
            try:
                if data[x * down][(x * right) % len(data[0])] == "#":
                    temp += 1
            except IndexError:
                break

        trees *= temp

    return trees


if __name__ == '__main__':
    data = get_line_data("03")
    print(part_one(data))
    print(part_two(data))
