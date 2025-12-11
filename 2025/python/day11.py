from utils import get_line_data, timeit, memoize


GRAPH = {}


def build_graph(data):
    for line in data:
        device, outputs = line.split(": ", 1)
        GRAPH[device.strip()] = [out.strip() for out in outputs.split()]

    GRAPH["out"] = []


@memoize
def count_paths(curr, end, has_visited_dac, has_visited_fft):
    if curr == "fft":
        has_visited_dac = True
    if curr == "dac":
        has_visited_fft = True

    if curr == end:
        return 1 if has_visited_dac and has_visited_fft else 0

    return sum(
        count_paths(neighbor, end, has_visited_dac, has_visited_fft)
        for neighbor in GRAPH[curr]
    )


@timeit
def main():
    data = get_line_data("11")
    build_graph(data)

    part_one = count_paths("you", "out", True, True)
    print(part_one)

    part_two = count_paths("svr", "out", False, False)
    print(part_two)
