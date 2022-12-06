from utils import get_line_data

P1_REQUIREMENTS = {
    "children": lambda x: x == 3,
    "cats": lambda x: x == 7,
    "samoyeds": lambda x: x == 2,
    "pomeranians": lambda x: x == 3,
    "akitas": lambda x: x == 0,
    "vizslas": lambda x: x == 0,
    "goldfish": lambda x: x == 5,
    "trees": lambda x: x == 3,
    "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1
}


P2_REQUIREMENTS = {
    "children": lambda x: x == 3,
    "cats": lambda x: x > 7,
    "samoyeds": lambda x: x == 2,
    "pomeranians": lambda x: x < 3,
    "akitas": lambda x: x == 0,
    "vizslas": lambda x: x == 0,
    "goldfish": lambda x: x < 5,
    "trees": lambda x: x > 3,
    "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1
}


def parse_line(line):
    index = int(line.split(":")[0].split()[1])

    info = {}
    other_values = ": ".join(line.split(": ")[1:])
    for record in other_values.split(", "):
        key, value = record.split(": ")
        value = int(value)
        info[key] = value

    return {index: info}


def parse_data(data):
    output = {}
    for line in data:
        output |= parse_line(line)

    return output


def aunt_is_match(aunt, requirements):
    for key, value in requirements.items():
        if key not in aunt:
            continue

        if not value(aunt[key]):
            return False

    return True


def part_one(data):
    for index, info in data.items():
        if aunt_is_match(info, P1_REQUIREMENTS):
            return index


def part_two(data):
    for index, info in data.items():
        if aunt_is_match(info, P2_REQUIREMENTS):
            return index


if __name__ == '__main__':
    data = get_line_data("16")
    data = parse_data(data)

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
