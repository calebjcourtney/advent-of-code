import re

from utils import get_line_data


def trace(wire, c):
    rule = c[wire]
    val = None

    # Base case
    if len(rule) == 1:
        if rule[0].isdigit():
            return int(rule[0])
        else:
            return trace(rule[0], c)

    elif len(rule) == 2:
        return ~trace(rule[1], c)

    else:
        if rule[0] == 'AND':
            val = (int(rule[1]) if rule[1].isdigit() else trace(rule[1], c)) & (int(rule[2]) if rule[2].isdigit() else trace(rule[2], c))
        elif rule[0] == 'OR':
            val = (int(rule[1]) if rule[1].isdigit() else trace(rule[1], c)) | (int(rule[2]) if rule[2].isdigit() else trace(rule[2], c))
        elif rule[0] == 'LSHIFT':
            val = trace(rule[1], c) << int(rule[2])
        elif rule[0] == 'RSHIFT':
            val = trace(rule[1], c) >> int(rule[2])

        if isinstance(val, int):
            c[wire] = (str(val),)

        return val


if __name__ == '__main__':
    data = get_line_data("07")

    connections = {}

    # Set up dictionary of connections
    for line in data:
        rule, wire = re.search(r'(.*) -> (.*)', line).groups()
        value = None

        if len(rule.split()) == 1:
            value = (rule,)
        elif 'NOT' in rule:
            value = ('NOT', rule.split()[1])
        else:
            value = (rule.split()[1], rule.split()[0], rule.split()[2])

        connections[wire] = value

    connections2 = connections.copy()

    s = trace('a', connections)

    print(s)

    connections2['b'] = (str(s), )

    print(trace('a', connections2))
