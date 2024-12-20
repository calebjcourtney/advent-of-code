from collections import deque
from itertools import combinations

from utils import DIRS, get_data, manhattan, parse_grid, timeit


def get_distances(grid, start):
    distances = {start: 0}
    queue = deque([start])

    while queue:
        pos = queue.popleft()
        for direction in DIRS:
            new = pos + direction
            if new in grid and new not in distances:
                distances[new] = distances[pos] + 1
                queue.append(new)

    return distances


@timeit
def main(grid):
    start = [p for p in grid if grid[p] == "S"][0]
    distances = get_distances(grid, start)

    p1 = 0
    p2 = 0

    for (p, p_dist), (q, q_dist) in combinations(distances.items(), 2):
        dist = manhattan(p, q)
        p1 += dist == 2 and q_dist - p_dist - dist >= 100
        p2 += dist < 21 and q_dist - p_dist - dist >= 100

    print(p1)
    print(p2)


if __name__ == "__main__":
    grid = parse_grid(
        get_data("20"),
        keep_values=".SE",
    )
    main(grid)
