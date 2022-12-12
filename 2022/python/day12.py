from utils import get_line_data, Point

from collections import deque


class Grid:
    def __init__(self, lines):
        self.board = {}
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                if c == 'S':
                    self.end = Point(x, y)
                    self.board[self.end] = 'a'
                elif c == 'E':
                    self.start = Point(x, y)
                    self.board[self.start] = 'z'
                else:
                    self.board[Point(x, y)] = c

        self.steps = {}
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

        for point in self.board.keys():
            if point not in self.steps:
                self.steps[point] = float('inf')


if __name__ == '__main__':
    lines = get_line_data("12")
    grid = Grid(lines)

    print(grid.steps[grid.end])
    print(min(grid.steps[point] for point, value in grid.board.items() if value == "a"))
