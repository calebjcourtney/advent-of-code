from utils import get_line_data

inputList = get_line_data("07")

# this took me the longest time to put together
bags = {}
for line in inputList:
    line = line.split(" contain ")

    parent_bag = " ".join(line[0].split()[:-1])
    contains = line[1].split(", ")

    # this was annoying
    if contains == ["no other bags."]:
        contains = []
        nums = []

    else:
        nums = [int(x.split()[0]) for x in contains]
        contains = [" ".join(x.split()[1:-1]) for x in contains]

    bags[parent_bag] = []

    for x in range(len(nums)):
        bags[parent_bag].append({"count": nums[x], "color": contains[x]})


# part 1
def canContain(bag):
    if "shiny gold" in [content["color"] for content in bags[bag]]:
        return True

    for nextBag in [content["color"] for content in bags[bag]]:
        # yay recursion
        if canContain(nextBag):
            return True

    return False


totalNum = 0
for bag in bags.keys():
    if canContain(bag):
        totalNum += 1

print(f"part one answer: {totalNum}")


# part 2
def numContained(bag):
    contained = bags[bag]
    total = 0
    for sub_bag in contained:
        # why is there more recursion
        total += sub_bag["count"] * (numContained(sub_bag["color"]) + 1)

    return total


print(f"part two answer: {numContained('shiny gold')}")
