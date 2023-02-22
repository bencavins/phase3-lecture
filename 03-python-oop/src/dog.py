"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class Dog:
    def __init__(self, name, age):  # constructor
        print('calling constrctor')
        # variable == attribute/property
        self.name = name
        self.age = age
        self.breed = None
    
    def bark(self, sound):
        return f"{self.name} says {sound}!"
    
    def set_age(self, new_age):
        if (new_age > 0):
            self.age = new_age



my_dog = Dog('rex', 3)
my_dog.set_age(-1)
print(my_dog.age)