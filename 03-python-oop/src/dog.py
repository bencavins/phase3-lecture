"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

class Dog:
    # constructor 
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says 'bark!'")
    
    def __repr__(self):
        """
        This gets called whenever the obj is printed
        This should return a string
        """
        return f"<Dog name={self.name} age={self.age}>"


my_dog = Dog('fido')
my_dog.bark()
# print(my_dog)
# another_dog = Dog('rex', 4)
# another_dog.bark()
# print(another_dog)