from collections import deque
from collections import defaultdict

from utils import get_data
from utils import parse_grid
from utils import timeit
from utils import DIRS
from utils import Point


def get_score(grid: dict[Point, int], current_pos: Point) -> dict[Point, int]:
    paths = defaultdict(int)
    positions = deque([current_pos])
    while positions:
        position = positions.popleft()
        for direction in DIRS:
            new_position = position + direction
            if new_position in grid:
                if grid[new_position] == grid[position] + 1 and grid[new_position] == 9:
                    paths[new_position] += 1
                elif grid[new_position] == grid[position] + 1:
                    positions.append(new_position)

    return paths


@timeit
def main(grid: dict[Point, int]) -> None:
    trail_heads = [point for point, value in grid.items() if value == 0]
    p1 = 0
    p2 = 0

    for th in trail_heads:
        paths = get_score(grid, th)
        p1 += len(paths)
        p2 += sum(paths.values())

    print(p1)
    print(p2)


if __name__ == '__main__':
    data = get_data("10")
    grid = parse_grid(data)
    grid = {key: int(value) for key, value in grid.items()}

    main(grid)
