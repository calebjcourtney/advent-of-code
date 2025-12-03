from utils import get_line_data
from utils import timeit


def highest_possible_joltage(line: str, n: int = 2) -> int:
    digits = list(line[:n])

    for i in range(n, len(line)):
        digits.append(line[i])

        best_number = 0
        best_digits = None

        for j in range(len(digits)):
            candidate = digits[:j] + digits[j+1:]
            number = int("".join(candidate))
            if number > best_number:
                best_number = number
                best_digits = candidate

        digits = best_digits

    return int("".join(digits))


@timeit
def main():
    data = get_line_data("03")

    print(sum(highest_possible_joltage(line) for line in data))
    print(sum(highest_possible_joltage(line, 12) for line in (data)))
