from Obj import Obj


class Row(Obj):
    def __init__(self, t):
        super().__init__("Row")
        self.cells = t
        self.cooked = t.copy()
        self.isEvaled = False
