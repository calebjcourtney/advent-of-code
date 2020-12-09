from utils import get_int_data


def is_sum_of_two_vals(num, inits):
    for x in inits:
        if num - x in inits:
            return True

    return False


def part_one(int_data):
    inits = int_data[:25]
    for num in int_data[25:]:
        if not is_sum_of_two_vals(num, inits):
            return num

        inits.append(num)
        inits = inits[1:]


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
    print(my_num)

    # part two
    contiguous_answer = part_two(my_num, int_data)
    print(contiguous_answer)
