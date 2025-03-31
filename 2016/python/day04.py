from utils import get_line_data
from utils import timeit
from utils import get_nums

from collections import Counter
from typing import NamedTuple


def shift_cipher(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    table[" "] = " "
    return text.translate(table)


class Room(NamedTuple):
    encrypted_name: str
    sector_id: int
    checksum: str

    def part_one(self):
        if set(self.checksum) & set(self.encrypted_name) != set(self.checksum):
            return False

        c = [(key, value) for key, value in Counter(self.encrypted_name).items() if key != " "]
        c.sort(key=lambda x: (-x[1], x[0]))
        if "".join(x[0] for x in c[:5]) == self.checksum:
            return self.sector_id

        return 0

    def part_two(self):
        shift = self.sector_id % 26
        return shift_cipher(self.encrypted_name, shift)


def parse_data(data) -> list[Room]:
    output = []
    for line in data:
        pieces = line.split("-")

        encrypted_name = " ".join(pieces[:-1])
        sector_id = get_nums(pieces[-1])[0]
        checksum = "".join(pieces[-1].split("[")[1].strip("]"))

        output.append(Room(encrypted_name, sector_id, checksum))

    return output


@timeit
def main(data):
    p1 = 0
    p2 = None
    for r in data:
        val = r.part_one()
        if p2 is None and r.part_two() == "northpole object storage":
            p2 = r.sector_id

        p1 += val

    return p1, p2



if __name__ == '__main__':
    data = get_line_data("04")
    data = parse_data(data)

    p1, p2 = main(data)
    print(p1)
    print(p2)
