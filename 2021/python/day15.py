from utils import get_line_data

import numpy as np
import networkx as nx


DIFFS = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
]


def solve(data):
    graph = nx.DiGraph()

    for y, row in enumerate(data):
        for x, col in enumerate(row):
            for dy, dx in DIFFS:
                if 0 <= dy + y < len(data) and 0 <= dx + x < len(data[0]):
                    graph.add_edge(
                        f"{x}_{y}_{data[y][x]}",
                        f"{x + dx}_{y + dy}_{data[dy + y][dx + x]}",
                        weight = int(data[dy + y][dx + x])
                    )

    path = nx.shortest_path(
        graph,
        source = f"0_0_{data[0][0]}",
        target = f"{len(data[0]) - 1}_{len(data) - 1}_{data[-1][-1]}",
        weight = "weight"
    )

    total = 0
    for node in path[1:]:
        x, y, v = node.split("_")
        total += int(v)

    return total


if __name__ == '__main__':
    data = get_line_data("15")
    core_data = [list(map(int, row)) for row in data]

    print(f"part one: {solve(core_data)}")

    # multiply the core data by a factor of 5
    expanded_data = core_data[:]
    for x in range(1, 5):
        temp = np.array(core_data)
        temp += x

        expanded_data = [a + b for a, b in zip(expanded_data, temp.tolist())]

    core_expanded_data = expanded_data[:]

    for x in range(1, 5):
        temp = np.array(core_expanded_data)
        temp += x

        expanded_data += temp.tolist()

    for y in range(len(expanded_data)):
        for x in range(len(expanded_data[0])):
            while expanded_data[y][x] > 9:
                expanded_data[y][x] -= 9

    print(f"part two: {solve(expanded_data)}")
