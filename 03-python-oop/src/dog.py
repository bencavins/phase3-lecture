"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class Dog:
    # constructor 
    def __init__(self, name='fido', age=1):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f'{self.name} says: bark!')
    
    def __repr__(self):
        return f'<Dog name={self.name} age={self.age} >'

