from utils import get_data
from utils import parse_grid
from utils import timeit
from utils import N, E, W

from collections import deque
from functools import cache


@timeit
def part_one(start, grid):
    tachyon_splits = set()
    visited = set()

    current_points = deque([start])
    while current_points:
        current_point = current_points.popleft()

        if current_point in visited:
            continue

        if current_point not in grid:
            continue

        visited.add(current_point)
        cell = grid[current_point]

        if cell == "^":
            tachyon_splits.add(current_point)
            left = current_point + W
            right = current_point + E
            if left in grid:
                current_points.append(left)
            if right in grid:
                current_points.append(right)
        elif cell in ".S":
            down = current_point + N
            if down in grid:
                current_points.append(down)

    return len(tachyon_splits)


@timeit
def part_two(start, grid):
    max_y = max(p.y for p in grid.keys()) if grid else 0
    
    @cache
    def count_timelines(point):
        if point.y >= max_y:
            return 1
        
        down = point + N
        
        if down not in grid:
            return 1
        
        cell_below = grid[down]
        
        if cell_below == "^":
            left = down + W
            right = down + E
            result = 0
            if left in grid:
                result += count_timelines(left)
            else:
                result += 1
            if right in grid:
                result += count_timelines(right)
            else:
                result += 1
            return result
        else:
            return count_timelines(down)
    
    return count_timelines(start)


@timeit
def main():
    data = get_data("07")
    grid = parse_grid(data)
    start = [key for key, value in grid.items() if value == "S"][0]

    p1_result = part_one(start, grid)
    print(p1_result)

    p2_result = part_two(start, grid)
    print(p2_result)
