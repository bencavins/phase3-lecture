class Person:
    def __init__(self, id=None, first_name='', last_name='', age=None):  # constructor
        self._id = None
        self._first_name = None
        self._last_name = None
        self._age = None

        self.id = id  # calls the setter
        self.first_name = first_name # calls the setter
        self.last_name = last_name # calls the setter
        self.age = age # calls the setter
    
    @property
    def id(self):
        """Getter for _id"""
        print('inside _id getter')
        return self._id

    @id.setter
    def id(self, new_id):
        """Setter for _id"""
        print('inside _id setter')
        self._id = new_id

    @property
    def first_name(self):
        """Getter for _first_name"""
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_first_name):
        """Setter for _first_name"""
        if isinstance(new_first_name, str):
            self._first_name = new_first_name
    
    @property
    def last_name(self):
        """This describes how the function works"""
        return self._last_name
    
    @last_name.setter
    def last_name(self, new_last_name):
        if isinstance(new_last_name, str):
            self._last_name = new_last_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self._age = new_age
    
    @property
    def full_name(self):
        return self.first_name + ' ' + self._last_name
    
    def func(self):
        """Doc string for func"""
        pass
    
    def __repr__(self):
        return f'<Person id={self.id} name={self.full_name} age={self.age}>'


# calls the Person constructor (__init__)
p1 = Person(
    id=123, 
    first_name='bob', 
    last_name='smith', 
    age=55) # Person.__init__()
p2 = Person(
    id=234, 
    first_name='alice', 
    last_name='jones', 
    age=34)


p1.id # calls the getter
p1.id = 234  # calls the setter
