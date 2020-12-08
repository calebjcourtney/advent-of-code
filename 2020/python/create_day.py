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


data = get_data("{day}")

line_data = get_line_data("{day}")
for line in line_data:
    pass

int_data = get_int_data("{day}")

for num in int_data:
    pass
"""

# if the file exists, we don't want to accidentally overwrite it
assert not os.path.exists(f"day{day}.py")

with open(f"day{day}.py", "w+") as python_day:
    python_day.write(python_script)
