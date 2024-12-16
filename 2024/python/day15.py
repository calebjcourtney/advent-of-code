from utils import get_data
from utils import parse_grid
from utils import timeit
from utils import N, S, E, W
from utils import print_grid
from utils import Point

import time
from collections import deque


MOVEMENT_MAP = {
    "<": W,
    ">": E,
    "v": N,
    "^": S,
}


def boxes_to_move(grid, current, direction):
    output = set()
    tmp = current + direction
    queue = deque([tmp])
    while queue:
        tmp = queue.popleft()
        if tmp in output:
            continue

        if grid[tmp] == "O":
            output.add(tmp)
            queue.append(tmp + direction)

        elif grid[tmp] == "[":
            output.add(tmp)
            output.add(tmp + E)
            queue.append(tmp + direction)
            queue.append(tmp + E + direction)

        elif grid[tmp] == "]":
            output.add(tmp)
            output.add(tmp + W)
            queue.append(tmp + direction)
            queue.append(tmp + W + direction)

        elif grid[tmp] == ".":
            continue

        elif grid[tmp] == "#":
            return []

    return output


@timeit
def solve(grid: dict, movements):
    current = [k for k, v in grid.items() if v == "@"][0]

    for move in movements:
        direction = MOVEMENT_MAP[move]
        next_pos = grid[current + direction]
        if next_pos in "0[]":
            boxes_in_way = boxes_to_move(grid, current, direction)

            # can't move
            if not boxes_in_way:
                continue
            else:
                current_values = {point: grid[point] for point in boxes_in_way}
                for point in boxes_in_way:
                    grid[point] = "."

                for point in boxes_in_way:
                    grid[point + direction] = current_values[point]

                grid[current + direction] = "@"
                grid[current] = "."
                current += direction

        elif next_pos == ".":
            grid[current + direction] = "@"
            grid[current] = "."
            current += direction
        elif next_pos == "#":
            continue

    return grid


@timeit
def main(text_grid, movements):
    p1_grid = parse_grid(text_grid)
    p1_grid = solve(p1_grid, movements)
    print(sum(key.x + key.y * 100 for key, value in p1_grid.items() if value == "O"))

    text_grid = text_grid.replace("#", "##")
    text_grid = text_grid.replace("O", "[]")
    text_grid = text_grid.replace(".", "..")
    text_grid = text_grid.replace("@", "@.")

    p2_grid = parse_grid(text_grid)
    p2_grid = solve(p2_grid, movements)

    print(sum(key.x + key.y * 100 for key, value in p2_grid.items() if value == "["))



if __name__ == '__main__':
    data = get_data("15")
    text_grid, movements = data.split("\n\n")
    movements = "".join(movements.split("\n"))
    main(text_grid, movements)
