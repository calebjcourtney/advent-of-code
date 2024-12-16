from utils import get_data
from utils import parse_grid
from utils import Point
from utils import DIRS
from utils import N, S, E, W
from utils import timeit

from collections import defaultdict
from collections import deque


def process_plot(garden, start, visited):
    plot = set()
    horizon = deque([start])
    plant = garden.get(start)

    while horizon:
        node = horizon.popleft()
        if node in plot:
            continue

        plot.add(node)
        visited.add(node)

        for n in node.neighbors:
            if n in garden and garden.get(n) == plant:
                horizon.append(n)

    area = len(plot)

    perimeter = sum(len(set(p.neighbors) - plot) for p in plot)

    row_sides = {
        N: defaultdict(set),
        S: defaultdict(set),
    }
    for y in range(-2, 150):
        for d in [N, S]:
            for x in range(-2, 150):
                p = Point(x, y)
                if p in plot and p + d not in plot:
                    row_sides[d][y].add(p)

    col_sides = {
        E: defaultdict(set),
        W: defaultdict(set)
    }

    for x in range(-2, 150):
        for d in [E, W]:
            for y in range(-2, 150):
                p = Point(x, y)
                if p in plot and p + d not in plot:
                    col_sides[d][x].add(p)

    # horizonal/vertical sweep
    sides = 0

    for d in [N, S]:
        for y in range(-2, 150):
            x = -2
            inside = False
            while x < 150:
                p = Point(x, y)
                if p in row_sides[d][y]:
                    if not inside:
                        sides += 1
                        inside = True
                else:
                    if inside:
                        inside = False

                x += 1

    for d in [E, W]:
        for x in range(-2, 150):
            y = -2
            inside = False
            while y < 150:
                p = Point(x, y)
                if p in col_sides[d][x]:
                    if not inside:
                        sides += 1
                        inside = True
                else:
                    if inside:
                        inside = False

                y += 1

    return area, perimeter, sides


@timeit
def main(grid):
    p1 = 0
    p2 = 0
    visited = set()

    for pos in grid:
        if pos not in visited:
            area, perim, sides = process_plot(grid, pos, visited)
            p1 += area * perim
            p2 += area * sides

    print(p1)
    print(p2)


if __name__ == '__main__':
    data = get_data("12")
    grid = parse_grid(data)
    main(grid)
