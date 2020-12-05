from utils import get_line_data


data = get_line_data("05")

# convert to binary string
t = str.maketrans({'B': '1', 'R': '1', 'F': '0', 'L': '0'})
# then int convert to int
seat_ids = [int(line.translate(t), 2) for line in data]


# part 1
print(max(seat_ids))


# part 2
for x in range(min(seat_ids), max(seat_ids)):
    if x not in seat_ids:
        print(x)
