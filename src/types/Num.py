from collections import OrderedDict
from Obj import Obj
import random
from src.utils import per

THE_NUMS=99


class Num(Obj):
    def __init__(self,column_position=0,column_name=""):
        super().__init__("Num")
        self.n = 0  # items seen
        self.at = column_position # column position
        self.name = column_name  # column name
        self._has = OrderedDict()  # kept data
        self.lo = float('inf') #lowest seen
        self.hi= float('-inf')  #highest seen
        self.isSorted= True, # no updates since last sort of data
        self.w = (column_name or "":find"−$" and −1 or 1)   #ToDo: update the logic

    def nums(self):
        """
        Differs in implementation from Lua
        :return: sorted self._has dictionary
        """
        return self._has

    def add(self, v,pos):
        global THE_NUMS
        if v!="?":
            self.n +=1
            self.lo = min(self.lo,v)
            self.hi = max(self.hi,v)
            if len(self._has) < THE_NUMS:   #ToDo : change the the.nums
                pos = 1 + len(self._has)
            elif random.random() < THE_NUMS/self.n:  #ToDo : change the the.nums
                pos = random(len(self._has))
            if pos:
                self.isSorted = False
                self._has[pos] = int(v)

    def div(self,a):
        a = self.nums()
        return (per(a,0.9) - per(a,0.1)) / 2.58

    def mid(self):
        return per(self.nums(),0.5)