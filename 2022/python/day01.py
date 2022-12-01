data = open("../inputs/input01.txt", "r").read()

elves = data.split("\n\n")

weights = [sum(map(int, elf.split())) for elf in elves]
# part 1
print(max(weights))

# part 2
print(sum(sorted(weights)[-3:]))
