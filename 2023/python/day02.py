import re

from utils import get_line_data


def combined(data):
    red_count = re.compile(r"(\d+) red")
    blue_count = re.compile(r"(\d+) blue")
    green_count = re.compile(r"(\d+) green")
    game_id = re.compile(r"Game (\d+):")

    part_one = 0
    part_two = 0

    for line in data:
        id = int(game_id.search(line).group(1))

        red = max(map(int, red_count.findall(line)))
        green = max(map(int, green_count.findall(line)))
        blue = max(map(int, blue_count.findall(line)))
        if all([red <= 12, green <= 13, blue <= 14]):
            part_one += id

        part_two += red * green * blue

    return part_one, part_two


if __name__ == '__main__':
    data = get_line_data("02")
    p1, p2 = combined(data)
    print(p1)
    print(p2)
