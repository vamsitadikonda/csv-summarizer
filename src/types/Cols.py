from Obj import Obj


class Cols(Obj):
    def __init__(self):
        super(Cols, self).__init__("Cols")
        self.rows = None
        self.cols = {}


