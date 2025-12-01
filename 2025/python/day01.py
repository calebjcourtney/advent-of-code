from utils import get_line_data
from utils import timeit
from utils import get_nums


@timeit
def main():
    data = get_line_data("01")

    p1 = 0
    p2 = 0
    pos = 50
    for line in data:
        nums = get_nums(line)[0]
        for _ in range(nums):
            if line.startswith("R"):
                pos += 1
            elif line.startswith("L"):
                pos -= 1

            if pos >= 100:
                pos -= 100
            if pos < 0:
                pos += 100

            if pos == 0:
                p2 += 1

        if pos == 0:
            p1 += 1

    print(p1)
    print(p2)
