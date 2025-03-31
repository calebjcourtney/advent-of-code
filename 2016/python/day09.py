import re

from utils import get_data
from utils import timeit

marker_re = re.compile(r'(\d+)x(\d+)')


def main(data, improved=False):
    found = re.findall(marker_re, data)
    if not found:
        return len(data)

    length = 0

    take, repeat = (int(x) for x in found[0])

    # Find start and end indices of first marker
    start = data.index('(')
    end = data.index(')')

    length += start

    data = data[end+1:]
    to_repeat = data[:take]

    if '(' in to_repeat and improved:
        length += main(to_repeat, improved) * repeat
    else:
        length += take * repeat

    return length + main(data[take:], improved)


if __name__ == '__main__':
    data = get_data("09")

    print("Length of original format:", main(data))
    print("Length of improved format:", main(data, improved=True))
