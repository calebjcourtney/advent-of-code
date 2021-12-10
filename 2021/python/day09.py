from utils import get_line_data


class Board:
    def __init__(self, rows):
        self.rows = [[int(col) for col in cols] for cols in rows]

    def find_lows(self):
        total = 0
        for row_index, row in enumerate(self.rows):
            for col_index, col in enumerate(row):
                if self.is_lower_than_surrounding(row_index, col_index):
                    total = total + 1 + col

        return total

    def is_lower_than_surrounding(self, row_index, col_index):
        points = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for point in points:
            drow = point[0] + row_index
            dcol = point[1] + col_index

            if 0 > drow or drow > len(self.rows):
                continue
            if 0 > dcol or dcol > len(self.rows[0]):
                continue

            try:
                if self.rows[drow][dcol] <= self.rows[row_index][col_index]:
                    return False
            except IndexError:
                continue

        return True

    def get_basin_sizes(self):
        sizes = []
        seen = set()
        points = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for row_index, row in enumerate(self.rows):
            for col_index, col in enumerate(row):
                if (row_index, col_index) in seen or self.rows[row_index][col_index] == 9:
                    continue

                size = 0

                deque = [(row_index, col_index)]
                while deque:
                    r, c = deque.pop(0)
                    if (r, c) in seen:
                        continue

                    seen.add((r, c))

                    size += 1

                    for d in range(len(points)):
                        rr = r + points[d][0]
                        cc = c + points[d][1]

                        if 0 <= rr < len(self.rows) and 0 <= cc < len(self.rows[0]) and self.rows[rr][cc] != 9:
                            deque.append((rr, cc))

                sizes.append(size)

        return sizes


def part_one(data):
    b = Board(data)
    return b.find_lows()


def part_two(data):
    b = Board(data)
    sizes = b.get_basin_sizes()
    sizes.sort()
    return sizes[-3] * sizes[-2] * sizes[-1]


if __name__ == '__main__':
    data = get_line_data("09")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
