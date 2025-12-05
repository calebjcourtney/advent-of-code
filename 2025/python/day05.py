from utils import get_data
from utils import timeit


def parse_data(data):
    sections = data.split("\n\n")
    range_lines = sections[0].split("\n")
    ingredient_ranges = [
        range(int(range_line.split("-")[0]), int(range_line.split("-")[1]) + 1)
        for range_line in range_lines
    ]
    available_ingredient_ids = list(map(int, sections[1].split()))

    return ingredient_ranges, available_ingredient_ids


def merge_ranges(ingredient_ranges):
    ingredient_ranges = sorted(ingredient_ranges, key=lambda r: r.start)

    idx = 0
    while idx < len(ingredient_ranges) - 1:
        current_range = ingredient_ranges[idx]
        next_range = ingredient_ranges[idx + 1]

        if current_range.stop - 1 >= next_range.start:
            ingredient_ranges[idx] = range(
                current_range.start,
                max(current_range.stop, next_range.stop)
            )
            ingredient_ranges.pop(idx + 1)
        else:
            idx += 1

    return ingredient_ranges


@timeit
def part_one(ingredient_ranges, available_ingredient_ids):
    return sum(
        1 for ingredient_id in available_ingredient_ids
        if any(ingredient_id in r for r in ingredient_ranges)
    )


@timeit
def part_two(ingredient_ranges):
    return sum(len(r) for r in ingredient_ranges)


@timeit
def main():
    data = get_data("05")
    ingredient_ranges, available_ingredient_ids = parse_data(data)
    ingredient_ranges = merge_ranges(ingredient_ranges)

    result_part_one = part_one(ingredient_ranges, available_ingredient_ids)
    print(result_part_one)

    result_part_two = part_two(ingredient_ranges)
    print(result_part_two)
