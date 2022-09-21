from src.utils import init_the, cli
from src.constants import help_string, the
from tests.Example import Example
from tests.testUtils import runs


def main():
    init_the()
    cli()
    if the["help"]:
        print(help_string)
    else:
        eg = Example()
        runs(eg, the['eg'])

if __name__ == "__main__":
    main()
