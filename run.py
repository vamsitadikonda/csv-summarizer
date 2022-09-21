from src.utils import init_the, cli
from src.constants import help_string, the
from tests.Example import Example


def main():
    init_the()
    cli()
    print(the)
    if the["help"]:
        print(help_string)
    else:
        the['eg'] = Example()
        print(the["eg"].LIST())

if __name__ == "__main__":
    main()
