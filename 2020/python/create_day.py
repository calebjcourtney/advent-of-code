import argparse
import os

parser = argparse.ArgumentParser(description='Create python script for AOC day')
parser.add_argument('day', type=int, help='an integer for the day to be created')

args = parser.parse_args()

day = args.day if len(str(args.day)) == 2 else f"0{args.day}"

python_script = f"""from utils import get_data, get_line_data, get_int_data

import numpy
import itertools
import collections


def part_one(data):
    for line in data:
        pass


def part_two(data):
    for line in data:
        pass


if __name__ == '__main__':
    data = get_data("{day}")
    data = get_line_data("{day}")
    data = get_int_data("{day}")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
"""

# if the file exists, we don't want to accidentally overwrite it
assert not os.path.exists(f"day{day}.py")

with open(f"day{day}.py", "w+") as python_day:
    python_day.write(python_script)
