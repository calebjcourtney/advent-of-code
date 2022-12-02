from utils import get_line_data


winner = {
    "r": "s",
    "s": "p",
    "p": "r"
}


score = {
    "r": 1,
    "p": 2,
    "s": 3
}


class Round():
    p1: str
    p2: str
    outcome: int

    def part_one(self, p1, p2):
        mapping = {
            "A": "r",
            "B": "p",
            "C": "s",
            "X": "r",
            "Y": "p",
            "Z": "s"
        }

        self.p1 = mapping[p1]
        self.p2 = mapping[p2]

        return self.get_player_score()

    def part_two(self, p1, outcome):
        p1_mapping = {
            "A": "r",
            "B": "p",
            "C": "s",
        }

        self.p1 = p1_mapping[p1]

        p2_mapping = {
            "X": [v for k, v in winner.items() if k == self.p1][0],
            "Y": self.p1,
            "Z": [k for k, v in winner.items() if v == self.p1][0]
        }

        self.p2 = p2_mapping[outcome]

        return self.get_player_score()

    def get_player_score(self):
        if self.p1 == self.p2:
            return 3 + score[self.p2]

        return score[self.p2] + 6 * (winner[self.p2] == self.p1)


def part_one(data):
    p2_score = 0

    for p1, p2 in data:
        rnd = Round()
        p2_score += rnd.part_one(p1, p2)

    return p2_score


def part_two(data):
    p2_score = 0

    for p1, outcome in data:
        rnd = Round()
        p2_score += rnd.part_two(p1, outcome)

    return p2_score


if __name__ == '__main__':
    data = get_line_data("02")

    data = [record.split() for record in data]

    p1_result = part_one(data)
    print(f"part one: {p1_result}")

    p2_result = part_two(data)
    print(f"part two: {p2_result}")
