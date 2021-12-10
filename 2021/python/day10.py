from utils import get_line_data

from collections import Counter


POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

INCOMPLETE_POINTS = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def find_symbols(line: str):
    start_end = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    expecting = line[0]
    for index, character in enumerate(line[1:], start = 1):
        if character not in start_end.keys() and character != expecting:
            return character

        expecting = character

    return None


def clean_line(line):
    while "()" in line:
        line = line.replace("()", "")

    while "{}" in line:
        line = line.replace("{}", "")

    while "[]" in line:
        line = line.replace("[]", "")

    while "<>" in line:
        line = line.replace("<>", "")

    if "()" in line or "{}" in line or "[]" in line or "<>" in line:
        return clean_line(line)
    else:
        return line


def line_is_incomplete(line):
    cleaned = clean_line(line)
    for char in cleaned:
        if char in POINTS.keys():
            return False

    return True


def part_one(data):
    symbols = ""
    for line in data:
        cleaned = clean_line(line)
        for char in cleaned:
            if char in POINTS.keys():
                symbols += char
                break

    c = Counter(symbols)

    return sum([POINTS[key] * value for key, value in c.items()])


def part_two(data):
    scores = []
    for line in data:
        if line_is_incomplete(line):
            cleaned = clean_line(line)
            rev_cleaned = cleaned[::-1]

            c = 0
            for char in rev_cleaned:
                c = c * 5 + INCOMPLETE_POINTS[char]

            scores.append(c)

    scores.sort()

    return scores[len(scores) // 2]


if __name__ == '__main__':
    data = get_line_data("10")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
