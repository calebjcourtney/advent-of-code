from utils import get_data


def solve(data, limit):
    last = {v: i for i, v in enumerate(data, 1)}
    prev = data[-1]
    for i in range(len(data) + 1, limit + 1):
        new = i - 1 - last[prev] if prev in last else 0
        last[prev] = i - 1
        prev = new

    return prev


if __name__ == '__main__':
    data = get_data("15")
    data = list(map(int, data.split(',')))

    print(solve(data, 2020))
    print(solve(data, 30000000))
