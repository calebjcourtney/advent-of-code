from itertools import combinations

from utils import get_data, get_distances, manhattan, parse_grid, timeit


@timeit
def main(data):
    grid = parse_grid(
        data,
        keep_values=".SE",
    )
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
    data = get_data("20")
    main(data)
