from socket import if_nameindex
from utils import get_line_data
from utils import timeit

import re

swap_position = re.compile(r"swap position (\d+) with position (\d+)")
swap_letter = re.compile(r"swap letter (\w+) with letter (\w+)")
rotate_left = re.compile(r"rotate left (\d+) steps?")
rotate_right = re.compile(r"rotate right (\d+) steps?")
rotate_position = re.compile(r"rotate based on position of letter (\w+)")
reverse = re.compile(r"reverse positions (\d+) through (\d+)")
move = re.compile(r"move position (\d+) to position (\d+)")


@timeit
def part_one(code, instructions):
    for instruction in instructions:
        if swap_position.match(instruction):
            pos1, pos2 = swap_position.match(instruction).groups()
            code[pos1], code[pos2] = code[pos2], code[pos1]
        elif swap_letter.match(instruction):
            letter1, letter2 = swap_letter.match(instruction).groups()
            code[code.index(letter1)], code[code.index(letter2)] = code[code.index(letter2)], code[code.index(letter1)]
        elif rotate_left.match(instruction):
            steps = int(rotate_left.match(instruction).groups()[0])
            code = code[steps:] + code[:steps]
        elif rotate_right.match(instruction):
            steps = int(rotate_right.match(instruction).groups()[0])
            code = code[-steps:] + code[:-steps]
        elif rotate_position.match(instruction):
            letter = rotate_position.match(instruction).groups()[0]
            code = code[code.index(letter):] + code[:code.index(letter)]
        elif reverse.match(instruction):
            pos1, pos2 = reverse.match(instruction).groups()
            code = code[:pos1] + code[pos1:pos2+1][::-1] + code[pos2+1:]
        elif move.match(instruction):
            pos1, pos2 = move.match(instruction).groups()
            code = code[:pos1] + code[pos1+1:] + code[pos1] + code[pos2:]

    return code


@timeit
def main():
    code = list("abcdefgh")
    instructions = get_line_data("21")

    p1_result = part_one(code, instructions)
    print(p1_result)


if __name__ == '__main__':
    main()