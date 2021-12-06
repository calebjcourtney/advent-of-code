from utils import get_data


def rotate(fish_count, days):
    for _ in range(days):
        fish_count = [*fish_count[1:], fish_count[0]]
        fish_count[6] += fish_count[-1]

    return sum(fish_count)


if __name__ == '__main__':
    data = get_data("06")
    fish = [data.count(f) for f in "012345678"]

    part_one = rotate(fish, 80)
    print(part_one)

    part_two = rotate(fish, 256)
    print(part_two)
