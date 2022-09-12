from Obj import Obj

class Data(Obj):
    def __init__(self):
        super(Data, self).__init__("Data")
        self.rows = None
        self.cols = {}
