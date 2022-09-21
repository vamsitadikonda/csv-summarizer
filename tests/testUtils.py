import src.constants
import random
import traceback


def runs(eg, k):
    if not (hasattr(eg, k) and callable(getattr(eg, k))):
        return
    err, status, out = None, None, None
    random.seed(src.constants.the["seed"])
    old = {k: src.constants.the[k] for k in src.constants.the}
    try:
        if src.constants.the['dump']:
            status, out = True, getattr(eg, k)()
        else:
            out = getattr(eg, k)()
            status = out is not None
            print(k,status,out)
    except Exception as e:
        status = False
        err = traceback.format_exc(e)
    finally:
        the = {k: old[k] for k in old}
        msg = status and ((out == True and "PASS") or "FAIL") or "CRASH"
        print("!!!!", msg, k, status)
        return out or err
