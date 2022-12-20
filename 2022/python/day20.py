from collections import deque

from utils import get_int_data


class Num:
    def __init__(self, index, value):
        self.index = index
        self.value = value


def solve(data, n_times):
    for t in range(n_times):
        for i in range(len(data)):
            # rotate the number
            rotations = [num.index for num in data].index(i)
            data.rotate(-rotations)

            num = data.popleft()

            # number of rotations left to do
            rotations = num.value % len(data)
            data.rotate(-rotations)

            data.append(num)

    zero_index = [num.value for num in data].index(0)

    return (
        data[(zero_index + 1000) % len(data)].value
        + data[(zero_index + 2000) % len(data)].value
        + data[(zero_index + 3000) % len(data)].value
    )


if __name__ == "__main__":
    data = get_int_data("20")

    pattern = deque([Num(i, x) for i, x in enumerate(data)])
    print(solve(pattern, 1))

    pattern = deque([Num(i, x * 811589153) for i, x in enumerate(data)])
    print(solve(pattern, 10))
