from collections import OrderedDict
from Obj import Obj
import random
import regex as re
from test import eg
from src.utils import *

THE_NUMS=99


class Num(Obj):
    def __init__(self,column_position,column_name):
        super().__init__("Num")
        self.n = 0  # items seen
        self.at = column_position or 0 # column position
        self.name = column_name or ""  # column name
        self._has = OrderedDict()  # kept data
        self.lo = float('inf') #−− lowest seen
        self.hi= float('-inf')  #highest seen
        self.isSorted= True, # no updates since last sort of data
        #Change
        if re.search(column_name or "","−$"):
            self.w = -1
        else:
            self.w = 1
        return 

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
            ##Change
            else:
                if random.random() < THE_NUMS/self.n:  #ToDo : change the the.nums
                    pos = random(len(self._has))
                if pos:
                    self.isSorted = False
                    self._has[pos] = int(v)

    def div(self,a):
        a = self.nums()
        return (per(a,0.9) - per(a,0.1)) / 2.58

    def mid(self):
        return per(self.nums(),0.5)