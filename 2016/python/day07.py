from utils import get_line_data
from utils import timeit

import re
from typing import NamedTuple


ENCLOSED = re.compile(r"\[\w+\]")
BEFORE = re.compile(r"^\w+\[")
END = re.compile(r"\]\w+$")
BETWEEN = re.compile(r"\]\w+\[")


class Code(NamedTuple):
    ip_sequences: list[str]
    hyp_sequences: list[str]

    def supports_tls(self):
        for hyp in self.hyp_sequences:
            if has_abba(hyp):
                return False

        for ip in self.ip_sequences:
            if has_abba(ip):
                return True

        return False

    def supports_ssl(self):
        abas = []
        for ip in self.ip_sequences:
            for i in range(len(ip) - 2):
                if is_chiasm(ip[i:i + 3]):
                    abas.append(ip[i:i + 3])

        for aba in abas:
            for hyp in self.hyp_sequences:
                if f"{aba[1]}{aba[0]}{aba[1]}" in hyp:
                    return True

        return False


def parse_data(data):
    output = []
    for line in data:
        hyp_sequences = ENCLOSED.findall(line)

        ip_sequences = []
        b = BEFORE.search(line)
        assert b is not None
        ip_sequences.append(b.group())
        e = END.search(line)
        assert e is not None
        ip_sequences.append(e.group())
        between_vals = BETWEEN.findall(line)
        ip_sequences.extend(between_vals)

        output.append(Code(ip_sequences, hyp_sequences))

    return output


def is_chiasm(text):
    return text[0] != text[1] and text == text[::-1]


def has_abba(text):
    if len(text) < 4:
        return False

    for i in range(len(text)-3):
        if is_chiasm(text[i:i+4]):
            return True

    return False


@timeit
def main(data):
    return (
        sum(c.supports_tls() for c in data),
        sum(c.supports_ssl() for c in data),
    )


if __name__ == '__main__':
    data = get_line_data("07")
    data = parse_data(data)

    p1, p2 = main(data)
    print(p1)
    print(p2)
