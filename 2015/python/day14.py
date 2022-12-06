from utils import get_line_data

from collections import defaultdict
import re


class Reindeer:
    def __init__(self, arg):
        self.name = arg["name"]
        self.speed = arg["speed"]
        self.time = arg["time"]
        self.rest = arg["rest"]

        self.time_left = self.time
        self.rest_left = self.rest

    def distance_traveled(self, seconds):
        distance = 0
        while seconds > 0:
            travel_time = min(seconds, self.time)
            distance += travel_time * self.speed
            seconds -= travel_time
            seconds -= self.rest

        return distance

    def second(self):
        # flying
        if self.time_left > 0:
            self.time_left -= 1
            return self.speed

        # resting
        self.rest_left -= 1
        # reset for next second
        if self.rest_left == 0:
            self.rest_left = self.rest
            self.time_left = self.time

        return 0


def parse_line(line: str) -> Reindeer:
    p = re.match(
        r"(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<time>\d+) seconds, but then must rest for (?P<rest>\d+) seconds.",
        line
    )

    data = {key: value if not value.isnumeric() else int(value) for key, value in p.groupdict().items()}
    return Reindeer(data)


def part_one(data):
    total_seconds = 2503
    distances = []
    for reindeer in data:
        distances.append(reindeer.distance_traveled(total_seconds))

    return max(distances)


def part_two(data):
    scores = defaultdict(int)
    distances = defaultdict(int)
    for second in range(2503):
        for reindeer in data:
            temp = reindeer.second()
            distances[reindeer.name] += temp

        best_deer = [key for key, value in distances.items() if value == max(distances.values())]
        for name in best_deer:
            scores[name] += 1

    return max(scores.values())


if __name__ == '__main__':
    data = get_line_data("14")
    data = [parse_line(line) for line in data]

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
