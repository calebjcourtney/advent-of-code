from utils import get_line_data

from typing import List, Dict, Tuple


def parse_codes_allergens(line: str) -> Tuple[List[str], List[str]]:
    codes, allergens = line.split(" (contains ")

    codes = codes.split()
    allergens = allergens[:-1].split(", ")

    return codes, allergens


def process_data(data: List[str]) -> Dict[str, List[str]]:
    mapping = {}
    for line in data:
        codes, allergens = parse_codes_allergens(line)

        for allergen in allergens:
            if allergen not in mapping:
                mapping[allergen] = set(codes)
            else:
                mapping[allergen] &= set(codes)

    return mapping


def code_is_allergen(code: str, processed_info: Dict[str, List[str]]) -> bool:
    for value in processed_info.values():
        if code in value:
            return True

    return False


def part_one(data: List[str], processed_info: Dict[str, List[str]]):
    output = []
    for line in data:
        codes, allergens = parse_codes_allergens(line)

        for code in codes:
            if not code_is_allergen(code, processed_info):
                output.append(code)

    return len(output)


def continue_process(processed_info: Dict[str, List[str]]):
    for value in processed_info.values():
        if len(value) > 1:
            return True

    return False


def part_two(processed_info: Dict[str, List[str]]):
    needs_processing = True

    while needs_processing:
        for key in processed_info.keys():
            if len(processed_info[key]) == 1:
                for key_2 in processed_info.keys():
                    if key == key_2:
                        continue

                    processed_info[key_2].discard(list(processed_info[key])[0])

        needs_processing = continue_process(processed_info)

    output = []
    for key, value in processed_info.items():
        output.append((key, list(value)[0]))

    output.sort(key=lambda x: x[0])

    return ",".join(x[1] for x in output)


if __name__ == '__main__':
    data = get_line_data("21")

    processed = process_data(data)

    print(part_one(data, processed))
    print(part_two(processed))
