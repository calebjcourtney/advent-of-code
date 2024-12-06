from collections import defaultdict

from utils import get_data
from utils import timeit
from utils import get_nums


def parse_data(data: str) -> list[list[int]]:
    return list(map(get_nums, data.split("\n")))


@timeit
def main(pages: list[list[int]], rules: list[list[int]]) -> None:
    orders = defaultdict(set)
    for rule in rules:
        orders[rule[0]].add(rule[1])

    part_1 = 0
    part_2 = 0

    for record in pages:
        sorted_record = sorted(
            record,
            key=lambda num: -len(orders[num] & set(record)),
        )
        if record == sorted_record:
            part_1 += record[len(record) // 2]
        else:
            part_2 += sorted_record[len(sorted_record) // 2]

    print(part_1)
    print(part_2)


if __name__ == '__main__':
    data = get_data(5)
    rules, pages = data.split("\n\n")
    pages = parse_data(pages)
    rules = parse_data(rules)

    main(pages, rules)
