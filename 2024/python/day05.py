from utils import get_data
from utils import timeit
from utils import get_nums


def parse_data(data: str) -> list[list[int]]:
    return [
        list(map(int, get_nums(record)))
        for record in data.split("\n")
    ]


def broken_rules(record: list[int], rules: list[list[int]]) -> tuple[bool, list[list[int]] | None]:
    broken_rules = []
    for rule in rules:
        if (
            set(rule) & set(record) == set(rule) and record.index(rule[0]) > record.index(rule[1])
        ):
            broken_rules.append(rule)

    return broken_rules


@timeit
def part_one(pages, rules):
    return sum(
        line[len(line) // 2]
        for line in pages
    )


@timeit
def part_two(pages, rules):
    output = 0
    for line in pages:
        broken = broken_rules(line, rules)
        while broken:
            for broken_rule in broken:
                (
                    line[line.index(broken_rule[0])],
                    line[line.index(broken_rule[1])],
                ) = (
                    line[line.index(broken_rule[1])],
                    line[line.index(broken_rule[0])],
                )

            broken = broken_rules(line, rules)

        output += line[len(line) // 2]

    return output


@timeit
def main(pages, rules):
    valid_pages = []
    invalid_pages = []
    for record in pages:
        if broken_rules(record, rules):
            invalid_pages.append(record)
        else:
            valid_pages.append(record)

    print(part_one(valid_pages, rules))
    print(part_two(invalid_pages, rules))


if __name__ == '__main__':
    data = get_data(5)
    rules, pages = data.split("\n\n")
    rules = parse_data(rules)
    pages = parse_data(pages)

    main(pages, rules)
