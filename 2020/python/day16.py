from utils import get_data, special_split

from typing import List, Set, Dict


class Rule(object):
    def __init__(self, name: str, r1: int, r2: int, r3: int, r4: int):
        self.name = name

        self.r1 = int(r1)
        self.r2 = int(r2)
        self.r3 = int(r3)
        self.r4 = int(r4)

    def is_valid(self, num: int):
        return self.r1 <= num <= self.r2 or self.r3 <= num <= self.r4


def parse_rules_ranges(rules_ranges: List[str]) -> Dict[str, Set]:
    out = []
    for line in rules_ranges.split("\n"):
        name, r1, r2, r3, r4 = special_split(line, [": ", " or ", "-"])

        rule = Rule(name, r1, r2, r3, r4)

        out.append(rule)

    return out


def parse_ticket(lines: List[str]) -> List[int]:
    return [int(x) for x in lines.split("\n")[1].split(",")]


def parse_nearby_tickets(nearby_tickets: List[str]) -> List[List[int]]:
    out = []
    for ticket in nearby_tickets.split("\n")[1:]:
        out.append([int(x) for x in ticket.split(",")])

    return out


def part_one(rules_ranges: List['Rule'], nearby_tickets: List[List[int]]):
    total = 0

    for ticket in nearby_tickets:
        for value in ticket:
            # check if the value is valid for any of the options
            is_valid = any([rule.is_valid(value) for rule in rules_ranges])

            if not is_valid:
                total += value

    return total


def is_valid_ticket(rules_ranges: Dict[str, Set], ticket: List[int]):
    # reuse code from above, but I'm not sure how to break them apart
    for value in ticket:
        is_valid = any([rule.is_valid(value) for rule in rules_ranges])
        if not is_valid:
            return False

    return True


def part_two(rules_ranges: Dict[str, Set], your_ticket: List[int], nearby_tickets: List[List[int]]):
    # eliminate any tickets with invalid values
    nearby_tickets = [ticket for ticket in nearby_tickets if is_valid_ticket(rules_ranges, ticket)]

    # set all indices as containing each name for the rules
    valid_options = [set([rule.name for rule in rules_ranges]) for _ in your_ticket]

    # keep iterating while we have more valid options than we should
    while sum(map(len, valid_options)) > len(valid_options):
        # iterate through the nearby tickets
        for ticket in nearby_tickets:

            # look through the values in each ticket
            for index, value in enumerate(ticket):

                # look through the params of each rule
                for rule in rules_ranges:

                    # if the value for the column is not in the valid range for the rules
                    # and the name of that rule is still in our valid options
                    if not rule.is_valid(value) and rule.name in valid_options[index]:
                        valid_options[index].remove(rule.name)

        # if we know that one of the values is solved,
        # then we can go through and remove it from the other options
        for vals in valid_options:
            if len(vals) == 1:
                for others in valid_options:
                    if list(vals)[0] in others and vals != others:
                        others.remove(list(vals)[0])

    # convert the List[Set[str]] to List[str]
    valid_options = [list(val)[0] for val in valid_options]

    # yay! now we can spit out the data
    total = 1
    for index, value in enumerate(your_ticket):
        if "departure" in valid_options[index]:
            total *= your_ticket[index]

    return total


if __name__ == '__main__':
    data = get_data("16")

    rules_ranges, your_ticket, nearby_tickets = data.split("\n\n")

    rules_ranges = parse_rules_ranges(rules_ranges)
    your_ticket = parse_ticket(your_ticket)
    nearby_tickets = parse_nearby_tickets(nearby_tickets)

    p1_result = part_one(rules_ranges, nearby_tickets)
    print(p1_result)

    p2_result = part_two(rules_ranges, your_ticket, nearby_tickets)
    print(p2_result)
