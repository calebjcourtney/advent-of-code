from utils import get_data


def solve(data, depth):
    count = 0
    for count, record in enumerate(data, 1):
        if count >= depth:
            if len(set(data[count - depth:count])) == depth:
                return count


if __name__ == '__main__':
    data = get_data("06")

    p1_result = solve(data, 4)
    print(p1_result)

    p2_result = solve(data, 14)
    print(p2_result)
