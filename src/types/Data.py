from src.types.Obj import Obj
from src.types.Cols import Cols
from src.types.Row import Row
from src.utils import csv, rnd


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
            row = xs if hasattr(xs, 'cell') and xs.cells else Row(xs)
            self.rows.append(row)
            for _, col in enumerate(self.cols.x + self.cols.y):
                col.add(row.cells[col.at])

    def stats(self, places, showCols=None, fun="mid"):
        if showCols is None:
            showCols = self.cols
        print(showCols)
        t = {}
        for col in showCols:
            v = fun(col)
            v = v.isnumeric() and rnd(v, places) or v
            t[col.name] = v
        return t
