from utils import get_line_data
from utils import get_nums
from utils import timeit

from math import prod
from collections import Counter


MAX_X = 101
MAX_Y = 103


def parse_data(data) -> tuple:
    robots = []
    for line in data:
        px, py, vx, vy = get_nums(line)
        robots.append((px, py, vx, vy))

    return robots


@timeit
def main(robots):
    for iteration in range(1, 100000):
        new_robots = []
        for px, py, vx, vy in robots:
            nx = (px + vx) % MAX_X
            ny = (py + vy) % MAX_Y
            new_robots.append((nx, ny, vx, vy))

        robots = new_robots

        picture = set((px, py) for px, py, _, _ in robots)

        contig = 0
        max_contig = 0

        for y in range(MAX_Y):
            for x in range(MAX_X):
                if (x, y) in picture:
                    contig += 1
                    max_contig = max(contig, max_contig)
                else:
                    contig = 0

        # if we find a line of robots, it's probably the tree.
        if max_contig > 15:
            print(iteration)
            return

        if iteration == 100:
            quadrants = Counter()
            for px, py, _, _ in robots:
                if px < MAX_X // 2 and py < MAX_Y // 2:
                    quadrants[1] += 1
                elif px < MAX_X // 2 and py > MAX_Y // 2:
                    quadrants[2] += 1
                elif px > MAX_X // 2 and py < MAX_Y // 2:
                    quadrants[3] += 1
                elif px > MAX_X // 2 and py > MAX_Y // 2:
                    quadrants[4] += 1

            print(prod(quadrants.values()))


if __name__ == '__main__':
    data = get_line_data("14")
    data = parse_data(data)
    main(data)
