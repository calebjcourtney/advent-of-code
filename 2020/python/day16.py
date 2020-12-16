from utils import get_data

from typing import List, Set, Dict


def parse_rules_ranges(rules_ranges: List[str]) -> Dict[str, Set]:
    out = {}
    for line in rules_ranges.split("\n"):
        name, options = line.split(": ")

        a, b = options.split(" or ")

        r1, r2 = a.split("-")
        r3, r4 = b.split("-")

        out[name] = set(range(int(r1), int(r2) + 1)) | set(range(int(r3), int(r4) + 1))

        # not sure why this didn't work if anyone wants to offer insight
        # out[name] = lambda x: (int(r1) <= x <= int(r2)) or (int(r3) <= x <= int(r4))

    return out


def parse_ticket(lines: List[str]) -> List[int]:
    return [int(x) for x in lines.split("\n")[1].split(",")]


def parse_nearby_tickets(nearby_tickets: List[str]) -> List[List[int]]:
    out = []
    for ticket in nearby_tickets.split("\n")[1:]:
        out.append([int(x) for x in ticket.split(",")])

    return out


def part_one(rules_ranges: Dict[str, Set], nearby_tickets: List[List[int]]):
    total = 0

    for ticket in nearby_tickets:
        for value in ticket:
            # check if the value is valid for any of the options
            is_valid = any([value in valid_vals for name, valid_vals in rules_ranges.items()])

            if not is_valid:
                total += value

    return total


def is_valid_ticket(rules_ranges: Dict[str, Set], ticket: List[int]):
    # reuse code from above, but I'm not sure how to break them apart
    for value in ticket:
        is_valid = any([value in valid_vals for name, valid_vals in rules_ranges.items()])
        if not is_valid:
            return False

    return True


def part_two(rules_ranges: Dict[str, Set], your_ticket: List[int], nearby_tickets: List[List[int]]):
    # eliminate any tickets with invalid values
    valid_tickets = [ticket for ticket in nearby_tickets if is_valid_ticket(rules_ranges, ticket)]

    # set all indices as containing each name for the rules
    is_valids = [set([key for key in rules_ranges.keys()]) for _ in your_ticket]

    # keep iterating while we have more valid options than we should
    while sum(map(len, is_valids)) > len(is_valids):
        for ticket in valid_tickets:
            for index, value in enumerate(ticket):
                for key, range_vals in rules_ranges.items():
                    if value not in range_vals and key in is_valids[index]:
                        is_valids[index].remove(key)

        # if we know that one of the values is solved,
        # then we can go through and remove it from the other options
        for vals in is_valids:
            if len(vals) == 1:
                for others in is_valids:
                    if list(vals)[0] in others and vals != others:
                        others.remove(list(vals)[0])

    # yay! now we can spit out the data
    total = 1
    for index, value in enumerate(your_ticket):
        if "departure" in list(is_valids[index])[0]:
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
