import itertools
data = list(map(int, open("input01.txt").read().split()))

for a, b in itertools.permutations(data, 2):
    if a + b == 2020:
        print(a * b)
        break

for a, b, c in itertools.permutations(data, 3):
    if a + b + c == 2020:
        print(a * b * c)
        break
