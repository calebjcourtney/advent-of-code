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


# props to AltNyx for this elegant solution
def part_two(line_data):
    points = [1] + [0] * (line_data[-1])

    for r in line_data:
        points[r] = points[r - 1] + points[r - 2] + points[r - 3]

    return points[-1]


if __name__ == '__main__':
    data = get_int_data("10")
    data.sort()

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
