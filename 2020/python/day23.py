from typing import List


class Cup:
    def __init__(self, value: int, after: 'Cup' = None):
        self.value = value
        self.after = after

    def __repr__(self):
        return f"({self.value})"


class Cups:
    def __init__(self, cups: List[Cup], max_val: int):
        self.cups = cups
        self.max_val = max_val

        for first, second in zip(self.cups, self.cups[1:]):
            first.after = second

        cups[-1].after = cups[0]

        self.current_cup = cups[0]

        self.lookup = {}
        for cup in self.cups:
            self.lookup[cup.value] = cup

    def move(self):
        # the next three values
        # is there a better way to do this?
        second = self.current_cup.after
        third = second.after
        fourth = third.after

        self.current_cup.after = fourth.after

        current_value = self.current_cup.value

        used = [current_value, second.value, third.value, fourth.value]

        # get the next available number (which will be some lower number not in the above four)
        while current_value in used:
            current_value -= 1
            if current_value == 0:
                current_value = self.max_val

        # insert between these two cups
        insert_after = self.lookup[current_value]
        insert_before = insert_after.after

        # assign the insertion
        insert_after.after = second
        fourth.after = insert_before

        # new current cup
        self.current_cup = self.current_cup.after


def part_one(data: List[int]) -> str:
    cups = Cups([Cup(record) for record in data], max(data))
    for _ in range(100):
        cups.move()

    output = ""
    current = cups.lookup[1].after
    while current.value != 1:
        output += str(current.value)
        current = current.after

    return output


def part_two(cups: List[int]) -> int:
    cups = [Cup(cup) for cup in cups]

    cur = 10
    while len(cups) < 1000000:
        cups.append(Cup(cur))
        cur += 1

    cups = Cups(cups, 1000000)

    for _ in range(10000000):
        cups.move()

    cup_one = cups.lookup[1]
    first = cup_one.after
    second = first.after

    return first.value * second.value


if __name__ == '__main__':
    data = list(map(int, "198753462"))

    print(part_one(data))
    print(part_two(data))
