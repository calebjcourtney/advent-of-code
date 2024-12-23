import networkx as nx

from utils import get_line_data, timeit


@timeit
def main(data):
    data = [line.split("-") for line in data]
    graph = nx.Graph()
    graph.add_edges_from(data)

    triangles = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3]

    p1 = 0
    for triangle in triangles:
        p1 += any(node.startswith("t") for node in triangle)

    print(p1)

    cliques = list(nx.find_cliques(graph))
    largest_clique = max(cliques, key=len)
    print(",".join(sorted(largest_clique)))


if __name__ == "__main__":
    data = get_line_data("23")

    main(data)
