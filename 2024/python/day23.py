import networkx as nx

from utils import get_line_data, timeit


@timeit
def main(data):
    data = [line.split("-") for line in data]
    g = nx.Graph()
    g.add_edges_from(data)

    cliques = [clique for clique in nx.enumerate_all_cliques(g)]
    triangles = [clique for clique in cliques if len(clique) == 3]

    p1 = 0
    for triangle in triangles:
        p1 += any(node.startswith("t") for node in triangle)

    print(p1)

    biggest_clique = None
    for clique in cliques:
        if biggest_clique is None or len(clique) > len(biggest_clique):
            biggest_clique = clique

    print(",".join(sorted(biggest_clique)))


if __name__ == "__main__":
    data = get_line_data("23")

    main(data)
