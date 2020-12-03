from utils import get_line_data

from numpy import prod


def get_trees(data, right, down):
    trees = 0
    for x in range(len(data)):
        if (x * down <= len(data)) and (data[x * down][(x * right) % len(data[0])] == "#"):
            trees += 1

    return trees


if __name__ == '__main__':
    data = get_line_data("03")
    print(get_trees(data, 3, 1))
    print(prod([get_trees(data, right, down) for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]))
