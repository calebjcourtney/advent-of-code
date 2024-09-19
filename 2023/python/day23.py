from collections import deque, defaultdict

from utils import Point, N, S, E, W, DIRS
from utils import get_data
from utils import parse_grid
from utils import min_max_xy
from utils import timeit


SLOPES = {
    "^": S,
    "v": N,
    "<": W,
    ">": E,
}


def get_neighbours(graph, node, part_2=False):
    """In part 2, we ignore slopes."""
    if graph.get(node) == "#":
        return

    if not part_2:
        if graph.get(node) in SLOPES:
            yield node + SLOPES[graph.get(node)]
            return

    for d in DIRS:
        np = node + d
        if np not in graph:
            continue

        neighbour = graph.get(np)

        if neighbour == "#":
            continue

        if not part_2 and neighbour in SLOPES and d != SLOPES[neighbour]:
            continue

        yield np


@timeit
def combined(graph, start, end, part_2=False):
    horizon = [(start, 0, set())]
    best = 0

    while horizon:
        curr, dist, seen = horizon.pop()

        if curr == end:
            best = max(best, dist)
            continue

        if curr in seen:
            continue

        new_seen = seen | {curr}

        for neighbour, weight in graph[curr]:
            horizon.append((neighbour, dist + weight, new_seen))

    return best


def compress_graph(graph, part_2=False):
    degrees = defaultdict(set)
    for node in graph:
        degrees[len(list(get_neighbours(graph, node, part_2)))].add(node)

    key_points = degrees[1] | degrees[3] | degrees[4]

    # Find the distance from node to all other "key points" it can reach.
    def search(start):
        horizon = deque([(start, 0)])
        seen = set()

        while horizon:
            curr, dist = horizon.pop()

            if curr != start and curr in key_points:
                yield curr, dist
                continue

            if curr in seen:
                continue

            seen.add(curr)

            for neighbour in get_neighbours(graph, curr, part_2):
                horizon.appendleft((neighbour, dist + 1))

    compressed = defaultdict(list)

    for node in key_points:
        for neighbour, weight in search(node):
            compressed[node].append((neighbour, weight))

    return compressed


if __name__ == '__main__':
    # Parse problem input.
    data = get_data("23")
    GRID = parse_grid(data)
    min_x, max_x, min_y, max_y = min_max_xy(GRID)
    START = Point(min_x + 1, min_y)
    END = Point(max_x - 1, max_y)

    print(combined(compress_graph(GRID), START, END))
    print(combined(compress_graph(GRID, part_2=True), START, END, part_2=True))
