from itertools import combinations

from utils import Point, get_line_data, get_nums, timeit


class Grid:
    def __init__(self, data: list[str]):
        self.points_set = {Point(get_nums(line)[0], get_nums(line)[1]) for line in data}
        self.points_ordered = [Point(get_nums(line)[0], get_nums(line)[1]) for line in data]
        self._vertical_lines = None
        self._horizontal_lines = None

    @staticmethod
    def _area_between_points(p1: Point, p2: Point) -> int:
        return (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)

    def _build_line_segments(self):
        if self._vertical_lines is not None:
            return

        self._vertical_lines = []
        self._horizontal_lines = []
        prev_point = self.points_ordered[-1]

        for point in self.points_ordered:
            if prev_point.x == point.x:
                # Vertical
                y1, y2 = prev_point.y, point.y
                self._vertical_lines.append((point.x, (y1, y2) if y1 < y2 else (y2, y1)))
            elif prev_point.y == point.y:
                # Horizontal
                x1, x2 = prev_point.x, point.x
                self._horizontal_lines.append(((x1, x2) if x1 < x2 else (x2, x1), point.y))
            prev_point = point

    def _check_lines_cross_rectangle(self, x_min: int, x_max: int, y_min: int, y_max: int) -> bool:
        # Check vertical
        for line_x, (line_y_start, line_y_end) in self._vertical_lines:
            if x_min < line_x < x_max:
                if line_y_start <= y_min < line_y_end or line_y_start < y_max <= line_y_end:
                    return False

        # Check horizontal
        for (line_x_start, line_x_end), line_y in self._horizontal_lines:
            if y_min < line_y < y_max:
                if line_x_start <= x_min < line_x_end or line_x_start < x_max <= line_x_end:
                    return False

        return True

    @timeit
    def part_one(self) -> int:
        return max(self._area_between_points(p1, p2) for p1, p2 in combinations(self.points_set, 2))

    @timeit
    def part_two(self) -> int:
        self._build_line_segments()

        n = len(self.points_ordered)
        areas_and_pairs = [
            (self._area_between_points(self.points_ordered[i], self.points_ordered[j]), i, j)
            for i in range(n)
            for j in range(i + 1, n)
        ]
        areas_and_pairs.sort(reverse=True, key=lambda x: x[0])

        for area, i, j in areas_and_pairs:
            p1, p2 = self.points_ordered[i], self.points_ordered[j]
            x_min, x_max = (p1.x, p2.x) if p1.x < p2.x else (p2.x, p1.x)
            y_min, y_max = (p1.y, p2.y) if p1.y < p2.y else (p2.y, p1.y)

            if self._check_lines_cross_rectangle(x_min, x_max, y_min, y_max):
                return area


@timeit
def main():
    data = get_line_data("09")
    grid = Grid(data)
    print(grid.part_one())
    print(grid.part_two())


if __name__ == '__main__':
    main()
