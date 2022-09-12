from Obj import Obj

class Row(Obj):
    def __init__(self,t):
        return {"cells":t,
                "cooked":t.copy(),
                "isEvaled":False
                }
