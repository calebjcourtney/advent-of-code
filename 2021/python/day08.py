from utils import get_line_data

# 0: abcefg (6)
# 6: abdefg (6)
# 9: abcdfg (6)

# 2: acdeg (5)
# 3: acdfg (5)
# 5: abdfg (5)

# 1: cf (2)
# 4: bcdf (4)
# 7: acf (3)
# 8: abcdefg (7)


INT_SETS = {
    0: set("abcefg"),
    1: set("cf"),
    2: set("acdeg"),
    3: set("acdfg"),
    4: set("bcdf"),
    5: set("abdfg"),
    6: set("abdefg"),
    7: set("acf"),
    8: set("abcdefg"),
    9: set("abcdfg"),
}


class CircuitBoard:
    def __init__(self, line):
        self.before = line.split(" | ")[0].split()
        self.outputs = line.split(" | ")[1].split()
        self.all_vals = self.before + self.outputs

        self.char_map = {letter: set("abcdefg") for letter in "abcdefg"}

    def all_chars_solved(self):
        for v in self.char_map.values():
            if len(v) > 1:
                return False

        return True

    def update_letter(self, letter, new_set):
        if len(self.char_map[letter]) > 1:
            self.char_map[letter] = self.char_map[letter] & new_set

    def update_letters(self, letters, new_set):
        for letter in letters:
            self.update_letter(letter, new_set)

    def subtract_letters(self, letters, subtract_set):
        for letter in letters:
            self.char_map[letter] -= subtract_set

    def no_empty_letters(self):
        for k, v in self.char_map.items():
            if len(v) == 0:
                print(self.char_map)
                return False

        return True

    def remove_duplicates(self):
        for _ in range(10):
            for l1 in self.char_map.keys():
                assert self.no_empty_letters()
                if len(self.char_map[l1]) == 1:
                    other_letters = set([l2 for l2 in self.char_map.keys() if l2 != l1])
                    self.subtract_letters(other_letters, self.char_map[l1])

            assert self.no_empty_letters()

    def solve(self):
        for word in self.all_vals:
            word = set(word)
            if len(word) == 2:  # this is a 1
                self.update_letters("cf", word)

        assert len(self.char_map["c"]) == 2, self.char_map["c"]
        assert len(self.char_map["f"]) == 2, self.char_map["f"]
        self.subtract_letters("abdeg", self.char_map["c"])
        assert self.no_empty_letters()

        for word in self.all_vals:
            word = set(word)
            if len(word) == 3:  # this is a 7
                self.update_letters("acf", word)

                if len(self.char_map["c"]) == 2:
                    self.subtract_letters("a", self.char_map["c"])

                if len(self.char_map["a"]) == 1:
                    self.remove_duplicates()

            elif len(word) == 4:  # this is a 4
                self.update_letters("bcdf", word)
                self.subtract_letters("bd", self.char_map["c"])

                assert len(self.char_map["b"]) == 2
                assert len(self.char_map["d"]) == 2

                self.subtract_letters("eg", self.char_map["b"])

        self.remove_duplicates()
        assert len(self.char_map["a"]) == 1
        assert self.no_empty_letters()

        for word in self.all_vals:
            word = set(word)

            if len(word) == 5:
                if len(word & self.char_map["c"]) == 2:  # we know we're dealing with a 3
                    self.update_letters("acdfg", word)

                    assert self.no_empty_letters()

                    # if it's a 3, then we know it has an overlap of the middle (d) value
                    self.char_map["d"] = (word - self.char_map["c"]) & self.char_map["d"]

        self.remove_duplicates()

        # now we need to deduce the vals of c and f
        for word in self.all_vals:
            word = set(word)

            if len(word) == 6 and len(word & self.char_map["c"]) == 1:  # this is a 9 or 0
                self.update_letters("f", word)

        self.remove_duplicates()

        assert self.all_chars_solved()

    def reverse_map(self):
        return {list(v)[0]: k for k, v in self.char_map.items()}

    def map_word(self, word):
        rev_map = self.reverse_map()
        output = set()
        for char in word:
            output |= set(rev_map[char])

        assert len(output) == len(word)

        return output

    def sum_outputs(self):
        out = ""
        for word in self.outputs:
            word = set(word)
            char_set = self.map_word(word)
            for num, chars in INT_SETS.items():
                if len(char_set) == len(chars) and char_set == chars:
                    out += str(num)
                    break

        return out


def part_one(data):
    total = 0
    for line in data:
        outputs = line.split(" | ")[1].split()

        for o in outputs:
            if len(set(o)) in [2, 4, 3, 7]:
                total += 1

    return total


def part_two(data):
    total = 0
    for line in data:
        board = CircuitBoard(line)
        board.solve()

        total += int(board.sum_outputs())

    return total


if __name__ == '__main__':
    data = get_line_data("08")
    print(part_one(data))

    print(part_two(data))
