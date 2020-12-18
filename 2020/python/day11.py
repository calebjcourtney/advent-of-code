from typing import List

from utils import get_line_data


def part_one_adjacents(grid: List[str], row: int, col: int) -> List[str]:
    adj = []
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0:
                continue

            if 0 <= row + x < len(grid) and 0 <= col + y < len(grid[0]):
                adj.append(grid[row + x][col + y])

    return adj


def process_part_one_seats(grid: List[str]) -> List[str]:
    newgrid = []
    for row in range(len(grid)):
        newrow = ''
        for col in range(len(grid[0])):
            adj = part_one_adjacents(grid, row, col)

            if grid[row][col] == 'L' and '#' not in adj:
                newrow += '#'

            elif grid[row][col] == '#' and adj.count('#') >= 4:
                newrow += 'L'

            else:
                newrow += grid[row][col]

        newgrid.append(newrow)

    return newgrid


def part_one(grid: List[str]) -> int:
    while True:
        after = process_part_one_seats(grid)

        if after == grid:
            return ''.join(grid).count('#')

        grid = after


def part_two_adjacents(grid: List[str], row: int, col: int) -> List[str]:
    adj = []
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0:
                continue

            i = 1
            while 0 <= row + i * x < len(grid) and 0 <= col + i * y < len(grid[0]):
                ch = grid[row + i * x][col + i * y]

                if ch != '.':
                    adj.append(ch)
                    break

                i += 1

    return adj


def process_part_two_seats(grid: List[str]) -> List[str]:
    newgrid = []
    for row in range(len(grid)):
        newrow = ''
        for col in range(len(grid[0])):
            adj = part_two_adjacents(grid, row, col)

            if grid[row][col] == 'L' and '#' not in adj:
                newrow += '#'

            elif grid[row][col] == '#' and adj.count('#') >= 5:
                newrow += 'L'

            else:
                newrow += grid[row][col]

        newgrid.append(newrow)

    return newgrid


def part_two(grid: List[str]) -> int:
    while True:
        after = process_part_two_seats(grid)
        if after == grid:
            return ''.join(grid).count('#')

        grid = after


if __name__ == '__main__':
    data = get_line_data("11")

    print(part_one(data))
    print(part_two(data))
