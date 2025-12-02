from utils import get_data
from utils import get_nums
from utils import timeit


def process_data(data):
    nums = get_nums(data, signed=False)
    return [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]


def p1_invalid(num):
    num_str = str(num)

    if len(num_str) % 2 != 0:
        return False

    return num_str[:len(num_str)//2] == num_str[len(num_str)//2:]


def p2_invalid(num):
    num_str = str(num)

    for prefix_len in range(1, len(num_str) // 2 + 1):
        prefix = num_str[:prefix_len]

        if len(num_str) % prefix_len == 0:
            repetitions = len(num_str) // prefix_len

            if repetitions >= 2 and prefix * repetitions == num_str:
                return True

    return False


@timeit
def main():
    data = get_data("02")
    data = process_data(data)

    p1 = 0
    p2 = 0
    for low, high in data:
        for num in range(low, high + 1):
            if p1_invalid(num):
                p1 += num
            if p2_invalid(num):
                p2 += num

    print(p1)
    print(p2)
