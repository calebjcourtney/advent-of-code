from utils import get_line_data


data = get_line_data("05")


def parse_line(line):
    row = line[:-3]
    row = row.replace("F", "0").replace("B", "1")

    row = int(row, 2)

    column = line[-3:]
    column = column.replace("L", "0").replace("R", "1")
    column = int(column, 2)

    return (row * 8) + column


seat_ids = [parse_line(x) for x in data]


# part 1
print(max(seat_ids))


# part 2
for x in range(min(seat_ids), max(seat_ids)):
    if x not in seat_ids:
        print(x)
