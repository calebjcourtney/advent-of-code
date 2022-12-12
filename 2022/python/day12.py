from utils import get_line_data, parse_grid

from collections import deque, defaultdict


class Grid:
    def __init__(self, lines):
        self.board = parse_grid(lines)
        self.end = [key for key, value in self.board.items() if value == "S"][0]
        self.board[self.end] = "a"

        self.start = [key for key, value in self.board.items() if value == "E"][0]
        self.board[self.start] = "z"

        self.steps = defaultdict(lambda: float('inf'))
        self.compute_shortest_paths(end=self.end)

    def compute_shortest_paths(self, end=None):
        queue = deque([(self.start, 0)])
        while queue:
            current, depth = queue.popleft()
            for n in current.neighbors():
                if n not in self.board:
                    continue

                if n in self.steps:
                    continue

                if (ord(self.board[n]) + 1 >= ord(self.board[current])):
                    self.steps[n] = depth + 1
                    queue.append((n, depth + 1))


if __name__ == '__main__':
    lines = get_line_data("12")
    grid = Grid(lines)

    print(grid.steps[grid.end])
    print(min(grid.steps[point] for point, value in grid.board.items() if value == "a"))
