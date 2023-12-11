from utils import get_data
from utils import timeit
from utils import parse_grid
from utils import Point
from utils import E, W
from utils import N as S
from utils import S as N
from utils import min_max_xy
from utils import iterate_grid


TARGETS = {
    N: ["S", "|", "7", "F"],
    S: ["S", "|", "J", "L"],
    E: ["S", "-", "J", "7"],
    W: ["S", "-", "L", "F"],
}

NE = E + N
NW = W + N
SE = E + S
SW = W + S

# figured it out by looking at the input data
START = "F"


class PipeMap:
    def __init__(self, data):
        self.grid = parse_grid(data)
        self.start = next(p for p in self.grid if self.grid[p] == "S")
        self.searched = set()

    def get_connected_spots(self, point: Point) -> list[Point]:
        output = set()

        if self.grid[point] == "|":
            if self.grid.get(point + N) in TARGETS[N]:
                output.add(point + N)
            if self.grid.get(point + S) in TARGETS[S]:
                output.add(point + S)
        elif self.grid[point] == "-":
            if self.grid.get(point + E) in TARGETS[E]:
                output.add(point + E)
            if self.grid.get(point + W) in TARGETS[W]:
                output.add(point + W)
        elif self.grid[point] == "L":
            if self.grid.get(point + N) in TARGETS[N]:
                output.add(point + N)
            if self.grid.get(point + E) in TARGETS[E]:
                output.add(point + E)
        elif self.grid[point] == "J":
            if self.grid.get(point + N) in TARGETS[N]:
                output.add(point + N)
            if self.grid.get(point + W) in TARGETS[W]:
                output.add(point + W)
        elif self.grid[point] == "7":
            if self.grid.get(point + S) in TARGETS[S]:
                output.add(point + S)
            if self.grid.get(point + W) in TARGETS[W]:
                output.add(point + W)
        elif self.grid[point] == "F":
            if self.grid.get(point + S) in TARGETS[S]:
                output.add(point + S)
            if self.grid.get(point + E) in TARGETS[E]:
                output.add(point + E)
        elif self.grid[point] == "S":
            if self.grid.get(point + N) in TARGETS[N]:
                output.add(point + N)
            if self.grid.get(point + S) in TARGETS[S]:
                output.add(point + S)
            if self.grid.get(point + E) in TARGETS[E]:
                output.add(point + E)
            if self.grid.get(point + W) in TARGETS[W]:
                output.add(point + W)

        self.searched.add(point)

        return output

    def is_internal(self, point: Point) -> bool:
        min_x, max_x, _, _ = min_max_xy([p for p in self.grid.keys() if point.y == p.y])
        if point.x < min_x or max_x < point.x:
            return False

        # check if the point can get out east
        temp_point = Point(point.x, point.y)
        internal = False
        up = False
        while min_x < temp_point.x < max_x:
            temp_point += E
            if temp_point not in self.grid:
                break
            if self.grid[temp_point] == "|":
                # flip the internal value for every wall
                internal = not internal
            elif self.grid[temp_point] == "-":
                # nothing changes
                pass
            elif self.grid[temp_point] in "LF":
                # change the direction we're facing
                up = self.grid[temp_point] == "L"
            elif self.grid[temp_point] in "J7":
                # flip the internal value for every corner
                if self.grid[temp_point] != ("J" if up else "7"):
                    internal = not internal
                up = False
            elif self.grid[temp_point] == ".":
                pass
            else:
                raise RuntimeError(f"unexpected character (horizontal): {self.grid[temp_point]}")

        return internal

    @timeit
    def combined(self):
        points = {self.start}
        while points != self.searched:
            for point in set(points - self.searched):
                if point in self.searched:
                    continue

                connected = self.get_connected_spots(point)
                points |= connected

        part_one = len(points) // 2

        # made it easier to debug
        self.grid = {point: (value if point in points else ".") for point, value in self.grid.items()}
        self.grid[self.start] = START

        part_two = 0

        for point in iterate_grid(self.grid):
            if self.grid[point] == "." and self.is_internal(point):
                part_two += 1

        return part_one, part_two


if __name__ == '__main__':
    data = get_data("10")

    mapping = PipeMap(data)
    p1, p2 = mapping.combined()

    print(f"Part one: {p1}")
    print(f"Part two: {p2}")
