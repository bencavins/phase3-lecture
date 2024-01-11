# Class 
# a blueprint
# describes how to build an object
# what data the object has
# what functions the object has

# Object (instance)
# a thing build using a class
# this is what we operate with
# probably will store in a variable 

"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

# with new school properties
class Dog:
    def __init__(self, name, age):  # constructor function
        """
        This function gets called every time an object is built
        with this class
        """
        self.name = name  # attributes
        self.age = age

    @property
    def age(self):
        """Getter function for age"""
        print('in age getter')
        return self._age # this prevents a name conflict
    
    @age.setter
    def age(self, new_age):
        """Setter function for age"""
        print('in setter')
        if new_age >= 0:
            self._age = new_age
    
    def bark(self):  # methods
        print(f'{self.name} says bark!')
    
    def feed(self, food):
        if food == 'kibble':
            print('yum!')
        else:
            print('yuck!')


# with old school properties
class Dog:
    def __init__(self, name, age):  # constructor function
        """
        This function gets called every time an object is built
        with this class
        """
        self.name = name  # attributes
        self.age = age
    
    # properties new school
    @property
    def age(self):
        """Getter function for age"""
        print('in age getter')
        return self._age # this prevents a name conflict
    
    @age.setter
    def age(self, new_age):
        """Setter function for age"""
        print('in setter')
        if new_age >= 0:
            self._age = new_age
    
    def bark(self):  # methods
        print(f'{self.name} says bark!')
    
    def feed(self, food):
        if food == 'kibble':
            print('yum!')
        else:
            print('yuck!')