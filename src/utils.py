import math
import sys
import os

help = """
CSV :   summarized csv file
(c) 2022 Tim Menzies<timm@ieee.org> BSD-2 license
USAGE: lua seen.lua (OPTIONS]
OPTIONS:
    -e  --eg        start-up example                        = None
    -d  --dump      on test failure, exit with stack dump   = false
    -f  --file      file with csv data                      = ../data/auto93.csv
    -h  --help      show help                               = false
    -n  --nums      number of nums to keep                  = 512
    -s  --seed      random seed                             = 10019
    -S  --Seperator feild separator                         = ,
"""
fails = 0

def coerce(s):
    def fun(s1):
        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1
    return int(s) if s.isnumeric() else None or fun(s.split()[0])

def cli(t,args):
    for slot, v in enumerate(t):
        v = str(v)
        for i in range(len(args)):
            if args[i] == "-"+slot[0] or args[i] == "--"+slot :
                v = (v=="false" and "true") or (v =="true" and "false") or args[i+1]
        t[slot] = coerce(v)
        if t.help: 
            os.exit(print("\n"+help+"\n"))
    return t

def push(t,x):
    t[1+len(t)]=x 
    return x       

def runs():
    ''''''  
def rogues():
    ''''''
def init_the():
    ''''''

def rnd(x, places):
    mult = 10**(places or 2)
    return math.floor(x * mult + 0.5) / mult


def per(t, p):
    p = math.floor(((p or .5) * len(t)) + .5)
    return t[max(1, min(len(t), p))]

the = {}
init_the()