from Obj import Obj

class Test(Obj):
    def __init__(self,column_position,column_name):
        super().__init__("Obj")
        self.eg = {}
        return 