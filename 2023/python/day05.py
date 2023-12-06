from typing import NamedTuple

from utils import get_data
from utils import timeit


class Map(NamedTuple):
    destination: int
    source: int
    size: int


class Mapper:
    def __init__(self, lines):
        lines = lines.split("\n")[1:]
        self.maps: list[Map] = [Map(*[int(x) for x in line.split()]) for line in lines]

    def solve(self, current_range):
        out_of_bounds_range = []
        for resource_map in self.maps:
            src_end = resource_map.source + resource_map.size
            new_range = []
            while current_range:
                (start, end) = current_range.pop()
                before = (start, min(end, resource_map.source))
                interior = (max(start, resource_map.source), min(src_end, end))
                after = (max(src_end, start), end)
                if before[1] > before[0]:
                    new_range.append(before)
                if interior[1] > interior[0]:
                    out_of_bounds_range.append(
                        (
                            interior[0] - resource_map.source + resource_map.destination,
                            interior[1] - resource_map.source + resource_map.destination,
                        )
                    )
                if after[1] > after[0]:
                    new_range.append(after)

            current_range = new_range

        return out_of_bounds_range + current_range


def parse_data(data):
    seed, *others = data.split("\n\n")
    seed = [int(x) for x in seed.split(":")[1].split()]

    return seed, others


@timeit
def part_one(seed, mappers):
    output = []
    for x in seed:
        current_range = [(x, x + 1)]
        for mp in mappers:
            current_range = mp.solve(current_range)

        output.append(min(current_range)[0])

    return min(output)


@timeit
def part_two(seed, mappers):
    output = []
    pairs = list(zip(seed[::2], seed[1::2]))
    for start, size in pairs:
        current_range = [(start, start + size)]
        for mp in mappers:
            current_range = mp.solve(current_range)
        output.append(min(current_range)[0])

    return min(output)


if __name__ == "__main__":
    data = get_data("05")
    seed, others = parse_data(data)
    mappers = [Mapper(x) for x in others]

    print(part_one(seed, mappers))
    print(part_two(seed, mappers))
