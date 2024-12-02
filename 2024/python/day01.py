from utils import get_line_data
from utils import get_nums
from utils import timeit


@timeit
def combined(data: tuple[str, str]) -> None:
    lefts = sorted(list(map(int, [x[0] for x in data])))
    rights = sorted(list(map(int, [x[1] for x in data])))

    print("part 1:", sum([abs(x - y) for x, y in zip(lefts, rights)]))
    print("part 2:", sum(l * rights.count(l) for l in lefts))


if __name__ == '__main__':
    data = [get_nums(line) for line in get_line_data("01")]
    combined(data)
