from src.utils import init_the, the

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


def main():
    init_the()
    if the["help"]:
        print(help)
    else:
        print("Run Example")

if __name__ == "__main__":
    main()