import math


class ShapeValueError(Exception):
    pass


def is_number(value):
    """Return True if value is a number"""
    return isinstance(value, int) or isinstance(value, float)


def is_positive(value):
    """Return True if value is a number and > 0"""
    return is_number(value) and value > 0


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, new_x):
        if is_number(new_x):
            self._x = new_x
        else:
            raise ShapeValueError('x must be a number')
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, new_y):
        if is_number(new_y):
            self._y = new_y
        else:
            raise ShapeValueError('y must be a number')
    
    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        raise NotImplementedError
    

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        if is_positive(new_radius):
            self._radius = new_radius
        else:
            raise ShapeValueError('radius must be a positive number')
    
    def get_area(self):
        return math.pi * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
    def __repr__(self):
        return f"<Circle x:{self.x}, y:{self.y}, r:{self.radius}>"


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, new_width):
        if is_positive(new_width):
            self._width = new_width
        else:
            raise ShapeValueError('width must be positive')
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, new_height):
        if is_positive(new_height):
            self._height = new_height
        else:
            raise ShapeValueError('height must be positive')
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.height * 2) + (self.width * 2)

    def __repr__(self):
        return f"<Rectangle x:{self.x}, y:{self.y}, w:{self.width}, h:{self.height}>"


class Square(Rectangle):
    def __init__(self, x, y, width):
        super().__init__(x, y, width, width)


r = Square(1, 2, 25)
print(r.get_area())
print(r.get_perimeter())