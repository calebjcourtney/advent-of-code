from utils import get_line_data
from utils import timeit
from utils import rotate_text

from collections import Counter
import numpy as np


@timeit
def main(data):
    data = [np.array([x for x in line]) for line in data]
    data = np.transpose(data)

    p1 = ""
    p2 = ""
    for row in data:
        c = Counter(row)
        p1 += c.most_common(1)[0][0]
        p2 += c.most_common(len(c))[-1][0]

    return p1, p2


if __name__ == '__main__':
    data = get_line_data("06")

    p1, p2 = main(data)
    print(p1)
    print(p2)
