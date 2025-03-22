from utils import get_data
from utils import get_nums


def get_column_seed_value(columns):
    total = 1
    for x in range(2, columns + 1):
        total += x

    return total


def get_num_order(rows, columns):
    val = get_column_seed_value(columns)
    inc = columns
    for _ in range(rows - 1):
        val += inc
        inc += 1

    return val


def main(rows, columns):
    iterations = get_num_order(rows, columns)

    val = 20151125
    for x in range(iterations - 1):
        val *= 252533
        val = val % 33554393

    return val


if __name__ == '__main__':
    data = get_data("25")
    rows, columns = get_nums(data)

    p1_result = main(rows, columns)
    print(p1_result)
