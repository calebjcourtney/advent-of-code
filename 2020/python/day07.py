from typing import Dict, List


def parse_bags(relationships: List[str]) -> Dict[str, List[Dict[str, int]]]:
    bags = {}

    for relationship in relationships:
        parent_bag, children = relationship.split(" contain ")

        parent_bag = " ".join(parent_bag.split()[:-1])

        bags[parent_bag] = []
        if children == "no other bags.":
            bags[parent_bag].append(
                {
                    "count": 0,
                    "color": None
                }
            )
            continue

        children = children.split(", ")

        for child in children:
            child = child.split()

            count = int(child[0])
            color = " ".join(child[1:-1])

            bags[parent_bag].append(
                {
                    "count": count,
                    "color": color
                }
            )

    return bags


def canContain(bag: str, bags: Dict[str, List[Dict[str, int]]]) -> bool:
    if "shiny gold" in [child["color"] for child in bags[bag]]:
        return True

    for nextBag in [child["color"] for child in bags[bag] if child["color"] is not None]:
        if canContain(nextBag, bags):
            return True

    return False


def part_one(bags: List[Dict[str, int]]) -> int:
    total = 0

    for bag in bags.keys():
        if canContain(bag, bags):
            total += 1

    return total


def part_two(bags: List[Dict[str, int]], parent: str) -> int:
    if parent is None:
        return 0
    else:
        parent = bags[parent]

    total = 0
    for child in parent:
        total += child["count"] * (part_two(bags, child["color"]) + 1)

    return total


if __name__ == '__main__':
    data = open("input.txt", "r").read().strip().split("\n")
    bags = parse_bags(data)

    print(part_one(bags))
    print(part_two(bags, "shiny gold"))
