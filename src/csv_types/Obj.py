from src.utils import o


class Obj:
    def __init__(self, type_name):
        self._type = type_name

    def __repr__(self, ):
        d = {}
        x = vars(self)
        for k in x:
            if not k.startswith("_"):
                d[k] = x[k]
        return o(d)
