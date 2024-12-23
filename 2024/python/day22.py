from collections import deque, defaultdict

from utils import get_int_data, timeit


def run(secret: int) -> int:
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    secret = ((secret * 2048) ^ secret) % 16777216

    return secret


@timeit
def main(data):
    p1 = 0
    changes = defaultdict(int)
    for line in data:
        line_changes = {}
        seq = []
        for _ in range(2000):
            new = run(line)

            if len(seq) < 4:
                seq.append(new % 10 - line % 10)
            else:
                seq = seq[1:] + [new % 10 - line % 10]
                t = tuple(seq)
                if t not in line_changes:
                    line_changes[t] = new % 10

            line = new

        for k, v in line_changes.items():
            changes[k] += v

        p1 += new

    print(p1)
    print(max(changes.values()))


if __name__ == '__main__':
    data = get_int_data("22")
    main(data)
