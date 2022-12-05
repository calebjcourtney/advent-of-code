import os
import re
from typing import List, Tuple
from more_itertools import windowed


def get_data(day: str) -> str:
    input_dir = "/".join(os.getcwd().split("/")[:-1])
    data = open("{}/inputs/input{}.txt".format(input_dir, day), "r").read()

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


def find_corresponding_chars(line: str, start: str, end: str) -> List[Tuple[int, int]]:
    # finds matching figures in a string and returns the indices
    stack = []
    parentheses_locs = []
    for index, character in enumerate(line):
        if character == start:
            stack.append(index)
        elif character == end:
            parentheses_locs.append((stack.pop(), index))

    return parentheses_locs


def find_parentheses(line: str) -> List[Tuple[int, int]]:
    return find_corresponding_chars(line, "(", ")")


def nwise(iterable, n=2):
    return windowed(iterable, n)


# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def array_left_rotate(lst, n=1):
    return lst[n:] + lst[:n]


def array_right_rotate(lst, n=1):
    return lst[-n:] + lst[:-n]
