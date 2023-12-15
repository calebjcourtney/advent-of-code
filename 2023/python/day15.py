from utils import get_data
from utils import timeit

from typing import NamedTuple


def hash(chars: str):
    current_value = 0
    for char in chars:
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value


class Lens(NamedTuple):
    label: str
    power: int


class Box:
    def __init__(self, id):
        self.id = id
        self.lenses = []

    def update(self, new_lens: Lens):
        for index, l in enumerate(self.lenses):
            if l.label == new_lens.label:
                self.lenses[index] = new_lens
                return

        self.lenses.append(new_lens)

    def remove(self, new_lens: Lens):
        self.lenses = [lens for lens in self.lenses if lens.label != new_lens.label]

    @property
    def value(self):
        return sum((self.id + 1) * slot * lens.power for slot, lens in enumerate(self.lenses, 1))


@timeit
def part_one(data):
    return sum(map(hash, data))


@timeit
def part_two(data):
    boxes = [Box(id) for id in range(256)]
    for seq in data:
        if "=" in seq:
            label, power = seq.split("=")
            power = int(power)
            boxes[hash(label)].update(Lens(label, power))
        elif "-" in seq:
            label = seq[:-1]
            boxes[hash(label)].remove(Lens(label, 0))

    return sum(box.value for box in boxes)


if __name__ == '__main__':
    data = get_data("15")
    initialization_seq = data.split(",")

    print(part_one(initialization_seq))
    print(part_two(initialization_seq))
