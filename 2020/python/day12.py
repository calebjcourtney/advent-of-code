from typing import List


from utils import get_line_data


def part_one(data: List[str]) -> int:
    x, y = 0, 0
    rotation = 0
    for line in data:
        action = line[0]
        units = int(line[1:])

        if action == "F":
            if rotation == 0:
                action = "E"

            elif rotation == 90:
                action = "N"

            elif rotation == 180:
                action = "W"

            elif rotation == 270:
                action = "S"

        if action == "L":
            rotation += units

            if rotation >= 360:
                rotation -= 360

        elif action == "R":
            rotation -= units

            if rotation < 0:
                rotation += 360

        elif action == "N":
            y += units

        elif action == "S":
            y -= units

        elif action == "E":
            x += units

        elif action == "W":
            x -= units

        assert action != "F"

    return abs(x) + abs(y)


def part_two(data: List[str]) -> int:
    x, y = 0, 0
    waypoint_x, waypoint_y = 10, 1

    for line in data:
        action = line[0]
        units = int(line[1:])

        if action == 'F':
            x += waypoint_x * units
            y += waypoint_y * units

        elif action == 'N':
            waypoint_y += units

        elif action == 'E':
            waypoint_x += units

        elif action == 'S':
            waypoint_y -= units

        elif action == 'W':
            waypoint_x -= units

        elif action == 'L':
            while units:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
                units -= 90

        elif action == 'R':
            while units:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
                units -= 90

    return abs(x) + abs(y)


if __name__ == '__main__':
    data = get_line_data("12")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
