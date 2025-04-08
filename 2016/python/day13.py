from utils import get_data
from utils import timeit
from utils import Point
from utils import get_distances


@timeit
def main(seed):
    grid = {}
    for x in range(50):
        for y in range(50):
            val = '{0:b}'.format(x*x + 3*x + 2*x*y + y + y*y + seed).count("1")
            if val % 2 == 0:
                grid[Point(x, y)] = "."

    distances = get_distances(grid, Point(1, 1))

    return distances[Point(31, 39)], len([x for x in distances.values() if x <= 50])


if __name__ == '__main__':
    data = get_data("13")
    seed = int(data)

    p1, p2 = main(seed)
    print(p1)
    print(p2)
