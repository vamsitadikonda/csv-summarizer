import math
import sys
import re
from src.constants import help_string, the


def coerce(s):
    def fun(s1):
        if s1 == "True":
            return True
        if s1 == "False":
            return False
        return s1

    return int(s) if s.isnumeric() else None or fun(s.split()[0])


def cli():
    args = sys.argv
    for slot, v in the.items():
        v = str(v)
        for i in range(len(args)):
            if args[i] == "-" + slot[0] or args[i] == "--" + slot:
                v = (v == "False" and "True") or (v == "True" and "False") or args[i + 1]
        the[slot] = coerce(v)
        if the['help']:
            exit(print("\n" + help_string + "\n"))
    return the


def push(t, x):
    t[1 + len(t)] = x
    return x


def runs():  # ToDo
    return NotImplementedError


def rogues():  # ToDo
    return NotImplementedError


def init_the():
    def func(v):
        the[v.group(1)] = coerce(v.group(2))

    pattern = re.compile(r"[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)")
    for match in pattern.finditer(help_string):
        # extract words
        func(match)


def csv(fname, fun):  # ToDo
    sep = []
    return NotImplementedError


def rnd(x, places):
    mult = 10 ** (places or 2)
    return math.floor(x * mult + 0.5) / mult


def per(t, p):
    p = math.floor(((p or .5) * len(t)) + .5)
    return t[max(1, min(len(t), p))]
