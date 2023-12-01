from utils import get_line_data
data = get_line_data(1)


def part_one(lines: list[str]):
    nums = ["".join(x for x in line if x.isdigit()) for line in lines]
    return [int(f"{x[0]}{x[-1]}") for x in nums]


NUMS = "0 zero 1 one 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine".split()


def indexes(line: str) -> list[tuple[str, int]]:
    return [(x, line.index(x)) for x in NUMS if x in line]


def part_two(lines: list[str]):
    answer = 0

    for line in lines:
        idx = indexes(line)
        first = min(idx, key=lambda x: x[1])[0]
        last = max(idx, key=lambda x: x[1])[0]
        answer += int(f"{NUMS.index(first) // 2}{NUMS.index(last) // 2}")

    return answer


if __name__ == '__main__':
    print(sum(part_one(data)))
    print(part_two(data))
