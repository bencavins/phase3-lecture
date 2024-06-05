"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class Dog:
    def __init__(self, name, age, breed='unknown', is_good=True):
        self.name = name
        self.age = age
        self.breed = breed
        self.is_good = is_good
    
    def __repr__(self):
        return f'<Dog {self.name} {self.age} {self.breed} {self.is_good}>'
    
d1 = Dog(name='fido', age=3, breed='bulldog')
print(d1)