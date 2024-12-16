from utils import get_data
from utils import parse_grid
from utils import timeit
from utils import N, E, S, W
from utils import Point

import itertools
from collections import deque
from typing import NamedTuple
import time


class Path(NamedTuple):
    current: Point
    direction: Point
    score: int
    points: set[Point] = set()

    def __eq__(self, other):
        return all([
            self.current == other.current,
            self.direction == other.direction,
        ])

    def __hash__(self):
        return hash((self.current, self.direction))


@timeit
def main(grid):
    start_pos = [p for p, v in grid.items() if v == "S"][0]
    end_pos = [p for p, v in grid.items() if v == "E"][0]

    path = Path(start_pos, E, 0, {start_pos})
    score_to_point = {path: 0}

    queue = deque([path])
    complete_paths = []
    while queue:
        path = queue.popleft()

        if path not in score_to_point:
            score_to_point[path] = path.score
        elif path.score <= score_to_point[path]:
            score_to_point[path] = path.score
        else:
            continue

        if path.current == end_pos:
            complete_paths.append(path)
            continue

        for new_dir in [N, E, S, W]:
            new_pos = path.current + new_dir

            if grid[new_pos] == "#" or new_pos in path.points:
                continue

            new_score = path.score + 1
            if new_dir != path.direction:
                new_score += 1000

            queue.append(
                Path(
                    new_pos,
                    new_dir,
                    new_score,
                    path.points | {new_pos}
                )
            )

    best_score = min(v for k, v in score_to_point.items() if k.current == end_pos)
    print(best_score)

    path_points = set()
    for path in complete_paths:
        if path.score == best_score:
            path_points |= path.points

    print(len(path_points))


if __name__ == '__main__':
    data = get_data("16")
    grid = parse_grid(data)
    main(grid)
