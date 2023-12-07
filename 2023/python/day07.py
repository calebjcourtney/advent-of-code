from utils import get_line_data
from utils import timeit

from collections import Counter

P1_CARD_RANKS = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
P2_CARD_RANKS = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")


class Hand:
    def __init__(self, line):
        self.cards, self.bid = line.split()
        self.bid = int(self.bid)

    def __lt__(self, other):
        s1 = Counter(self.cards)
        s2 = Counter(other.cards)

        if sorted(s1.values()) == sorted(s2.values()):
            for c1, c2 in zip(self.cards, other.cards):
                if c1 == c2:
                    continue
                return P1_CARD_RANKS.index(c1) < P1_CARD_RANKS.index(c2)

        # five of a kind
        if len(s1) == 1:
            return True
        elif len(s2) == 1:
            return False
        # four of a kind
        elif len(s1) == 2 and max(s1.values()) == 4:
            return True
        elif len(s2) == 2 and max(s2.values()) == 4:
            return False
        # full house
        elif len(s1) == 2 and max(s1.values()) == 3:
            return True
        elif len(s2) == 2 and max(s2.values()) == 3:
            return False
        # three of a kind
        elif len(s1) == 3 and max(s1.values()) == 3:
            return True
        elif len(s2) == 3 and max(s2.values()) == 3:
            return False
        # two pair
        elif len(s1) == 3 and max(s1.values()) == 2:
            return True
        elif len(s2) == 3 and max(s2.values()) == 2:
            return False
        # one pair
        elif len(s1) == 4 and max(s1.values()) == 2:
            return True
        elif len(s2) == 4 and max(s2.values()) == 2:
            return False
        else:
            raise ValueError(f"No winner, hands: {self.cards}, {other.cards}")

    def __repr__(self):
        return f"Hand({self.cards}, {self.bid})"


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
    for line in data:
        pass


if __name__ == '__main__':
    data = get_line_data("07")
#     data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483""".split("\n")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
