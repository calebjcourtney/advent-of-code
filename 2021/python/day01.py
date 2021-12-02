from utils import get_int_data


if __name__ == '__main__':
    data = get_int_data("01")

    print(sum(x < y for x, y in zip(data, data[1:])))
    print(sum(x < y for x, y in zip(data, data[3:])))
