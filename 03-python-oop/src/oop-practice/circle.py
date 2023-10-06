import math

all = []

class Circle:
    def __init__(self, radius):
        self.radius = radius  # this calls our setter
        all.append(self)
    
    @property  # getter for radius
    def radius(self):
        return self._radius

    @radius.setter  # setter for radius
    def radius(self, new_radius):
        # make sure radius is not negative
        if new_radius < 0:
            raise ValueError(f"radius cannot be negative, value={new_radius}")
        else:
            self._radius = new_radius
    
    @property
    def circumfrence(self):
        return 2 * math.pi * self.radius
    
    @property
    def diameter(self):
        return 2 * self.radius
    
    @diameter.setter
    def diameter(self, new_diameter):
        self._radius = new_diameter / 2


# c = Circle(12)
# c.radius  # this will call the getter
# c.radius = 123  # this will call the setter