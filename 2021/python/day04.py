from utils import get_data


class Board:
    def __init__(self, arg):
        self.arg = arg

        self.data = []
        for row in arg.split("\n"):
            self.data.append(list(map(int, row.split())))

        self.guesses = [[False for _ in range(len(self.data[0]))] for _ in range(len(self.data))]

    def has_number(self, num):
        for x, row in enumerate(self.data):
            for y, column in enumerate(row):
                if num == column:
                    self.guesses[x][y] = True
                    return True

    def is_bingo(self):
        for row in self.guesses:
            if all(row):
                return True

        for col_i in range(len(self.guesses)):
            if all([row[col_i] for row in self.guesses]):
                return True

        return False

    def bingo_data(self):
        c = 0
        for x, row in enumerate(self.guesses):
            for y, column in enumerate(row):
                if not column:
                    c += self.data[x][y]

        return c


def part_one(boards, instructions):
    guessed_numbers = set()
    for number in instructions:
        guessed_numbers.add(number)
        for board in boards:
            if board.has_number(number) and board.is_bingo():

                nums = board.bingo_data()

                return nums * number


def part_two(boards, instructions):
    i = 0

    # solve all the boards but the last one
    while len(boards) > 1:
        drop_boards = []
        for bi, board in enumerate(boards):
            if board.has_number(instructions[i]) and board.is_bingo():
                drop_boards.append(bi)

        boards = [board for c, board in enumerate(boards) if c not in drop_boards]

        i += 1

    # solve the last board.
    board = boards[0]

    for c in range(i, len(instructions)):
        if board.has_number(instructions[c]) and board.is_bingo():
            sums = board.bingo_data()

            return sums * instructions[c]


if __name__ == '__main__':
    data = get_data("04")

    numbers = list(map(int, data.split("\n\n")[0].split(",")))

    boards = []
    for board in data.split("\n\n")[1:]:
        b = Board(board)
        boards.append(b)

    p1_result = part_one(boards, numbers)
    print(p1_result)

    p2_result = part_two(boards, numbers)
    print(p2_result)
