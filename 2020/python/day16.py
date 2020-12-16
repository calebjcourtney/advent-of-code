from utils import get_data, get_line_data, get_int_data

from utils import re_split


def parse_rules_ranges(rules_ranges):
    out = {}
    for line in rules_ranges.split("\n"):

        name, options = line.split(": ")

        a, b = options.split(" or ")

        r1, r2 = a.split("-")
        r3, r4 = b.split("-")

        out[name] = set()

        for x in range(int(r1), int(r2) + 1):
            out[name].add(x)

        for x in range(int(r3), int(r4) + 1):
            out[name].add(x)

        # not sure why this didn't work
        # out[name] = lambda x: (int(r1) <= x <= int(r2)) or (int(r3) <= x <= int(r4))

    return out


def parse_ticket(lines):
    ticket_nums = [int(x) for x in lines.split("\n")[1].split(",")]
    return ticket_nums


def parse_nearby_tickets(nearby_tickets):
    out = []
    for ticket in nearby_tickets.split("\n")[1:]:
        out.append([int(x) for x in ticket.split(",")])

    return out


def part_one(rules_ranges, your_ticket, nearby_tickets):
    rules_ranges = parse_rules_ranges(rules_ranges)
    your_ticket = parse_ticket(your_ticket)
    nearby_tickets = parse_nearby_tickets(nearby_tickets)

    total = 0

    for ticket in nearby_tickets:
        for value in ticket:
            is_valid = any([value in valid_vals for name, valid_vals in rules_ranges.items()])

            if not is_valid:
                total += value

    return total


def is_valid_ticket(rules_ranges, ticket):
    for value in ticket:
        is_valid = any([value in valid_vals for name, valid_vals in rules_ranges.items()])
        if not is_valid:
            return False

    return True


def part_two(rules_ranges, your_ticket, nearby_tickets):
    rules_ranges = parse_rules_ranges(rules_ranges)
    your_ticket = parse_ticket(your_ticket)
    nearby_tickets = parse_nearby_tickets(nearby_tickets)

    valid_tickets = [ticket for ticket in nearby_tickets if is_valid_ticket(rules_ranges, ticket)]

    is_valids = [set([key for key in rules_ranges.keys()]) for _ in your_ticket]

    while sum(map(len, is_valids)) > len(is_valids):
        for ticket in valid_tickets:
            for index, value in enumerate(ticket):
                for key, range_vals in rules_ranges.items():
                    if value not in range_vals and key in is_valids[index]:
                        is_valids[index].remove(key)

        for vals in is_valids:
            if len(vals) == 1:
                for others in is_valids:
                    if list(vals)[0] in others and vals != others:
                        others.remove(list(vals)[0])

    total = 1
    for index, value in enumerate(your_ticket):
        if "departure" in list(is_valids[index])[0]:
            total *= your_ticket[index]

    return total


if __name__ == '__main__':
    data = get_data("16")

    rules_ranges, your_ticket, nearby_tickets = data.split("\n\n")

    p1_result = part_one(rules_ranges, your_ticket, nearby_tickets)
    print(p1_result)

    p2_result = part_two(rules_ranges, your_ticket, nearby_tickets)
    print(p2_result)
