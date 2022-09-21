from src.utils import oo
import src.constants
from src.types.Sym import Sym
from src.types.Num import Num
from src.types.Data import Data
from tests.testUtils import runs


class Example:
    def __init__(self):
        self.fails = 0

    def BAD(self):
        print(self.dont_have_this_field)

    def LIST(self):
        t = [method for method in dir(Example) if method.startswith('__') is False]
        return sorted(t)

    def LS(self):
        print("\nExamples lua csv −e ...")
        for test in self.LIST():
            print(str.format("\t{}".format(test)))
        return True

    def ALL(self):
        for _, k in enumerate(self.LIST()):
            if k != "ALL":
                print("\n−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
                if not runs(self, k):
                    self.fails += 1
        return True

    def the(self):
        oo(src.constants.the)
        return True

    def sym(self):
        sym = Sym()
        for x in ["a", "a", "a", "a", "b", "b", "c"]:
            sym.add(x)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000 * entropy) // 1 / 1000
        oo({"mid": mode, "div": entropy})
        print(mode, entropy)
        return mode == "a" and 1.37 <= entropy <= 1.38

    def num(self):
        num_obj = Num()
        for i in range(1, 101):
            num_obj.add(i)
        div_val, mid_val = num_obj.div(), num_obj.mid()
        print(mid_val, div_val)
        return 52 >= mid_val >= 50 and 32 > div_val > 30.5

    def bignum(self):
        num_obj = Num()
        src.constants.the['nums'] = 32
        for i in range(0, 999):
            num_obj.add(i + 1)
        oo(num_obj.nums())
        return 32 == len(num_obj._has)
