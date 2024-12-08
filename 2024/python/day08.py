from utils import get_data
from utils import parse_grid
from utils import timeit
from utils import Point
from utils import euclidean_distance

from itertools import combinations


def create_function_from_two_points(p1, p2) -> callable:
    slope = (p2.y - p1.y) / (p2.x - p1.x)
    y_intercept = p1.y - slope * p1.x

    def line_function(x):
        return round(slope * x + y_intercept, 6)

    return line_function


def get_antinodes(p1, p2, max_x) -> set[Point]:
    func = create_function_from_two_points(p1, p2)
    output = set()
    for x in range(max_x + 1):
        p = Point(x, func(x))
        output.add(p)

    return output

@timeit
def main(grid) -> None:
    unique_symbols = set(val for val in grid.values() if val != ".")
    max_x = max(key.x for key in grid)

    part_one = set()
    part_two = set()

    for symbol in unique_symbols:
        locations = {key for key, value in grid.items() if value == symbol}
        for p1, p2 in combinations(locations, 2):
            dist = euclidean_distance(p1, p2)
            antinodes = get_antinodes(p1, p2, max_x)
            part_two |= (antinodes & set(grid.keys()))

            for node in antinodes:
                d1 = euclidean_distance(p1, node)
                d2 = euclidean_distance(p2, node)
                if node in grid and {d1, d2} == {dist, dist * 2}:
                    part_one.add(node)

    print(len(part_one))
    print(len(part_two))


if __name__ == '__main__':
    data = get_data("08")
    grid = parse_grid(data)

    main(grid)
