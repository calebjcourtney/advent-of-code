from utils import get_data, chunks


class Board:
    def __init__(self, data: str):
        # initialize the data structures
        self.data = list(map(int, data.split()))

    def has_number(self, num: int) -> [bool, None]:
        # finds an input number in the board and sets the guessed list to True
        if num in self.data:
            self.data = [n if n != num else -1 for n in self.data]
            return True

    def is_bingo(self) -> [bool, None]:
        # checks if the board is a bingo (row or column complete)

        # row is complete
        for row in chunks(self.data, 5):
            if sum(row) == -5:
                return True

        # column is complete
        for col_i in range(5):
            if sum([row[col_i] for row in chunks(self.data, 5)]) == -5:
                return True

    def bingo_data(self) -> int:
        # returns the sum of the numbers in the board not already guessed in the sequence
        return sum(num for num in self.data if num != -1)

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
    solved_boards = sorted([board.solve(numbers) for board in boards], key = lambda x: x[0])

    # this is the fastest solution
    p1_result = solved_boards[0][1]
    print(p1_result)

    # this is the slowest solution
    p2_result = solved_boards[-1][1]
    print(p2_result)
