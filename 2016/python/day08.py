from utils import get_line_data
from utils import get_nums
from utils import grid_rotate_column_down
from utils import grid_rotate_row_right
from utils import parse_grid
from utils import Point
from utils import print_grid
from utils import timeit


@timeit
def main(data):
    grid = parse_grid([
        ["." for _ in range(50)]
        for _ in range(6)
    ])
    for line in data:
        if line.startswith("rect"):
            x, y = get_nums(line)
            for iy in range(y):
                for ix in range(x):
                    grid[Point(ix, iy)] = "#"

        elif line.startswith("rotate row"):
            y, count = get_nums(line)
            grid = grid_rotate_row_right(grid, y, count)

        elif line.startswith("rotate column"):
            x, count = get_nums(line)
            grid = grid_rotate_column_down(grid, x, count)

        tmp = x = y = count = None

    print(len([val for val in grid.values() if val == "#"]))

    print_grid(grid)


if __name__ == '__main__':
    data = get_line_data("08")

    main(data)
