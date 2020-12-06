from utils import get_data

# part 1
data = get_data("06")
data = data.split("\n\n")
data = [rec.replace("\n", "") for rec in data]

total = 0
for rec in data:
    pos = set(x for x in rec)

    total += len(pos)

print(total)


# part 2
data = get_data("06")
data = data.split("\n\n")

total = 0
for record in data:
    cur = None
    for passenger in record.split("\n"):
        temp = set(x for x in passenger)

        if cur is None:
            cur = temp
        else:
            cur = cur & temp

    total += len(cur)

print(total)
