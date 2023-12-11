from utils import get_line_data
from utils import timeit
from utils import parse_grid
from utils import Point

import itertools


def get_empty_col_rows(data):
    rows = [i for i, row in enumerate(data) if "#" not in row]
    columns = [c for c in range(len(data[0])) if "#" not in [row[c] for row in data]]
    return columns, rows


@timeit
def combined(galaxies: dict[Point, str], columns: list[int], rows: list[int], factor: int):
    total = 0
    for g1, g2 in itertools.combinations(galaxies, 2):
        total += abs(g1.x - g2.x) + abs(g1.y - g2.y)
        for col in columns:
            if g1.x < col < g2.x or g2.x < col < g1.x:
                total += factor - 1

        for row in rows:
            if g1.y < row < g2.y or g2.y < row < g1.y:
                total += factor - 1

    return total


if __name__ == "__main__":
    data = get_line_data("11")
    columns, rows = get_empty_col_rows(data)
    galaxies = parse_grid(data, "#")

    print(combined(galaxies, columns, rows, 2))
    print(combined(galaxies, columns, rows, 1000000))
