from src.csv_types.Obj import Obj
import random
import re
from src.utils import per


class Num(Obj):
    def __init__(self, column_position=0, column_name=""):
        super().__init__("Num")
        self.n = 0  # items seen
        self.at = column_position  # column position
        self.name = column_name  # column name
        self._has = []  # kept data
        self.lo = float('inf')  # lowest seen
        self.hi = float('-inf')  # highest seen
        self.isSorted = True,  # no updates since last sort of data
        if re.search(re.compile(r"-$"), column_name or ""):
            self.w = -1
        else:
            self.w = 1

    def nums(self):
        """
        :return: sorted self._has list
        """
        if not self.isSorted:
            self._has.sort()
            self.isSorted = True
        return self._has

    def add(self, v):
        from src.constants import the
        if v != "?":
            self.n += 1
            self.lo = min(self.lo, v)
            self.hi = max(self.hi, v)
            if len(self._has) < the["nums"]:
                self.isSorted = False
                self._has.append(int(v))
            elif random.random() < the["nums"] / self.n:
                pos = random.randint(0, len(self._has)-1)
                self.isSorted = False
                self._has[pos] = int(v)

    def div(self):
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1)) / 2.58

    def mid(self):
        return per(self.nums(), 0.5)
