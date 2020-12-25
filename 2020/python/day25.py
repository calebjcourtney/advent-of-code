from utils import get_line_data

from tqdm import tqdm


def root(a):
    for i in tqdm(range(100000000)):
        if pow(7, i, 20201227) == a:
            return i


if __name__ == '__main__':
    data = get_line_data("25")
    a, b = [int(i) for i in data]

    print(pow(a, root(b), 20201227))
