from utils import get_line_data, timeit, memoize


GRAPH = {}


def build_graph(data):
    for line in data:
        device, outputs = line.split(": ", 1)
        GRAPH[device.strip()] = [out.strip() for out in outputs.split()]

    GRAPH["out"] = []


@memoize
def count_paths(start, end):
    if start == end:
        return 1

    if start == "out":
        return 0

    return sum(count_paths(neighbor, end) for neighbor in GRAPH[start])


@timeit
def main():
    data = get_line_data("11")
    build_graph(data)

    part_one = count_paths("you", "out")
    print(part_one)

    part_two = count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out") + count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")
    print(part_two)
