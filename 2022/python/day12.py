from utils import get_line_data, Point

from collections import deque


def parse_lines(lines):
    board = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            board[Point(x, y)] = c
            if c == 'S':
                start = Point(x, y)
                board[start] = 'a'  # min height, but still lowercase
            elif c == 'E':
                end = Point(x, y)
                board[end] = 'z'  # max height, but still lowercase

    return board, start, end


def solve(data, start, end):
    queue = deque([(start, 0)])
    seen = set()
    while queue:
        current, depth = queue.popleft()
        if current in seen:
            continue
        elif current == end:
            return depth

        seen.add(current)

        for n in current.neighbors():  # returns the 4 adjacent points
            if n not in board:
                continue
            if (ord(board[n]) - 1 <= ord(board[current])):
                queue.append((n, depth + 1))

    return 1e50


if __name__ == '__main__':
    lines = get_line_data("12")
    board, start, end = parse_lines(lines)

    print(solve(board, start, end))
    print(min(solve(board, s, end) for s in board if board[s] == 'a'))
