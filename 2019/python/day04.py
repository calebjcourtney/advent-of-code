def has_adjacents(num):
    for x in range(len(num) - 1):
        if num[x] == num[x + 1]:
            return True

    return False


def is_increasing(num):
    return num == "".join(sorted(num))


# part 1
total = 0
for num in range(264793, 803936):
    num = str(num)
    if is_increasing(num) and has_adjacents(num):
        total += 1

print(total)


def has_two(num):
    for x in num:
        if num.count(x) == 2:
            return True

    return False


# part 2
total = 0
for num in range(264793, 803936):
    num = str(num)

    if is_increasing(num) and has_adjacents(num) and has_two(num):
        total += 1

print(total)
