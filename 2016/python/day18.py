from utils import get_data
from utils import timeit


def is_trap(left, center, right):
    return (
        (left and center and not right) or
        (center and right and not left) or
        (left and not center and not right) or
        (right and not center and not left)
    )


def solve(data, iterations):
    line = [char == "." for char in data]

    safe = sum(line)

    for _ in range(iterations - 1):
        new_line = []
        for i in range(len(line)):
            if i == 0:
                new_line.append(not is_trap(False, not line[i], not line[i+1]))
            elif i == len(line) - 1:
                new_line.append(not is_trap(not line[i-1], not line[i], False))
            else:
                new_line.append(not is_trap(not line[i-1], not line[i], not line[i+1]))

        line = new_line
        safe += sum(line)

    return safe


@timeit
def main():
    data = get_data("18")

    print(solve(data, 40))
    print(solve(data, 400000))
