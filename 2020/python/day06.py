from utils import get_data

from typing import List


def part_one(data: List[str]) -> int:
    data = [record.replace("\n", "") for record in data]
    data = [set(record) for record in data]

    total = sum([len(record) for record in data])

    return total


def part_two(data: List[str]) -> int:
    total = 0
    for record in data:
        cur = None
        for passenger in record.split("\n"):
            temp = set(x for x in passenger)

            if cur is None:
                cur = temp
            else:
                cur = cur & temp

        total += len(cur)

    return total


if __name__ == '__main__':
    data = get_data("06")
    data = data.split("\n\n")

    print(part_one(data))
    print(part_two(data))
