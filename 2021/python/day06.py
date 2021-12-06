from utils import get_data, array_left_rotate


def solve(fish_count, days):
    for _ in range(days):
        fish_count = array_left_rotate(fish_count)
        fish_count[6] += fish_count[-1]

    return sum(fish_count)


if __name__ == '__main__':
    data = get_data("06")
    fish = [data.count(f) for f in "012345678"]

    part_one = solve(fish, 80)
    print(part_one)

    part_two = solve(fish, 256)
    print(part_two)
