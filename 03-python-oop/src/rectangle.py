# classes are blueprints for objects
class Rectangle:
    # constructor -- function that builds the object
    def __init__(self, width_param, height_param):
        self._width = None
        self._height = None

        self.width = width_param  # calling width setter
        self.height = height_param  # calling height setter

    # old-school properties    
    def get_width(self):
        '''return the width'''
        # print('inside getter')
        return self._width  # make sure to access the _width attribute

    def set_width(self, new_width):
        '''update the existing width'''
        # print('in setter')
        if isinstance(new_width, int) and new_width > 0:
            self._width = new_width  # make sure to access the _width attribute
        else:
            raise ValueError('width must be positive')
    
    # make width a property
    width = property(get_width, set_width)

    # new-school properties
    @property
    def height(self):
        '''gets the height'''
        return self._height
    
    @height.setter
    def height(self, new_height):
        '''sets the height'''
        if new_height > 0:
            self._height = new_height
        else:
            raise ValueError('height must be positive')
    
    # method == functions attached to a class
    def get_area(self):
        return self.width * self.height
    
    def get_circumfrence(self):
        return (2 * self.width) + (2 * self.height)
    
    # this gets called when you print the object
    def __repr__(self):
        return f'<Rectangle w:{self.width}, h:{self.height}, a:{self.get_area()}>'


if __name__ == '__main__':
    # build a rectangle object
    r1 = Rectangle(2, 3)
    r2 = Rectangle(6, 9)

    print(r1)
    print(r2)
