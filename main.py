import math



class Triangle():
    def __init__(self) -> None:
        self.a = None
        self.b = None
        self.c = None
        
        self.alpha = None
        self.beta = None
        self.gamma = None
        
    def _kw_to_var(self, kw: dict) -> None:
        for key, value in kw.items():
            match key:
                case "a": self.a = value
                case "b": self.b = value
                case "c": self.c = value
                case "alpha": self.alpha = value
                case "beta": self.beta = value
                case "gamma": self.gamma = value
            
    def from_kw(self, **kw):
        self._kw_to_var(kw)
        
        self.alpha = float(math.degrees(math.acos(((self.a ** 2) - (self.b ** 2) - (self.c ** 2)) / ( -2 * self.b * self.c))))
        self.beta = float(math.degrees(math.acos(((self.b ** 2) - (self.a ** 2) - (self.c ** 2)) / ( -2 * self.a * self.c))))
        self.gamma = float(math.degrees(math.acos(((self.c ** 2) - (self.b ** 2) - (self.a ** 2)) / ( -2 * self.b * self.a))))
    
    def from_sws(self, **kw):
        self._kw_to_var(kw)
        
        lengths = {"a": self.a, "b": self.b, "c": self.c}
        angles = {"alpha": self.alpha, "beta": self.beta, "gamma": self.gamma}
        
        for key, value in lengths.items():
            if value != None:
                lengths.pop(key)
        
        for key, value in angles.items():
            if value != None:
                angles.pop(key)
        
        
        
        
    
    