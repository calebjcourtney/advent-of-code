from utils import get_data
from utils import timeit
from utils import get_nums
from utils import Point
from utils import N, S, E, W

MAP = {
    "R": {
        N: E,
        S: W,
        E: S,
        W: N,
    },
    "L": {
        N: W,
        S: E,
        E: N,
        W: S,
    }
}


@timeit
def main():
    data = get_data("01")
    data = data.split(", ")

    current = Point(0, 0)
    p2 = None
    visited = {current}
    direction = N
    for line in data:
        dist = get_nums(line)[0]
        direction = MAP[line[0]][direction]
        for _ in range(dist):
            current = current + direction
            if p2 is None and current in visited:
                p2 = Point(current.x, current.y)

            visited.add(current)

    assert p2 is not None

    print(abs(current.x) + abs(current.y))
    print(abs(p2.x) + abs(p2.y))
