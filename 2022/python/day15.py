from utils import (
    get_line_data,
    get_nums,
    Point,
    manhattan
)

from typing import Tuple, List, Generator


class Sensor:
    def __init__(self, sx: int, sy: int, bx: int, by: int):
        self.center = Point(sx, sy)
        self.radius = manhattan(self.center, Point(bx, by))
        self.distance = self.radius + 1

    def sensor_line(self, xy_range: Tuple[int, int] = None) -> Generator:
        for dx in range(self.radius + 2):
            dy = self.radius + 1 - dx

            for x in [self.center.x + dx, self.center.x + dx]:
                for y in [self.center.y + dy, self.center.y + dy]:
                    if not xy_range[0] <= x <= xy_range[1]:
                        continue

                    if not xy_range[0] <= y <= xy_range[1]:
                        continue

                    yield Point(x, y)

    def contains(self, point):
        return manhattan(point, self.center) <= self.radius

    def x_vals(self, y_val):
        dist_used = abs(self.center.y - y_val)
        dist_left = self.radius - dist_used

        x_min = self.center.x - dist_left
        x_max = self.center.x + dist_left + 1

        return set(range(x_min, x_max))


def parse_data(data):
    sensors = []
    beacons = []
    for line in data:
        sx, sy, bx, by = get_nums(line)
        sensors.append(Sensor(sx, sy, bx, by))
        beacons.append(Point(bx, by))

    return sensors, beacons


def part_one(data, check_y=2000000):
    sensors, beacons = parse_data(data)
    beacons = {beacon.x for beacon in beacons if beacon.y == check_y}
    x_vals = set()

    for line in data:
        sx, sy, bx, by = get_nums(line)
        sensor = Sensor(sx, sy, bx, by)

        x_vals |= sensor.x_vals(check_y)

    return len(x_vals - beacons)


def sensor_covers(sensors: List[Sensor], point: Point) -> bool:
    for sensor in sensors:
        if sensor.contains(point):
            return True

    return False


def part_two(data, xy_range=(0, 4000000)):
    sensors, _ = parse_data(data)
    for sensor in sensors:
        print(" " * 100, end="\r")
        print(f"processing for sensor: {sensor.center}", end="\r")
        for point in sensor.sensor_line(xy_range):
            if not sensor_covers(sensors, point):
                print()
                return point.x * 4000000 + point.y


if __name__ == '__main__':
    data = get_line_data("15")

    print(part_one(data))
    print(part_two(data))
