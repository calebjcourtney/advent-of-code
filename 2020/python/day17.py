from utils import get_line_data

import itertools

from typing import List, Tuple, Generator, Set


# might add this to utils later
def add_vector(point: Tuple[int], vector: Tuple[int]) -> Tuple[int]:
    return tuple(x + y for x, y in zip(point, vector))


def get_neighbors(point: Tuple[int]) -> Generator:
    dims = len(point)
    zero = tuple(0 for _ in range(dims))

    for vector in itertools.product([-1, 0, 1], repeat=dims):
        if vector != zero:
            yield add_vector(point, vector)


class PocketDimension:
    def __init__(self, active_points):
        self.active_points = set(active_points)

    def get_potential_changes(self) -> Set[Tuple[int]]:
        potential_changes = set()

        for point in self.active_points:
            potential_changes.add(point)

            for neighbor in get_neighbors(point):
                potential_changes.add(neighbor)

        return potential_changes

    def run_cycle(self) -> None:
        new_active_points = set()

        for point in self.get_potential_changes():
            active_neighbors = []
            for neighbor in get_neighbors(point):
                if neighbor in self.active_points:
                    active_neighbors.append(neighbor)

            if point in self.active_points and len(active_neighbors) in [2, 3]:
                new_active_points.add(point)
            elif point not in self.active_points and len(active_neighbors) == 3:
                new_active_points.add(point)

        self.active_points = new_active_points

    def run_process(self) -> None:
        for _ in range(6):
            self.run_cycle()


def create_pocket_dimension(data: List[str], dims: int) -> PocketDimension:
    active_points = set()

    for i, row in enumerate(data):
        for j, status in enumerate(row):
            if status == '#':
                point = (i, j) + tuple(0 for _ in range(dims - 2))
                active_points.add(point)

    return PocketDimension(active_points)


def part_1(data: List[str]) -> int:
    pocket_dimension = create_pocket_dimension(data, 3)
    pocket_dimension.run_process()
    return len(pocket_dimension.active_points)


def part_2(data: List[str]) -> int:
    pocket_dimension = create_pocket_dimension(data, 4)
    pocket_dimension.run_process()
    return len(pocket_dimension.active_points)


if __name__ == '__main__':
    data = get_line_data("17")
    print(part_1(data))
    print(part_2(data))
