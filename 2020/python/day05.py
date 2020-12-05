from utils import get_line_data


data = get_line_data("05")


seat_ids = [int(line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2) for line in data]


# part 1
print(max(seat_ids))


# part 2
for x in range(min(seat_ids), max(seat_ids)):
    if x not in seat_ids:
        print(x)
