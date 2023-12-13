from utils import get_data
from utils import timeit


@timeit
def combined(patterns: list[str]) -> int:
    part_one = 0
    part_two = 0
    for pattern in patterns:
        row_len = len(pattern)
        col_len = len(pattern[0])

        # Vertical symmetry
        for col in range(col_len - 1):
            smudges = 0

            for col_diff in range(col_len):
                left = col - col_diff
                right = col + 1 + col_diff

                if not (-1 < left < right < col_len):
                    continue

                for row in range(row_len):
                    if pattern[row][left] != pattern[row][right]:
                        smudges += 1

            if smudges == 0:
                part_one += col + 1
            elif smudges == 1:
                part_two += col + 1

        # Horizontal symmetry
        for row in range(row_len - 1):
            smudges = 0

            for row_diff in range(row_len):
                top = row - row_diff
                bottom = row + 1 + row_diff

                if not (-1 < top < bottom < row_len):
                    continue

                for col in range(col_len):
                    if pattern[top][col] != pattern[bottom][col]:
                        smudges += 1

            if smudges == 0:
                part_one += 100 * (row + 1)
            elif smudges == 1:
                part_two += 100 * (row + 1)

    return part_one, part_two


if __name__ == "__main__":
    patterns = get_data("13").split("\n\n")
    patterns = [list(map(list, pattern.split("\n"))) for pattern in patterns]

    p1, p2 = combined(patterns)

    print("part 1:", p1)
    print("part 2:", p2)
