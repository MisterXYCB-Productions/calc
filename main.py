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
        
        non_null_angles = [angle for angle in [self.alpha, self.beta, self.gamma] if angle is not None]
        non_null_sides = [side for side in [self.a, self.b, self.c] if side is not None]
        
        if all([self.a, self.b, self.c]):
            self._sides_to_angles()
        elif all([self.alpha, self.beta, self.gamma]):
            self._angles_to_sides()
        elif len(non_null_angles) == 2 and len(non_null_sides) == 1:
            self._two_angles_one_side(non_null_angles, non_null_sides)
        elif len(non_null_angles) == 1 and len(non_null_sides) == 2:
            self._one_angle_two_sides(non_null_angles, non_null_sides)
        
        return self
    
    def _sides_to_angles(self) -> None:
        self.alpha = math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2)/(2*self.b*self.c)))
        self.beta = math.degrees(math.acos((self.a**2 + self.c**2 - self.b**2)/(2*self.a*self.c)))
        self.gamma = math.degrees(math.acos((self.a**2 + self.b**2 - self.c**2)/(2*self.a*self.b)))
    
    def _angles_to_sides(self) -> None:
        if self.a:
            self.b = self.a*math.sin(math.radians(self.beta))/math.sin(math.radians(self.alpha))
            self.c = self.a*math.sin(math.radians(self.gamma))/math.sin(math.radians(self.alpha))
        elif self.b:
            self.a = self.b*math.sin(math.radians(self.alpha))/math.sin(math.radians(self.beta))
            self.c = self.b*math.sin(math.radians(self.gamma))/math.sin(math.radians(self.beta))
        elif self.c:
            self.a = self.c*math.sin(math.radians(self.alpha))/math.sin(math.radians(self.gamma))
            self.b = self.c*math.sin(math.radians(self.beta))/math.sin(math.radians(self.gamma))
        else:
            self.a = 1
            self.b = math.sin(math.radians(self.beta))/math.sin(math.radians(self.alpha))
            self.c = math.sin(math.radians(self.gamma))/math.sin(math.radians(self.alpha))
            
    def _two_angles_one_side(self, angles: list, sides: list) -> None:
        if self.alpha and self.beta:
            self.gamma = 180 - self.alpha - self.beta
        elif self.beta and self.gamma:
            self.alpha = 180 - self.beta - self.gamma
        elif self.alpha and self.gamma:
            self.beta = 180 - self.alpha - self.gamma
        
        self._angles_to_sides()
    
    def _one_angle_two_sides(self, angles: list, sides: list) -> None:
        if self.a and self.b:
            self.gamma = math.degrees(math.asin(self.a*math.sin(math.radians(self.beta))/self.b))
        elif self.b and self.c:
            self.alpha = math.degrees(math.asin(self.b*math.sin(math.radians(self.gamma))/self.c))
        elif self.a and self.c:
            self.beta = math.degrees(math.asin(self.a*math.sin(math.radians(self.gamma))/self.c))
        
        self._angles_to_sides()

    def __str__(self) -> str:
        return f"Triangle(a={self.a}, b={self.b}, c={self.c}, alpha={self.alpha}, beta={self.beta}, gamma={self.gamma})"

t = Triangle().from_kw(a=3, b=4, c=5)
print(t)