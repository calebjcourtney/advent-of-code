import os
import re
from typing import List, Tuple
import collections

from aocd.models import Puzzle


def get_data(day: str) -> str:
    input_dir = "/".join(os.getcwd().split("/")[:-1])
    try:
        data = open("{}/inputs/input{}.txt".format(input_dir, day), "r").read().strip()
    except FileNotFoundError:
        puzzle = Puzzle(year=2021, day=int(day))
        with open("{}/inputs/input{}.txt".format(input_dir, day), "w+") as saveFile:
            saveFile.write(puzzle.input_data)

        data = open("{}/inputs/input{}.txt".format(input_dir, day), "r").read().strip()

    return data


def get_line_data(day: str):
    data = get_data(day)
    return [x for x in data.split("\n") if x != ""]


def get_int_data(day: str):
    data = get_line_data(day)
    return list(map(int, data))


def re_split(val: str, chars: str) -> list:
    # splits along any of the chars provided in the list
    return re.split("[{}]".format(chars), val)


def special_split(line: str, patterns: List[str]) -> List[str]:
    # splits along any of the patters provided in the list
    return re.split("|".join(patterns), line)


def add_vector(point: Tuple[int], vector: Tuple[int]) -> Tuple[int]:
    return tuple(x + y for x, y in zip(point, vector))


def find_parentheses(line: str) -> List[Tuple[int, int]]:
    # finds matching parentheses in a string and returns the indices
    stack = []
    parentheses_locs = []
    for index, character in enumerate(line):
        if character == '(':
            stack.append(index)
        elif character == ')':
            parentheses_locs.append((stack.pop(), index))

    return parentheses_locs


def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]

    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                try:
                    newval = next(it)   # fetch a new value and
                except StopIteration:
                    return
                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)


def pairwise(iterable, n=2):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable, n)
    next(b, None)
    return zip(a, b)
