import os
import re


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
    return re.split("[{}]".format(chars), val)
