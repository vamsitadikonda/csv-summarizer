from src.types.Num import Num
from src.types.Sym import Sym
from testUtils import eg,runs,oo
from src.utils import the


def eg_BAD():
    print(eg.dont.have.this.field)

def eg_LIST():
    t = {}
    for k,_ in enumerate(eg):
        t[1+len(t)] = k
        t = sorted(t.items(), key=lambda x: x[1])

def eg_LS():
    print("\nExamples lua csv −e ...")
    for _,k in enumerate(eg_LIST()):
        print(str.format("\t%s",k))
    return True

def eg_ALL():
    for _,k in enumerate(eg_LIST()):
        if k != "ALL":
            print("\n−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
            if not runs(k):
                fails = fails+1
    return True


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

def eg_num():
    num_obj = Num()
    for i in range(0,99):
        num_obj.add(i+1)
    print(num_obj.div(),num_obj.mid())

    div_val,mid_val  = num_obj.div(),num_obj.mid()
    return 52 >= mid_val and mid_val >= 50 and 32 > div_val and div_val > 30.5

def eg_bignum():
    num_obj = Num()
    the['nums'] = 32
    for i in range(0,999):
        num_obj.add(i+1)
    oo(num_obj.nums())
    return 32 == len(num_obj._has)