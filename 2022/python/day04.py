from utils import get_line_data


class Section():
    def __init__(self, arg):
        self.start, self.end = map(int, arg.split("-"))
        self.seats = set([x for x in range(self.start, self.end + 1)])


def part_one(data):
    c = 0
    for line in data:
        s1, s2 = map(Section, line.split(","))

        if len(s1.seats & s2.seats) == min(len(s1.seats), len(s2.seats)):
            c += 1

    return c


def part_two(data):
    c = 0
    for line in data:
        s1, s2 = map(Section, line.split(","))
        if s1.seats & s2.seats:
            c += 1

    return c


if __name__ == '__main__':
    data = get_line_data("04")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
