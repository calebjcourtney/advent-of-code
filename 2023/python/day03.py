from typing import NamedTuple
from math import prod


from utils import get_line_data, parse_grid
from utils import DIRS_8, min_max_xy
from utils import timeit


class ResultNum(NamedTuple):
    num: int
    line: str
    span: tuple


def get_part_number(line, index) -> ResultNum:
    # given the full line and the index of at least one number in the line, get the entire number from the line
    if not line[index].isdigit():
        raise ValueError(f"index must be a digit, found, {line[index]}")
    num = ""
    high = index
    while high < len(line):
        if line[high].isdigit():
            num += line[high]
            high += 1
        else:
            break

    low = index - 1
    while low >= 0:
        if line[low].isdigit():
            num = line[low] + num
            low -= 1
        else:
            break

    return ResultNum(int(num), line, (low + 1, high - 1))


@timeit
def combined(data):
    part_one = set()
    part_two = 0

    grid = parse_grid(data)
    min_x, max_x, min_y, max_y = min_max_xy(list(grid.keys()))

    for point, value in grid.items():
        if value == "." or value.isdigit():
            continue

        gear_parts = set()

        for direction in DIRS_8:
            if point.x + direction.x < min_x or max_x < point.x + direction.x:
                continue
            if point.y + direction.y < min_y or max_y < point.y + direction.y:
                continue

            if grid[point + direction].isdigit():
                full_num = get_part_number(data[point.y + direction.y], point.x + direction.x)
                part_one.add(full_num)

                if value == "*":
                    gear_parts.add(full_num)

        if len(gear_parts) > 1:
            part_two += prod(r.num for r in gear_parts)

    return sum(result.num for result in part_one), part_two


if __name__ == '__main__':
    data = get_line_data("03")
    p1_result, p2_result = combined(data)
    print(p1_result)
    print(p2_result)
