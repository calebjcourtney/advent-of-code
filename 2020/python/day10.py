from utils import get_int_data


def part_one(line_data):
    ones = 1
    threes = 1
    for x in range(1, len(line_data)):
        if line_data[x] - line_data[x - 1] == 1:
            ones += 1

        elif line_data[x] - line_data[x - 1] == 3:
            threes += 1

        else:
            raise ValueError("You did something wrong")

    return ones * threes


memorize_ways = {}


def part_two(line_data, start, goal):
    point = (len(line_data), start)

    if point in memorize_ways:
        return memorize_ways[point]

    ways = 0

    if goal - start <= 3:
        ways += 1

    if not line_data:
        return ways

    # yay! recursion
    if line_data[0] - start <= 3:
        ways += part_two(line_data[1:], line_data[0], goal)

    # wut. more recursion? wy tho
    ways += part_two(line_data[1:], start, goal)

    memorize_ways[point] = ways

    return ways


if __name__ == '__main__':
    data = get_int_data("10")
    data.sort()

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data, 0, max(data) + 3)
    print(p2_result)
