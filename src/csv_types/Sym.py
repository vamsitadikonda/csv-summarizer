import math
from src.csv_types.Obj import Obj


class Sym(Obj):

    def __init__(self, column_position=0, column_name=""):
        super().__init__("Sym")
        self.n = 0  # items seen
        self.at = column_position # column position
        self.name = column_name  # column name
        self._has = {}  # kept data

    def add(self, v):
        if v != "?":
            self.n += 1
            self._has[v] = 1 + self._has[v] if v in self._has else 1

    def mid(self):
        most = -1
        for k in self._has:
            if self._has[k] > most:
                mode, most = k, self._has[k]
        return mode

    def div(self):
        def fun(p):
            return p * math.log2(p)

        e = 0
        for x in self._has.values():
            if x > 0:
                e = e - fun(x / self.n)
        return e
