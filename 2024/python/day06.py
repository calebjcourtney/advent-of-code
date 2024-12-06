from copy import deepcopy
from tqdm import tqdm
from collections import defaultdict
from itertools import combinations

from utils import get_data
from utils import parse_grid
from utils import timeit
from utils import N as S, E, S as N, W
from utils import print_grid
from utils import euclidean_distance
from utils import Point

direction_mapping = {
    N: E,
    S: W,
    E: S,
    W: N,
}


def is_loop(grid, current_pos, current_direction):
    seen = set()

    while True:
        next_pos = current_pos + current_direction
        if next_pos not in grid:
            return False

        if grid[next_pos] == "#":
            current_direction = direction_mapping[current_direction]
            next_pos = current_pos + current_direction
        if grid[next_pos] == "#":
            current_direction = direction_mapping[current_direction]
            next_pos = current_pos + current_direction

        current_pos = next_pos
        if (current_pos, current_direction) in seen:
            return True

        seen.add((current_pos, current_direction))


@timeit
def main(grid):
    starting_position = [key for key, value in grid.items() if value == "^"][0]
    current_pos = [key for key, value in grid.items() if value == "^"][0]
    current_direction = N

    grid[current_pos] = "X"
    while True:
        next_pos = current_pos + current_direction
        if next_pos not in grid:
            break

        if grid[next_pos] == "#":
            current_direction = direction_mapping[current_direction]
            next_pos = current_pos + current_direction

        else:
            current_pos = next_pos
            grid[current_pos] = "X"

    possible_obstructions = set(key for key, value in grid.items() if value == "X") - {starting_position}
    print(len(possible_obstructions) + 1)

    part_two = set()
    for ob in tqdm(possible_obstructions):
        temp_grid = deepcopy(grid)
        temp_grid[ob] = "#"
        if is_loop(temp_grid, starting_position, N):
                part_two.add(ob)

    print(len(part_two))


if __name__ == '__main__':
    data = get_data("06")
    grid = parse_grid(data)

    main(grid)
