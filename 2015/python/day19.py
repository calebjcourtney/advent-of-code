from utils import get_data

import re


def get_distinct_changes(in_text, out_text, line):
    expected_len = len(line) - len(in_text) + len(out_text)
    output = set()
    matches = re.finditer(in_text, line)
    for match in matches:
        span = match.span()
        temp = f"{line[:span[0]]}{out_text}{line[span[1]:]}"
        assert len(temp) == expected_len, f"{len(temp)} != {expected_len}"

        output.add(temp)

    return output


def get_possible_mutations(mapping_data, sequences):
    output = set()
    for sequence in sequences:
        for in_text, out_text in mapping_data:
            changes = get_distinct_changes(in_text, out_text, sequence)
            output |= changes

    return output


def parse_mapping_data(mapping_data):
    output = []
    for line in mapping_data.split("\n"):
        in_text, out_text = re.match(r"(?P<in_text>\w+) => (?P<out_text>\w+)", line).groups()
        output.append((in_text, out_text))

    return output


def part_one(mapping_data, sequence):
    output = set()
    for in_text, out_text in mapping_data:
        temp = get_distinct_changes(in_text, out_text, sequence)
        output |= temp

    return len(output)


def part_two(medicine_molecule):
    elements = len(re.findall(r'[A-Z]', medicine_molecule))
    radon = len(re.findall(r'Rn', medicine_molecule))
    yttrium = len(re.findall(r'Y', medicine_molecule))

    return elements - (2 * radon) - (2 * yttrium) - 1


if __name__ == '__main__':
    data = get_data("19")
    mapping_data, sequence = data.split("\n\n")
    mapping_data = parse_mapping_data(mapping_data)

    p1_result = part_one(mapping_data, sequence)
    print(p1_result)

    p2_result = part_two(sequence)
    print(p2_result)
