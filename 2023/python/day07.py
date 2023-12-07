from utils import get_line_data
from utils import timeit

from collections import Counter


P1_CARD_RANKS = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
P2_CARD_RANKS = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")


class Hand:
    def __init__(self, line, part_one=True):
        self.cards, self.bid = line.split()
        self.bid = int(self.bid)
        self.part_one = part_one

    def strength(self):
        card_counter = Counter(self.cards)

        if not self.part_one:
            # if 'J' is in count, take the value and add it to the largest other value in count
            # of
            if "J" in card_counter and len(card_counter) > 1:
                j_val = card_counter["J"]
                del card_counter["J"]
                for letter, count in card_counter.most_common(5):
                    card_counter[letter] += j_val
                    break

        if self.part_one:
            card_vals = tuple(P1_CARD_RANKS.index(x) for x in self.cards)
        else:
            card_vals = tuple(P2_CARD_RANKS.index(x) for x in self.cards)

        max_card_counter = max(card_counter.values())

        # five of a kind
        if len(card_counter) == 1:
            return 0, card_vals
        # four of a kind
        elif len(card_counter) == 2 and max_card_counter == 4:
            return 1, card_vals
        # full house
        elif len(card_counter) == 2 and max_card_counter == 3:
            return 2, card_vals
        # three of a kind
        elif len(card_counter) == 3 and max_card_counter == 3:
            return 3, card_vals
        # two pair
        elif len(card_counter) == 3 and max_card_counter == 2:
            return 4, card_vals
        # one pair
        elif len(card_counter) == 4 and max_card_counter == 2:
            return 5, card_vals
        elif len(card_counter) == 5:
            return 6, card_vals
        else:
            raise ValueError(f"Unknown: {self.cards}")

    def __lt__(self, other):
        assert self.part_one == other.part_one
        return self.strength() < other.strength()


@timeit
def part_one(data):
    hands = [Hand(line) for line in data]
    hands.sort(reverse=True)

    output = 0
    for rank, hand in enumerate(hands, start=1):
        output += rank * hand.bid

    return output


@timeit
def part_two(data):
    hands = [Hand(line, part_one=False) for line in data]
    hands.sort(reverse=True)

    output = 0
    for rank, hand in enumerate(hands, start=1):
        output += rank * hand.bid

    return output


if __name__ == '__main__':
    data = get_line_data("07")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
