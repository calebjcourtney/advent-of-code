from utils import (
    get_line_data,
    get_nums,
    chunks,
    Point
)


# inverted because +y is "down"
DOWN = Point(0, 1)
DOWN_LEFT = Point(1, 1)
DOWN_RIGHT = Point(-1, 1)


def parse_data(data):
    corners = []
    for line in data:
        nums = get_nums(line)
        corner = []
        for x, y in chunks(nums, 2):
            corner.append(Point(x, y))

        corners.append(corner)

    # Rock locations
    board = {}
    for corner in corners:
        for last, nxt in zip(corner, corner[1:]):
            if last.x == nxt.x:
                for y in range(min(last.y, nxt.y), max(last.y, nxt.y) + 1):
                    board[Point(last.x, y)] = "#"
            else:
                for x in range(min(last.x, nxt.x), max(last.x, nxt.x) + 1):
                    board[Point(x, last.y)] = "#"

    return board


def run(board, floor=1e10):
    source = [point for point, value in board.items() if value == "+"][0]
    sand = source
    while sand.y < 1000:
        if board.get(sand + DOWN, ' ') not in ("#", "o") and sand.y + 1 < floor:
            sand += DOWN

        elif board.get(sand + DOWN_RIGHT, ' ') not in ("#", "o") and sand.y + 1 < floor:
            sand += DOWN_RIGHT

        elif board.get(sand + DOWN_LEFT, ' ') not in ("#", "o") and sand.y + 1 < floor:
            sand += DOWN_LEFT

        elif sand == source:
            board[sand] = "o"
            return board

        else:
            board[sand] = "o"
            sand = source

    return board


def comb(data):
    board = parse_data(data)
    max_y = max(point.y for point in board.keys())

    source = Point(500, 0)
    board[source] = "+"
    board = run(board)
    part_one = sum(1 for v in board.values() if v == "o")

    board[source] = "+"
    board = run(board, floor=max_y + 2)
    part_two = sum(1 for v in board.values() if v == "o")

    return part_one, part_two


if __name__ == '__main__':
    data = get_line_data("14")

    p1, p2 = comb(data)

    print(p1)
    print(p2)
