from utils import get_int_data

from aocd import submit


def is_sum_of_two_vals(num, inits):
    for x in inits:
        for y in inits:
            if x == y:
                continue

            if x + y == num:
                return True

    return False


def part_one(int_data):
    inits = set(int_data[:25])
    for num in int_data[25:]:
        if not is_sum_of_two_vals(num, inits):
            return num

        inits.add(num)


def part_two(my_num, int_data):
    end = 3
    while True:
        for start in range(len(int_data)):
            if sum(int_data[start:start + end]) == my_num:
                return min(int_data[start:start + end]) + max(int_data[start:start + end])

        end += 1


if __name__ == '__main__':
    int_data = get_int_data("09")

    # part one
    my_num = part_one(int_data)
    submit(my_num, part = "a", day = 9, year=2020)

    # part two
    contiguous_answer = part_two(my_num, int_data)
    submit(contiguous_answer, part = "b", day = 9, year=2020)
