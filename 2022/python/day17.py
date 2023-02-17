from typing import Set

from utils import get_data, Point


class Rock:
    def __init__(self, points: Set[Point]):
        self.shape = points

    def move_left(self):
        if any([point.x == 0 for point in self.shape]):
            return

        return set([Point(point.x - 1, point.y) for point in self.shape])

    def move_right(self):
        if any([point.x == 6 for point in self.shape]):
            return

        return set([Point(point.x + 1, point.y) for point in self.shape])

    def move_down(self):
        return set([Point(point.x, point.y - 1) for point in self.shape])

    def move_up(self):
        return set([Point(point.x, point.y + 1) for point in self.shape])

    def __and__(self, r: Set[Point]) -> Set[Point]:
        return self.shape & r

    def __or__(self, r: Set[Point]) -> Set[Point]:
        print(r)
        return self.shape | r


def get_rock(t: int, y: int) -> Rock:
    if t == 0:
        return Rock(set(
            [
                Point(2, y),
                Point(3, y),
                Point(4, y),
                Point(5, y),
            ]
        ))
    elif t == 1:
        return Rock(set(
            [
                Point(3, y + 2),
                Point(2, y + 1),
                Point(3, y + 1),
                Point(4, y + 1),
                Point(3, y),
            ]
        ))
    elif t == 2:
        return Rock(set(
            [
                Point(2, y),
                Point(3, y),
                Point(4, y),
                Point(4, y + 1),
                Point(4, y + 2),
            ]
        ))
    elif t == 3:
        return Rock(set(
            [
                Point(2, y),
                Point(2, y + 1),
                Point(2, y + 2),
                Point(2, y + 3),
            ]
        ))
    elif t == 4:
        return Rock(set(
            [
                Point(2, y + 1),
                Point(2, y),
                Point(3, y + 1),
                Point(3, y),
            ]
        ))


def signature(R):
    maxY = max([y for (x, y) in R])
    return frozenset([(x, maxY - y) for (x, y) in R if maxY - y <= 30])


def simulate(data, L):
    rocks = set([Point(x, 0) for x in range(7)])

    SEEN = {}
    top = 0
    i = 0
    t = 0
    added = 0
    while t < L:
        rock = get_rock(t % 5, top + 4)
        while True:
            # pushed -> down
            if data[i] == "<":
                rock.move_left()
                if rock & rocks:
                    rock.move_right()
            else:
                rock.move_right()
                if rock & rocks:
                    rock.move_left()
            i = (i + 1) % len(data)
            rock.move_down()
            if rock & rocks:
                rock.move_up()
                rocks |= rock
                top = max([y for (x, y) in rocks])

                rock_signature = (i, t % 5, signature(rocks))
                if rock_signature in SEEN and t >= 2022:
                    (oldt, oldy) = SEEN[rock_signature]
                    dy = top - oldy
                    dt = t - oldt
                    amt = (L - t) // dt
                    added += amt * dy
                    t += amt * dt
                    assert t <= L

                SEEN[rock_signature] = (t, top)
                break

        t += 1

    return top, added


if __name__ == "__main__":
    data = get_data("17")
    part_1 = simulate(data, 2022)[0]
    print(part_1)
    part_2 = sum(simulate(data, 1000000000000))
    print(part_2)
