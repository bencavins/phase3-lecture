import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        if new_radius > 0:
            self._radius = new_radius

    @property
    def diameter(self):
        return self.radius * 2
    
    def get_area(self):
        return math.pi * (self.radius ** 2)
    
    def get_perimeter(self):
        return self.diameter * math.pi

    def __repr__(self):
        return f'<Circle >'

c1 = Circle(radius=1)