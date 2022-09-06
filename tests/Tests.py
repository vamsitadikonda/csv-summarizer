from src.types.Num import Num
from src.types.Sym import Sym

def eg_the():
    oo(the)
    return True

def eg_sym():
    sym = Sym()
    for x in list("a","a","a","a","b","b","c"):
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000*entropy)//1/1000
    oo({"mid":mode, "div":entropy})
    return mode=="a" and 1.37 <= entropy and entropy <=1.38
