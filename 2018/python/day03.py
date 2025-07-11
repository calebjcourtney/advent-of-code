from utils import get_line_data
from utils import get_nums
from utils import timeit
from utils import Point

from collections import defaultdict


@timeit
def main(data):
    overlapping_grid = {Point(x, y): 0 for x in range(1000) for y in range(1000)}
    unique_grid = defaultdict(set)
    for line in data:
        _id, left, top, width, height = get_nums(line)
        for x in range(left, left + width):
            for y in range(top, top + height):
                overlapping_grid[Point(x, y)] += 1
                unique_grid[_id].add(Point(x, y))

    print(sum(1 for v in overlapping_grid.values() if v > 1))

    for _id, points in unique_grid.items():
        if len({p for p in points if overlapping_grid[p] == 1}) == len(points):
            print(_id)
            return


if __name__ == '__main__':
    data = get_line_data("03")
    p1_result = main(data)
