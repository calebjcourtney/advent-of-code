from utils import get_line_data


def extrapolate_vals(nums: list[int]):
    diff_vals = [nums]
    while sum(diff_vals[-1]) != 0:
        diff_vals.append([y - x for x, y in zip(diff_vals[-1], diff_vals[-1][1:])])

    return sum(row[-1] for row in diff_vals)


if __name__ == '__main__':
    data = get_line_data("09")
    data = [list(map(int, line.split())) for line in data]

    print(sum(extrapolate_vals(row) for row in data))
    print(sum(extrapolate_vals(row[::-1]) for row in data))
