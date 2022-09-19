from collections import OrderedDict
from Obj import Obj
from Cols import Cols
from Row import Row
from src.utils import csv, push, rnd


class Data(Obj):
    def __init__(self, src):
        super().__init__("Data")
        self.cols = None
        self.rows = {}
        if isinstance(src, str):
            csv(src, lambda x: self.add(x))
        elif isinstance(src, dict):
            for row in src.values():
                self.add(row)
        return

    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = push(self.rows, xs if xs.cells else Row(xs))
            for _, todo in enumerate(self.cols.x, self.cols.y):
                for _, col in enumerate(todo):
                    col.add(row.cells[col.at])
        return

    def stats(self, places, showCols=None, fun="mid"):
        if showCols is None:
            showCols = self.cols
        t = {}
        for col in showCols.values():
            v = fun(col)
            v = v.isnumeric() and rnd(v, places) or v
            t[col.name] = v
        return t
