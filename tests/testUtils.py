from tests import eg
from src.utils import the
import random
import sys

def oo(t):
    if type(t) == list:
        t = list(map(lambda x: str(x), t))
        out_string = "{" + " ".join(t) + "}"
        print(out_string)
        return out_string
    else:
        out_string = o(t)
        print(out_string)
        return out_string

def runs(k):
    err = None
    if not eg[k]:
        return 
    random.seed(the.seed)
    old = {}
    for k,v in enumerate(the):
        old[k]=v
    try:
        ##TODO eg[k]()
        if the.dump:
            status, out = True, eg[k]()
        else:
            status, out = True if eg[k] else False, None
    except Exception as e:
        err = sys.exc_info()
    finally:
        for k, v in enumerate(old):
            the[k] = v
        msg = status and ((out == True and "PASS") or "FAIL") or "CRASH"
        print("!!!!", msg, k, status)
        return out or err


      

    


     
    