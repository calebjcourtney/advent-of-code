from utils import get_line_data


def part_one(line: str) -> bool:
    disallowed = ["ab", "cd", "pq", "xy"]
    for x in disallowed:
        if x in line:
            return False

    vowels = "aeiou"
    total = 0
    for x in vowels:
        total += line.count(x)

    if total < 3:
        return False

    for a, b in zip(line, line[1:]):
        if a == b:
            return True

    return False


def has_repeating(line) -> bool:
    """
        It contains a pair of any two letters that appears at least twice in the string without overlapping,
        like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    """

    for a, b in zip(line, line[1:]):
        if line.count(f"{a}{b}") > 1:
            return True

    return False


def has_separation(line: str) -> bool:
    """
    It contains at least one letter which repeats with exactly one letter between them,
    like xyx, abcdefeghi (efe), or even aaa.
    """

    for a, b in zip(line, line[2:]):
        if a == b:
            return True

    return False


def part_two(line: str) -> bool:
    return has_separation(line) and has_repeating(line)


if __name__ == '__main__':
    data = get_line_data("05")

    p1_result = sum(part_one(line) for line in data)
    print(p1_result)

    p2_result = sum(part_two(line) for line in data)
    print(p2_result)
