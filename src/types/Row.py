from src.types.Obj import Obj
from src.utils import copy


class Row(Obj):
    def __init__(self, t):
        super().__init__("Row")
        self.cells = t
        self.cooked = t.copy()
        self.isEvaled = False
