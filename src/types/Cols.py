from src.types.Obj import Obj
from src.types.Sym import Sym
from src.types.Num import Num
from src.utils import push
import re


class Cols(Obj):
    def __init__(self, names):
        super().__init__("Cols")
        self.names = names
        self.all = {}
        self.klass = None
        self.x = {}
        self.y = {}
        for c, s in enumerate(names):
            if re.search(s, "^[A−Z]*"):
                col = push(self.all, Num(c, s))
            else:
                col = push(self.all, Sym(c,s))
            if not re.search(s, ":$"):
                if re.search(s, "[!+−]"):
                    push(self.y, col)
                else:
                    push(self.x, col)
                if re.search(s, "!$"):
                    self.klass = col