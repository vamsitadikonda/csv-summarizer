from tests.testUtils import oo
from src.constants import the
from src.types.Sym import Sym
from src.types.Num import Num
from src.types.Data import Data


class Example:
    def __init__(self):
        self.fail = 0

    def BAD(self):
        print(self.dont_have_this_field)

    def LIST(self):
        t = [method for method in dir(Example) if method.startswith('__') is False]
        return sorted(t)

    def LS(self):
        print("\nExamples lua csv −e ...")
        for test in self.LIST():
            print(str.format("\t%s", test))
        return True

    def ALL(self):
        for _, k in enumerate(self.LIST()):
            if k != "ALL":
                print("\n−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
                if not self.runs(k):
                    self.fails += 1
        return True

    def the(self):
        oo(the)
        return True

    def sym(self):
        sym = Sym()
        for x in ["a", "a", "a", "a", "b", "b", "c"]:
            sym.add(x)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000 * entropy) // 1 / 1000
        oo({"mid": mode, "div": entropy})
        return mode == "a" and 1.37 <= entropy <= 1.38

    def num(self):
        num_obj = Num()
        for i in range(0, 99):
            num_obj.add(i + 1)
        print(num_obj.div(), num_obj.mid())

        div_val, mid_val = num_obj.div(), num_obj.mid()
        return 52 >= mid_val >= 50 and 32 > div_val > 30.5

    def bignum(self):
        num_obj = Num()
        the['nums'] = 32
        for i in range(0, 999):
            num_obj.add(i + 1)
        oo(num_obj.nums())
        return 32 == len(num_obj._has)
