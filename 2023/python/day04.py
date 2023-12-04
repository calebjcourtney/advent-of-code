from utils import get_line_data

from collections import defaultdict
import re


def overlapping_nums(line: str):
    winning_nums = set(re.findall(r"(\d+)", line.split("|")[0].split(": ")[1]))
    my_nums = set(re.findall(r"(\d+)", line.split("|")[1]))
    return len(winning_nums & my_nums)


def combined(data):
    p1_result = 0
    p2_cards = defaultdict(int)

    for card_id, line in enumerate(data, start=1):
        matches = overlapping_nums(line)

        p2_cards[card_id] += 1

        if matches:
            p1_result += 2 ** (matches - 1)

        for copy_id in range(card_id + 1, card_id + matches + 1):
            p2_cards[copy_id] += p2_cards[card_id]

    return p1_result, sum(p2_cards.values())


if __name__ == '__main__':
    data = get_line_data("04")

    p1_result, p2_result = combined(data)
    print(p1_result)
    print(p2_result)
