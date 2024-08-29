import math


class Circle:
    def __init__(self, radius):
        self.radius = radius  # calls setter
        self.x = None
        self.y = None
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        if new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError(f'radius must be > 0')

    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, new_diameter):
        self.radius = new_diameter / 2
    
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    def __repr__(self):
        return f'<Circle r={self.radius}, d={self.diameter}, per={self.perimeter}, area={self.area}>'


c1 = Circle(10)
print(c1)
c1.diameter = 45
print(c1)
