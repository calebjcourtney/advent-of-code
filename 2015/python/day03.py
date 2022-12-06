from utils import get_data


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


def part_one(data):
    current_location = Point()
    visited_locations = set()
    visited_locations.add((0, 0))
    for instruction in data:
        if instruction == ">":
            current_location.x += 1
        elif instruction == "<":
            current_location.x -= 1
        elif instruction == "^":
            current_location.y += 1
        elif instruction == "v":
            current_location.y -= 1

        visited_locations.add((current_location.x, current_location.y))

    return len(visited_locations)


def part_two(data):
    santa = Point()
    robo_santa = Point()
    visited_locations = set()
    visited_locations.add((0, 0))
    for i, instruction in enumerate(data):
        if i % 2 == 0:
            if instruction == ">":
                santa.x += 1
            elif instruction == "<":
                santa.x -= 1
            elif instruction == "^":
                santa.y += 1
            elif instruction == "v":
                santa.y -= 1

            visited_locations.add((santa.x, santa.y))

        elif i % 2 == 1:
            if instruction == ">":
                robo_santa.x += 1
            elif instruction == "<":
                robo_santa.x -= 1
            elif instruction == "^":
                robo_santa.y += 1
            elif instruction == "v":
                robo_santa.y -= 1

            visited_locations.add((robo_santa.x, robo_santa.y))

    return len(visited_locations)


if __name__ == '__main__':
    data = get_data("03")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
