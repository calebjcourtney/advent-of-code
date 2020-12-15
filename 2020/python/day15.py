data = "14,3,1,0,9,5"
data = list(map(int, data.split(',')))

p1, p2 = 0, 0

last = {v: i for i, v in enumerate(data, 1)}
prev = data[-1]
times = 30000000
for i in range(len(data) + 1, times + 1):
    new = i - 1 - last[prev] if prev in last else 0
    last[prev] = i - 1
    prev = new

    if i == 2020:
        p1 = prev

p2 = prev

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
