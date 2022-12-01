from utils import get_data
data = get_data(1)


def part_one(weights):
    return max(weights)


def part_two(weights):
    return sum(sorted(weights)[-3:])


if __name__ == '__main__':
    elves = data.split("\n\n")
    weights = [sum(map(int, elf.split())) for elf in elves]

    print(part_one(weights))
    print(part_two(weights))
