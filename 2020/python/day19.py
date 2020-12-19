from utils import get_data

from typing import List, Dict

import re


def part_one_re(rule_num: str, rules: Dict[str, str]) -> str:
    rule = rules[rule_num]

    if re.fullmatch(r'"."', rule):
        return rule[1]

    else:
        parts = rule.split(' | ')
        res = []

        for part in parts:
            nums = part.split(' ')

            # yay recursion
            res.append(''.join(part_one_re(num, rules) for num in nums))

        return '(?:' + '|'.join(res) + ')'


def part_one(rules: Dict[str, str], text: List[str]) -> int:
    zero_re = part_one_re("0", rules)
    count = 0

    for line in text:
        if re.fullmatch(zero_re, line):
            count += 1

    return count


def part_two_re(rule_num: str, rules: Dict[str, str]) -> str:
    # yay for hacky code
    if rule_num == '8':
        return part_two_re('42', rules) + '+'
    elif rule_num == '11':
        a = part_two_re('42', rules)
        b = part_two_re('31', rules)

        # make it so long that it should cover every option on the inputs
        out = f"(?:{a}{{{1}}}{b}{{{1}}}"
        for n in range(2, 300):
            out += f"|{a}{{{n}}}{b}{{{n}}}"

        out += ")"

        return out

    rule = rules[rule_num]

    if re.fullmatch(r'"."', rule):
        return rule[1]

    else:
        parts = rule.split(' | ')
        results = []

        for part in parts:
            sub_nums = part.split(' ')

            # yay recursion
            results.append(''.join(part_two_re(sub_num, rules) for sub_num in sub_nums))

        return '(?:' + '|'.join(results) + ')'


def part_two(rules: Dict[str, str], text: List[str]) -> int:
    zero_re = part_two_re("0", rules)
    count = 0

    for line in text:
        if re.fullmatch(zero_re, line):
            count += 1

    return count


if __name__ == '__main__':
    data = get_data("19")

    rules, text = data.split("\n\n")
    rules = dict([rule.split(': ') for rule in rules.split('\n')])
    text = text.split("\n")

    p1_result = part_one(rules, text)
    print(p1_result)

    p2_result = part_two(rules, text)
    print(p2_result)
