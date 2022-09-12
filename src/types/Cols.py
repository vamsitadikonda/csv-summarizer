from Obj import Obj
from Sym import Sym
from Num import Num
import re 

class Cols(Obj):
    def __init__(self,names):
        super().__init__("Cols")
        self.names = names
        self.all = {}
        self.klass=None
        self.x = {}
        self.y = {}
        for c,s in enumerate(names):
            col = push(self.all,
                    (re.search(s,"^[A−Z]*") and Num or Sym)(c,s)
                    )
            if not re.search(s,":$"):
                push(re.search(s,"[!+−]") and self.y or self.x, col)
                if re.search(s,"!$"): 
                    self.klass=col 
            return 
             
              