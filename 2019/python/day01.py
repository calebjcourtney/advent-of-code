from utils import get_int_data

data = get_int_data("01")

# part 1
total = 0
for val in data:
    total += (val // 3) - 2

print(total)


# part 2
total = 0
for val in data:
    while val > 0:
        val = (val // 3) - 2

        if val > 0:
            total += val

print(total)
