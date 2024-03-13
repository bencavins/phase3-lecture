import math

# perimeter = pi*r*2
# area = pi * r^2

class Circle:
    def __init__(self, radius):
        self.radius = radius
        # self.perimeter = 2 * math.pi * radius # best not to store the perimeter, we can calculate it
    
    @property
    def perimeter(self):  # perimeter getter (calcuates it using the radius)
        return 2 * math.pi * self.radius
    
    @perimeter.setter
    def perimeter(self, new_perimeter):  # perimeter setter (reverse engineers the radius and sets it)
        self.radius = new_perimeter / 2 / math.pi

    @property
    def area(self):  # area getter (calculates it using the radius)
        return math.pi * (self.radius ** 2)
    
    def __repr__(self):
        return f"<Circle raidus: {self.radius} perimeter: {self.perimeter} area: {self.area}>"


c1 = Circle(3)  # calls constructor
print(c1)  # calls __repr__
# c1.radius = 5  # sets radius attribute directly (we don't have a setter for radius)
c1.perimeter = 7  # calls setter
print(c1)  # calls __repr__
