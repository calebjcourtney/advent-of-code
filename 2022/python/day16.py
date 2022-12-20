from collections import defaultdict
import re

import networkx as nx

from utils import get_data


def parse_data(data):
    parsed = re.findall(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", data)

    G = nx.Graph()
    flow_rates = {"AA": 0}
    for valve in parsed:
        name = valve[0]
        flow_rate = int(valve[1])
        tunnels = valve[2].split(", ")

        if flow_rate > 0:
            flow_rates[name] = flow_rate

        for tun in tunnels:
            G.add_edge(name, tun)

    graph = defaultdict(list)
    for source in flow_rates:
        for dest in flow_rates:
            if source == dest:
                continue

            graph[source].append(
                (dest, nx.shortest_path_length(G, source, dest) + 1)
            )

    return graph, flow_rates


def get_flow_rate(source, dest, me, elephant, graph, flow_rates, total_flow_rate, visited, minutes):
    if minutes == 0:
        return total_flow_rate

    if me > 0 and elephant > 0:
        return get_flow_rate(
            source,
            dest,
            me - 1,
            elephant - 1,
            graph,
            flow_rates,
            total_flow_rate,
            visited,
            minutes - 1
        )

    best_flow_rate = total_flow_rate
    if me == 0:
        found_best = False

        for to, dist in graph[source]:
            if dist >= minutes or to in visited:
                continue

            found_best = True
            visited.add(to)

            flow_rate = get_flow_rate(
                to,
                dest,
                dist,
                elephant,
                graph,
                flow_rates,
                total_flow_rate + flow_rates[to] * (minutes - dist),
                visited,
                minutes,
            )
            visited.remove(to)

            if flow_rate > best_flow_rate:
                best_flow_rate = flow_rate

        if found_best:
            return best_flow_rate

    if elephant == 0:
        for to, dist in graph[dest]:
            if dist >= minutes or to in visited:
                continue

            visited.add(to)

            flow_rate = get_flow_rate(
                source,
                to,
                me,
                dist,
                graph,
                flow_rates,
                total_flow_rate + flow_rates[to] * (minutes - dist),
                visited,
                minutes,
            )
            visited.remove(to)

            if flow_rate > best_flow_rate:
                best_flow_rate = flow_rate

    return best_flow_rate


if __name__ == '__main__':
    data = get_data("16")
    graph, flow_rates = parse_data(data)

    print(get_flow_rate("AA", "AA", 0, 1000, graph, flow_rates, 0, {"AA"}, 30))
    print(get_flow_rate("AA", "AA", 0, 0, graph, flow_rates, 0, {"AA"}, 26))
