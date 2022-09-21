from src.types.Obj import Obj
from src.types.Cols import Cols
from src.types.Row import Row
from src.utils import csv, rnd, checknum


class Data(Obj):
    def __init__(self, src):
        super().__init__("Data")
        self.cols = None
        self.rows = []
        if isinstance(src, str):
            csv(src, self.add)
        elif isinstance(src, dict):
            for row in src.values():
                self.add(row)
        return

    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = xs if hasattr(xs, 'cells') and xs.cells else Row(xs)
            self.rows.append(row)
            for todo in self.cols.x + self.cols.y:
                todo.add(row.cells[todo.at])

    def stats(self, places, showCols=None, fun=None):
        def mid(col):
            return col.mid()
        if showCols is None:
            showCols = self.cols.y
        if fun is None:
            fun=mid
        t = {}
        for col in showCols:
            v = fun(col)
            v = checknum(v) and rnd(v, places) or v
            t[col.name] = v
        return t
