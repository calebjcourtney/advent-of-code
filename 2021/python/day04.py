from utils import get_data


class Board:
    def __init__(self, data):
        self.data = []
        for row in data.split("\n"):
            self.data.append(list(map(int, row.split())))

        self.guesses = [[False for _ in range(5)] for _ in range(5)]

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

    def solve(self, sequence):
        for i, number in enumerate(sequence):
            if self.has_number(number) and self.is_bingo():
                return i, number * self.bingo_data()


if __name__ == '__main__':
    data = get_data("04")

    numbers = list(map(int, data.split("\n\n")[0].split(",")))

    boards = []
    for board in data.split("\n\n")[1:]:
        b = Board(board)
        boards.append(b)

    solved_boards = sorted([board.solve(numbers) for board in boards], key = lambda board: board[0])

    p1_result = solved_boards[0][1]
    print(p1_result)

    p2_result = solved_boards[-1][1]
    print(p2_result)
