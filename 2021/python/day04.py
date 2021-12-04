from utils import get_data


class Board:
    def __init__(self, data: str):
        # initialize the data structures
        # data are the numbers in the board
        # guesses are the numbers already guessed on the board

        self.data = []
        for row in data.split("\n"):
            self.data.append(list(map(int, row.split())))

        self.guesses = [[False for _ in range(5)] for _ in range(5)]

    def has_number(self, num: int) -> [bool, None]:
        # finds an input number in the board and sets the guessed list to True
        for x, row in enumerate(self.data):
            for y, column in enumerate(row):
                if num == column:
                    self.guesses[x][y] = True
                    return True

    def is_bingo(self) -> [bool, None]:
        # checks if the board is a bingo (row or column complete)

        # row is complete
        for row in self.guesses:
            if all(row):
                return True

        # column is complete
        for col_i in range(len(self.guesses)):
            if all([row[col_i] for row in self.guesses]):
                return True

    def bingo_data(self) -> int:
        # returns the sum of the numbers in the board not already guessed in the sequence
        c = 0
        for x, row in enumerate(self.guesses):
            for y, column in enumerate(row):
                if not column:
                    c += self.data[x][y]

        return c

    def solve(self, sequence) -> int:
        for i, number in enumerate(sequence):
            if self.has_number(number) and self.is_bingo():
                return i, number * self.bingo_data()


if __name__ == '__main__':
    data = get_data("04")

    # break out the inputs - nums vs boards
    numbers = list(map(int, data.split("\n\n")[0].split(",")))
    boards = [Board(board) for board in data.split("\n\n")[1:]]

    # solve every board and sort by the number of iterations it takes for it to be solved
    solved_boards = sorted([board.solve(numbers) for board in boards], key = lambda board: board[0])

    # this is the fastest solution
    p1_result = solved_boards[0][1]
    print(p1_result)

    # this is the slowest solution
    p2_result = solved_boards[-1][1]
    print(p2_result)
