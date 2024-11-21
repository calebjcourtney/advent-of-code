from utils import get_data
from utils import get_line_data
from utils import get_int_data
from utils import timeit

import matplotlib.pyplot as plt
import networkx as nx


def parse_data(data: list[str]) -> nx.Graph:
    output = []
    for line in data:
        source, target = line.split(":")
        targets = target.split()
        for target in targets:
            output.append((source, target))

    graph = nx.Graph()

    graph.add_edges_from(output)

    return graph


@timeit
def part_one(data):
    cut_edges = nx.minimum_edge_cut(data)
    for edge in cut_edges:
        data.remove_edge(*edge)

    connected_components = list(nx.connected_components(data))
    cluster_sizes = [len(component) for component in connected_components]

    assert len(cluster_sizes) == 2

    return cluster_sizes[0] * cluster_sizes[1]



if __name__ == '__main__':
    data = get_line_data("25")
    data = parse_data(data)

    p1_result = part_one(data)
    print(p1_result)
