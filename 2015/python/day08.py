from utils import get_line_data

import ast


def comb(data):
    chars = 0
    lits = 0
    encoded_chars = 0

    for line in data:
        chars += len(line)
        lits += len(ast.literal_eval(line))
        encoded_chars += len(line.translate(str.maketrans({"\\": "\\\\", '"': '\\"'}))) + 2

    return chars - lits, encoded_chars - chars


if __name__ == '__main__':
    data = get_line_data("08")

    p1, p2 = comb(data)

    print(p1)
    print(p2)
