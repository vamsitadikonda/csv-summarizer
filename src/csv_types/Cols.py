from src.csv_types.Obj import Obj
from src.csv_types.Sym import Sym
from src.csv_types.Num import Num
import re


class Cols(Obj):
    def __init__(self, names):
        super().__init__("Cols")
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        for c, s in enumerate(names):
            # Checking for the type of the column
            if re.search(r"^[A-Z]",s):
                col = Num(c, s)
                self.all.append(Num(c, s))
            else:
                col = Sym(c, s)
                self.all.append(Sym(c, s))
            # ignoring for hidden cols
            if not re.search(r":$",s):
                if re.search(r"[!+−-]$",s):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if re.search(r"!$",s):
                    self.klass = col
