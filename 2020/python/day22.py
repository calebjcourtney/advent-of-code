from utils import get_data

from typing import List, Tuple


def part_one(p1_deck: List[int], p2_deck: List[int]) -> int:
    while p1_deck and p2_deck:
        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)

        if p1_card > p2_card:
            winner = p1_deck

        elif p2_card > p1_card:
            winner = p2_deck

        winner.append(max(p1_card, p2_card))
        winner.append(min(p1_card, p2_card))

    best_deck = p1_deck or p2_deck

    return sum(i * v for i, v in enumerate(reversed(best_deck), 1))


def part_two(p1_deck: List[int], p2_deck: List[int]) -> Tuple[bool, List[int]]:
    seen = set()
    while p1_deck and p2_deck:

        # if we've already seen this order, then player 1 wins
        deck_order = (tuple(p1_deck), tuple(p2_deck))
        if deck_order in seen:
            return 1, p1_deck

        seen.add(deck_order)

        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)

        # run the new rules
        if len(p1_deck) >= p1_card and len(p2_deck) >= p2_card:
            winnum, sub_deck = part_two(
                p1_deck[:p1_card],
                p2_deck[:p2_card],
            )
            winner = p1_deck if winnum else p2_deck

        # old rules
        elif p1_card > p2_card:
            winner = p1_deck

        elif p2_card > p1_card:
            winner = p2_deck

        winner.append(p1_card if winner is p1_deck else p2_card)
        winner.append(p2_card if winner is p1_deck else p1_card)

    return 1 if winner is p1_deck else 0, winner


if __name__ == '__main__':
    data = get_data("22")

    # part one
    player1, player2 = data.split("\n\n")
    p1_deck = list(map(int, player1.split("\n")[1:]))
    p2_deck = list(map(int, player2.split("\n")[1:]))
    print(part_one(p1_deck, p2_deck))

    # part two
    p1_deck = list(map(int, player1.split("\n")[1:]))
    p2_deck = list(map(int, player2.split("\n")[1:]))
    winner, best_deck = part_two(p1_deck, p2_deck)
    print(sum(i * v for i, v in enumerate(reversed(best_deck), 1)))
