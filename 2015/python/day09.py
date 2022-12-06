import re
import itertools
from collections import defaultdict


from utils import get_line_data


def parse_line(line):
    p1, p2, dist = re.search(r'(.*) to (.*) = (\d+)', line).groups()
    dist = int(dist)

    return p1, p2, dist


def get_order_distance(cities, distances):
    total = 0
    for c1, c2 in zip(cities, cities[1:]):
        total += distances[c1][c2]

    return total


def part_one(data):
    distances = defaultdict(lambda: defaultdict(int))
    min_distance = 0
    for line in data:
        p1, p2, dist = parse_line(line)
        distances[p1][p2] = dist
        distances[p2][p1] = dist
        min_distance += dist

    for cities in itertools.permutations(list(distances.keys()), len(distances)):
        temp = get_order_distance(cities, distances)
        if temp < min_distance:
            min_distance = temp

    return min_distance


def part_two(data):
    distances = defaultdict(lambda: defaultdict(int))
    max_distance = 0
    for line in data:
        p1, p2, dist = parse_line(line)
        distances[p1][p2] = dist
        distances[p2][p1] = dist

    for cities in itertools.permutations(list(distances.keys()), len(distances)):
        temp = get_order_distance(cities, distances)
        if temp > max_distance:
            max_distance = temp

    return max_distance


if __name__ == '__main__':
    data = get_line_data("09")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
