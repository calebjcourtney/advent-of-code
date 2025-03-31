import hashlib

from utils import get_data
from utils import timeit


def get_next_character(data, seed):
    pass


@timeit
def main(data):
    seed = 0
    p1 = ""
    p2 = [None for _ in range(8)]
    while None in p2:
        cur = f"{data}{seed}"
        d = hashlib.md5(cur.encode("utf8")).hexdigest()
        if d.startswith("00000"):
            if len(p1) < 8:
                p1 += d[5]

            if d[5].isnumeric():
                n = int(d[5])

                if n < 8 and p2[n] is None:
                    p2[n] = d[6]

        seed += 1

    return p1, "".join(p2)


if __name__ == '__main__':
    data = get_data("05").strip()

    p1, p2 = main(data)
    print(p1)
    print(p2)
