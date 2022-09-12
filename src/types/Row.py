from Obj import Obj

class Row(Obj):
    def __init__(self,t):
        super().__init__("Row")
        return {"cells":t,
                "cooked":t.copy(),
                "isEvaled":False
                }
