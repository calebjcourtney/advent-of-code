from collections import deque
import hashlib

from utils import get_data
from utils import timeit
from utils import Point

def md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()


def get_open_doors(passcode, path):
    hash_str = md5_hash(passcode + path)
    doors = hash_str[:4]

    open_doors = set()
    directions = ['U', 'D', 'L', 'R']

    for i, door in enumerate(doors):
        if door in 'bcdef':
            open_doors.add(directions[i])

    return open_doors


def get_valid_moves(pos, open_doors):
    x, y = pos
    valid_moves = []

    for door in open_doors:
        if door == 'U' and y > 0:
            valid_moves.append(('U', Point(x, y-1)))
        elif door == 'D' and y < 3:
            valid_moves.append(('D', Point(x, y+1)))
        elif door == 'L' and x > 0:
            valid_moves.append(('L', Point(x-1, y)))
        elif door == 'R' and x < 3:
            valid_moves.append(('R', Point(x+1, y)))

    return valid_moves


@timeit
def part_one(data):
    passcode = data.strip()
    start = (0, 0)
    target = (3, 3)

    queue = deque([(start, "")])
    visited = set()

    while queue:
        pos, path = queue.popleft()

        if pos == target:
            return path

        state = (pos, path)
        if state in visited:
            continue
        visited.add(state)

        open_doors = get_open_doors(passcode, path)

        for direction, new_pos in get_valid_moves(pos, open_doors):
            new_path = path + direction
            queue.append((new_pos, new_path))

    return "No path found"


@timeit
def part_two(data):
    passcode = data.strip()
    start = (0, 0)
    target = (3, 3)

    def find_all_paths(pos, path):
        if pos == target:
            return [path]

        if len(path) > 1000:
            return []

        open_doors = get_open_doors(passcode, path)
        all_paths = []

        for direction, new_pos in get_valid_moves(pos, open_doors):
            sub_paths = find_all_paths(new_pos, path + direction)
            all_paths.extend(sub_paths)

        return all_paths

    all_paths = find_all_paths(start, "")

    if not all_paths:
        return 0

    return len(max(all_paths, key=len))


@timeit
def main():
    data = get_data("17")

    p1_result = part_one(data)
    print(f"Part 1: {p1_result}")

    p2_result = part_two(data)
    print(f"Part 2: {p2_result}")
