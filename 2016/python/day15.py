from utils import get_line_data
from utils import timeit
from utils import get_nums
from typing import NamedTuple


class Disc(NamedTuple):
    id: int
    positions: int
    start_position: int

    @property
    def least(self):
        return self.positions - ((self.start_position + self.id) % self.positions)

    def sample(self, benchmark=None):
        if benchmark is None:
            return {self.least + (self.positions * i) for i in range(1000000)}
        else:
            output = set()
            for i in range(1000000):
                b = self.least + (self.positions * i)
                if b > benchmark:
                    return output

                output.add(b)

            return output


def parse_line(line):
    disc_id, positions, _, start_position = get_nums(line)
    return Disc(disc_id, positions, start_position)


@timeit
def part_one(data):
    first = data[0].sample()
    for record in data[1:]:
        first &= record.sample(max(first))
    return min(first)


@timeit
def part_two(data):
    first = data[0].sample()
    for record in data[1:]:
        first &= record.sample(max(first))
    return min(first)


if __name__ == '__main__':
    data = get_line_data("15")
    data = list(map(parse_line, data))
    print({record: record.least for record in data})

    p1_result = part_one(data)
    print(p1_result)

    data.append(Disc(data[-1].id + 1, 11, 0))

    p2_result = part_two(data)
    print(p2_result)
