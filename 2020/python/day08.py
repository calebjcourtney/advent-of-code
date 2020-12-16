from typing import List

from utils import get_line_data


def part_one(data: List[str]) -> int:
    accumulator = 0
    processed = set()
    index = 0

    while True:
        cur = data[index]

        if index in processed:
            break
        else:
            processed.add(index)

        instruction, val = cur.split()

        if instruction == "acc":
            accumulator += int(val)
            index += 1

        elif instruction == "jmp":
            index += int(val)

        else:
            index += 1

    return accumulator


# slight modification to part one
def run_instructions(data: List[str]) -> int:
    accumulator = 0
    processed = set()
    index = 0

    while True:
        # we've reached the last line
        if index == len(data):
            return accumulator

        cur = data[index]

        if index in processed:
            return 0
        else:
            processed.add(index)

        instruction, val = cur.split()

        if instruction == "acc":
            accumulator += int(val)
            index += 1

        elif instruction == "jmp":
            index += int(val)

        else:
            index += 1


def part_two(data) -> int:
    for line in range(len(data)):
        # make a copy
        lines = data[:]

        # swap the data
        if "jmp" in lines[line]:
            lines = lines[:line] + [lines[line].replace("jmp", "nop")] + lines[line + 1:]

        elif "nop" in lines[line]:
            lines = lines[:line] + [lines[line].replace("nop", "jmp")] + lines[line + 1:]

        # skip this iteration, since there won't be a change
        else:
            continue

        val = run_instructions(lines)

        if val:
            return val


if __name__ == '__main__':
    data = get_line_data("08")

    print(part_one(data))
    print(part_two(data))
