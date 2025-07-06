from utils import get_data
from utils import get_line_data
from utils import get_int_data
from utils import parse_grid
from utils import timeit

BENCHMARK = 272
BENCHMARK_2 = 35651584


def dragon_curve(data):
    a = data
    b = a[::-1]
    b = "".join(["1" if x == "0" else "0" for x in b])
    return a + "0" + b


def checksum(data):
    while len(data) % 2 == 0:
        data = "".join(["1" if x == y else "0" for x, y in zip(data[::2], data[1::2])])
    return data


@timeit
def run(data, benchmark):
    while len(data) < benchmark:
        data = dragon_curve(data)
    
    data = data[:benchmark]

    return checksum(data)


if __name__ == '__main__':
    data = get_data("16")

    p1_result = run(data, BENCHMARK)
    print(p1_result)

    p2_result = run(data, BENCHMARK_2)
    print(p2_result)
