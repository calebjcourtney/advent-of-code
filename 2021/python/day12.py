from utils import get_line_data

from collections import defaultdict


def part_one(path_map):
    start_path = ('start', set(['start']))
    answer = 0
    paths = [start_path]
    while len(paths) > 0:
        current, visited = paths.pop()
        if current == 'end':
            answer += 1
            continue

        for target in path_map[current]:
            if target not in visited:
                new_visited = set(visited)
                if target.lower() == target:
                    new_visited.add(target)

                paths.append((target, new_visited))

    return answer


def part_two(path_map):
    start_path = ('start', set(['start']), None)
    answer = 0
    paths = [start_path]
    while len(paths) > 0:
        current, visited, twice = paths.pop(0)
        if current == 'end':
            answer += 1
            continue

        for target in path_map[current]:
            if target not in visited:
                new_visited = set(visited)
                if target.lower() == target:
                    new_visited.add(target)

                paths.append((target, new_visited, twice))

            elif target in visited and twice is None and target not in ['start', 'end']:
                paths.append((target, visited, target))

    return answer


if __name__ == '__main__':
    data = get_line_data("12")
    paths = defaultdict(list)
    for line in data:
        f, t = line.split("-")
        paths[f].append(t)
        paths[t].append(f)

    p1_result = part_one(paths)
    print(p1_result)

    p2_result = part_two(paths)
    print(p2_result)
