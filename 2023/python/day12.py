from utils import get_line_data
from utils import timeit


class Solver:
    def __init__(self, springs, pattern):
        self.springs = springs
        self.pattern = pattern
        self.saved_patterns = {}

    def solve(self, spring_index, pattern_index, cur_len):
        """
        spring_index (int): Current position within springs.
        pattern_index (int): Current position within pattern.
        cur_len (int): Length of the current block of '#'.
        """
        # Check if the result for the current state is already computed
        key = (spring_index, pattern_index, cur_len)
        if key in self.saved_patterns:
            return self.saved_patterns[key]

        # Reached the end of springs
        if spring_index == len(self.springs):
            # Check if the pattern is fully matched
            if pattern_index == len(self.pattern) and cur_len == 0:
                return 1
            elif (
                pattern_index == len(self.pattern) - 1
                and self.pattern[pattern_index] == cur_len
            ):
                return 1
            else:
                return 0

        answer = 0
        for char in [".", "#"]:
            # Check if the cur_len character in springs matches the cur_len choice in pattern
            if self.springs[spring_index] == char or self.springs[spring_index] == "?":
                if char == "." and cur_len == 0:
                    answer += self.solve(spring_index + 1, pattern_index, 0)
                elif (
                    char == "."
                    and cur_len > 0
                    and pattern_index < len(self.pattern)
                    and self.pattern[pattern_index] == cur_len
                ):
                    answer += self.solve(spring_index + 1, pattern_index + 1, 0)
                elif char == "#":
                    answer += self.solve(spring_index + 1, pattern_index, cur_len + 1)

        # Save the result
        self.saved_patterns[key] = answer
        return answer


@timeit
def combined(data, part_one=True):
    ans = 0
    for line in data:
        springs, pattern = line.split()

        if not part_one:
            springs = "?".join([springs] * 5)
            pattern = ",".join([pattern] * 5)

        pattern = list(map(int, pattern.split(",")))
        solver = Solver(springs, pattern)
        score = solver.solve(0, 0, 0)
        ans += score

    return ans


if __name__ == "__main__":
    data = get_line_data("12")

    p1_result = combined(data)
    print(p1_result)

    p2_result = combined(data, False)
    print(p2_result)
