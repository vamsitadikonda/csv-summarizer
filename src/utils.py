import math
import sys
import re
from src.constants import help_string, the


def checknum(s):
    """
    Function to check if s can be converted to float
    :param s:
    :return: Boolean
    """
    try:
        float(s)
        return True
    except:
        return False


def coerce(s):
    def fun(s1):
        if s1 == "True":
            return True
        if s1 == "False":
            return False
        return s1

    return float(s) if checknum(s) else None or fun(s.split()[0])


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


def rogues():  # ToDo
    return NotImplementedError


def init_the():
    def func(v):
        the[v.group(1)] = coerce(v.group(2))

    pattern = re.compile(r"[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)")
    for match in pattern.finditer(help_string):
        # extract words
        func(match)


def csv(fname, fun):
    sep = ","
    with open(fname) as fp:
        for s in fp.readlines():
            t = []
            for s1 in s.strip("\n").split(sep):
                t.append(coerce(s1))
            fun(t)
    return


def rnd(x, places):
    mult = 10 ** (places or 2)
    return math.floor(x * mult + 0.5) / mult


def per(t, p):
    p = math.floor(((p or .5) * len(t) - 1) + .5)
    return t[max(0, min(len(t) - 1, p))]


def o(t):
    if not (isinstance(t, dict) or isinstance(t, list)):
        return str(t)

    def show(k, v):
        if str(k).find("_") != 0:
            v = o(v)
            return (isinstance(t, dict) and ":{} {}".format(k, v)) or str(v)

    if isinstance(t, dict):
        u = [show(k, v) for k, v in t.items()]
        if isinstance(t, dict):
            u = sorted(u)
        return "{" + " ".join(u) + "}"
    elif isinstance(t, list):
        u = [show(k, v) for k, v in enumerate(t)]
        return "{" + " ".join(u) + "}"


def oo(t):
    return print(o(t))


def copy(t):
    if not (isinstance(t, list) or isinstance(t, dict)):
        return t
    elif isinstance(t, list):
        return t.copy()
    else:
        u = {}
        for k in t:
            u[k] = t[k]
        return u
