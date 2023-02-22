"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class Dog:
    all_dogs = []

    def __init__(self, name, age):  # constructor
        # variable == attribute/property
        self._name = name
        # self.set_age(age)
        self._age = age
        self.breed = None
        Dog.all_dogs.append(self)
    
    def bark(self, sound):
        self.age = -1
        return f"{self.name} says {sound}!"
    
    @property
    def name(self):
        return self._name.title()
    
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if (new_age > 0):
            self._age = new_age
        else:
            raise ValueError(f'invalid age: {new_age}')
        
    age = property(get_age, set_age)
    
    def __repr__(self):
        return f'<Dog {self.name} {self.age}>'
    
    @classmethod
    def print_all_dogs(cls):
        print(cls.all_dogs)
    


if __name__ == '__main__':
    # print(add(1, 3))
    my_dog = Dog('rex', 3)
    my_dog.bark('woof')
    # another_dog = Dog('gus', 10)
    # # my_dog.age = -1  # my_dog.set_age(-1)
    # print(Dog.all_dogs)