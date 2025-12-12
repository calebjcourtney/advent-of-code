from utils import get_data
from utils import timeit
from utils import Point as Cell

from typing import Set, Tuple, List, Optional
import re


class Shape:
    def __init__(self, index: int, grid: List[str]):
        self.index = index
        self.grid = grid
        self._area = None
        self._orientations = None
        self._orientation_cells = None

    @property
    def area(self) -> int:
        if self._area is None:
            self._area = sum(row.count('#') for row in self.grid)

        return self._area

    def get_all_orientations(self) -> List[List[str]]:
        if self._orientations is not None:
            return self._orientations

        orientations = []
        seen = set()
        variants = [self.grid, flip_horizontal(self.grid)]

        for variant in variants:
            current = variant
            for _ in range(4):
                grid_str = '\n'.join(current)
                if grid_str not in seen:
                    seen.add(grid_str)
                    orientations.append(current)
                current = rotate_90(current)

        self._orientations = orientations

        return orientations

    def get_orientation_cells(self, orientation: List[str]) -> Set[Cell]:
        cells = set()
        for y, row in enumerate(orientation):
            for x, char in enumerate(row):
                if char == '#':
                    cells.add(Cell(x, y))

        if cells:
            min_x = min(cell.x for cell in cells)
            min_y = min(cell.y for cell in cells)
            normalized = {Cell(cell.x - min_x, cell.y - min_y) for cell in cells}
            return normalized

        return cells

    def get_all_orientation_cells(self) -> List[Set[Cell]]:
        if self._orientation_cells is not None:
            return self._orientation_cells

        orientations = self.get_all_orientations()
        self._orientation_cells = [self.get_orientation_cells(orient) for orient in orientations]

        return self._orientation_cells


class Region:
    def __init__(self, width: int, height: int, quantities: List[int]):
        self.width = width
        self.height = height
        self.quantities = quantities

    @property
    def total_area(self) -> int:
        return self.width * self.height

    def get_required_presents(self) -> List[Tuple[int, int]]:
        required = []
        for shape_idx, quantity in enumerate(self.quantities):
            if quantity > 0:
                required.append((shape_idx, quantity))

        return required


def parse(data: str) -> Tuple[dict, List[Region]]:
    lines = data.split("\n")
    shapes = {}
    regions = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if re.match(r"^\d+:$", line):
            shape_index = int(line[:-1])
            shape_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^\d+:$", lines[i].strip()) and not re.match(r"^\d+x\d+:", lines[i].strip()):
                shape_lines.append(lines[i].strip())
                i += 1
            shapes[shape_index] = Shape(index=shape_index, grid=shape_lines)
        elif re.match(r"^\d+x\d+:", line):
            match = re.match(r"^(\d+)x(\d+):\s*(.+)$", line)
            if match:
                width = int(match.group(1))
                height = int(match.group(2))
                quantities = [int(x) for x in match.group(3).split()]
                regions.append(Region(width=width, height=height, quantities=quantities))
            i += 1
        else:
            i += 1

    return shapes, regions


def rotate_90(grid: List[str]) -> List[str]:
    if not grid:
        return []
    rows = len(grid)
    cols = len(grid[0])
    rotated = []
    for c in range(cols):
        row = ''.join(grid[r][c] for r in range(rows - 1, -1, -1))
        rotated.append(row)
    return rotated


def flip_horizontal(grid: List[str]) -> List[str]:
    return [row[::-1] for row in grid]


class FittingSolver:
    def __init__(self, shapes: dict, region: Region):
        self.shapes = shapes
        self.region = region
        self.occupied_grid = [[False] * region.width for _ in range(region.height)]
        self.shape_cell_sets = {}
        self._precompute_orientations()

    def _precompute_orientations(self):
        for shape_idx, shape in self.shapes.items():
            self.shape_cell_sets[shape_idx] = shape.get_all_orientation_cells()

    def can_place_at(self, orientation_cells: Set[Cell], x: int, y: int) -> bool:
        for cell in orientation_cells:
            new_x = cell.x + x
            new_y = cell.y + y

            if new_x < 0 or new_x >= self.region.width or new_y < 0 or new_y >= self.region.height:
                return False

            if self.occupied_grid[new_y][new_x]:
                return False

        return True

    def place_at(self, orientation_cells: Set[Cell], x: int, y: int):
        for cell in orientation_cells:
            self.occupied_grid[cell.y + y][cell.x + x] = True

    def remove_at(self, orientation_cells: Set[Cell], x: int, y: int):
        for cell in orientation_cells:
            self.occupied_grid[cell.y + y][cell.x + x] = False

    def get_leftmost_topmost(self) -> Optional[Cell]:
        for y in range(self.region.height):
            for x in range(self.region.width):
                if not self.occupied_grid[y][x]:
                    return Cell(x, y)

    def can_fit_presents(self, required_presents: List[Tuple[int, int]]) -> bool:
        total_area = 0
        for shape_idx, count in required_presents:
            shape = self.shapes[shape_idx]
            total_area += shape.area * count

        if total_area > self.region.total_area:
            return False

        presents_to_place = []
        for shape_idx, count in required_presents:
            presents_to_place.extend([shape_idx] * count)

        if not presents_to_place:
            return True

        def get_shape_size(shape_idx):
            return len(self.shape_cell_sets[shape_idx][0]) if self.shape_cell_sets[shape_idx] else 0

        presents_to_place.sort(key=get_shape_size, reverse=True)

        self.occupied_grid = [[False] * self.region.width for _ in range(self.region.height)]

        return self._backtrack(presents_to_place, 0)

    def _backtrack(self, presents_to_place: List[int], present_idx: int) -> bool:
        if present_idx >= len(presents_to_place):
            return True

        position = self.get_leftmost_topmost()
        if position is None:
            return False

        min_x, min_y = position.x, position.y
        shape_idx = presents_to_place[present_idx]
        orientations = self.shape_cell_sets[shape_idx]

        for orientation_cells in orientations:
            if not orientation_cells:
                continue

            max_x = max(cell.x for cell in orientation_cells)
            max_y = max(cell.y for cell in orientation_cells)

            if max_x >= self.region.width or max_y >= self.region.height:
                continue

            for y in range(min_y, self.region.height - max_y):
                x_start = min_x if y == min_y else 0
                for x in range(x_start, self.region.width - max_x):
                    if not self.can_place_at(orientation_cells, x, y):
                        continue

                    self.place_at(orientation_cells, x, y)

                    if self._backtrack(presents_to_place, present_idx + 1):
                        return True

                    self.remove_at(orientation_cells, x, y)

        return False


@timeit
def main():
    data = get_data("12")
    shapes, regions = parse(data)

    count = 0
    for region in regions:
        required_presents = region.get_required_presents()
        solver = FittingSolver(shapes, region)
        if solver.can_fit_presents(required_presents):
            count += 1

    print(count)
