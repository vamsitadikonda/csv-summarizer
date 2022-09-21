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
        print(the["eg"].ALL())
        #print(the["eg"].LIST())
        #print(the["eg"].LS())
        #print(the["eg"].bignum())
        #print(the["eg"].num())
        #print(the["eg"].sym())
        #print(the["eg"].the())
        print(the["eg"].stats())


if __name__ == "__main__":
    main()
