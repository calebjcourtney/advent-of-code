import heapq
from typing import Generator

from utils import get_data
from utils import parse_grid
from utils import N, S, E, W
from utils import min_max_xy
from utils import Point
from utils import timeit


@timeit
def find_shortest_path(grid, part_2=False):
    min_x, max_x, min_y, max_y = min_max_xy(grid)
    start = Point(min_x, min_y)
    goal = Point(max_x, max_y)

    def gen_neighbours(node: Point, last_dir: Point, last_count: int) -> Generator:
        for direction in [N, S, E, W]:
            neighbor = node + direction
            if neighbor not in grid:
                continue

            if last_dir is not None:
                if last_dir == -direction:
                    continue

                if part_2:
                    if last_count < 4 and direction != last_dir:
                        continue
                    if last_count == 10 and direction == last_dir:
                        continue
                else:
                    if last_count == 3 and direction == last_dir:
                        continue

            yield neighbor, grid[neighbor], direction

    queue = [(0, start, None, 0)]
    seen = set()

    while queue:
        depth, curr, last_dir, last_count = heapq.heappop(queue)

        key = curr, last_dir, last_count

        if key in seen:
            continue

        seen.add(key)

        if curr == goal and (not part_2 or last_count >= 4):
            return depth

        for neighbor, cost, new_direction in gen_neighbours(curr, last_dir, last_count):
            new_cost = cost + depth
            new_count = 1 if new_direction != last_dir else last_count + 1
            heapq.heappush(queue, (new_cost, neighbor, new_direction, new_count))


if __name__ == '__main__':
    data = get_data("17")
    grid = parse_grid(data)
    grid = {key: int(value) for key, value in grid.items()}

    print(find_shortest_path(grid))
    print(find_shortest_path(grid, True))
