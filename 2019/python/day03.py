from utils import get_line_data

data = get_line_data("03")


def get_points(line):
    points = []
    current = (0, 0)
    for instruction in line.split(","):
        if "R" in instruction:
            for x in range(int(instruction[1:])):
                current = current[0] + 1, current[1]
                points.append(current)

        elif "L" in instruction:
            for x in range(int(instruction[1:])):
                current = current[0] - 1, current[1]
                points.append(current)

        elif "U" in instruction:
            for y in range(int(instruction[1:])):
                current = current[0], current[1] + 1
                points.append(current)

        elif "D" in instruction:
            for y in range(int(instruction[1:])):
                current = current[0], current[1] - 1
                points.append(current)

    return points


def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])


def part_1():
    first_points = set(get_points(data[0]))
    second_points = set(get_points(data[1]))

    both_points = (first_points & second_points)

    print(min([manhattan_distance(x) for x in both_points]))


def part_2():
    first_points = get_points(data[0])
    second_points = get_points(data[1])

    both_points = set(first_points) & set(second_points)

    print(min([first_points.index(point) + second_points.index(point) for point in both_points]) + 2)


if __name__ == '__main__':
    part_1()
    part_2()
