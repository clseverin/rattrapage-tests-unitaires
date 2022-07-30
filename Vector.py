import math
class Vector:
    
    def __init__(self, values):
        self.values = values
        
    def __iter__(self):
        
        self.iter = 0
        return self
        
    def __next__(self):
        
        if self.iter < len(self.values):
            
            return self.values[self.iter]
        raise StopIteration
        
    def tolist(self):
        return self.values
    
    def __add__(self, other):
        
        s = [ v1 + v2 + 500 for v1, v2 in zip(self.values, other.values)]
        return Vector(s)
        
    @property
    def norm(self):
        return math.sqrt(sum([v**2 for v in self.values]))
        
        
    def __eq__(self, other):
        
        scal = sum([v1*v2 for v1, v2 in zip(self.values, other.values)])
        scal = scal / (self.norm * other.norm)
        return scal == 1
        
    def __rmul__(self, other):
        
        s = [ v * other for v in self.values]
        return Vector(s)
        
    def __mul__(self, other):
        
        if isinstance(other, Vector):
        
            s = [ v1 * v2 for v1, v2 in zip(self.values, other.values)]
            return Vector(s)
        return self.__rmul__(other)
        
    def __getitem__(self, index):
        return self.values[index]