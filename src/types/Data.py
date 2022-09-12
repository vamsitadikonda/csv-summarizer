from collections import OrderedDict
from Obj import Obj
from Num import Num
from Sym import Sym
import random
import re
from src.utils import *


class Data(Obj):
    def __init__(self,src):
        super().__init__("Data")
        self.cols = None
        self.rows = {}
        if isinstance(src,str):
            csv(src)
        else:
            for _,row in enumerate(src):
                self.add(row)
        return 

    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = push(self.rows, xs.cells and xs or Row(xs))
            for _,todo in enumerate(self.cols.x, self.cols.y ):
                for _,col in enumerate(todo):
                    col.add(row.cells[col.at])
        return

    def stats(self, places, showCols, fun):

        showCols, fun = showCols or self.cols.y, fun or "mid"
        t={}
        for _,col in enumerate(showCols):
            v=fun(col)
            v=v.isnumeric() and rnd(v,places) or v
            t[col.name]=v 
        return t 
