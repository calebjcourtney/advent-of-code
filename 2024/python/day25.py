from utils import get_data, parse_grid


def parse_data(data):
    records = data.split("\n\n")

    keys = []
    locks = []

    for record in records:
        grid = parse_grid(record, keep_values="#")

        if (0, 0) in grid:
            keys.append(set(grid.keys()))
        else:
            locks.append(set(grid.keys()))

    return keys, locks


if __name__ == "__main__":
    data = get_data("25")
    keys, locks = parse_data(data)

    print(sum(1 for key in keys for lock in locks if len(key & lock) == 0))
