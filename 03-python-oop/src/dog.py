"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class Dog:
    all_dogs = []  # class attribute 
    genus = 'canine'

    @classmethod
    def print_all_dogs(cls):
        for dog in cls.all_dogs:
            print(dog)

    def __init__(self, name, age, breed='unknown', is_good=True):
        self.name = name
        self.age = age
        self.breed = breed
        self.is_good = is_good
        Dog.all_dogs.append(self)
    
    def __repr__(self):
        return f'<Dog {Dog.genus} {self.name} {self.age} {self.breed} {self.is_good}>'
    
Dog(name='fido', age=3, breed='bulldog')
Dog(name='rex', age=6, breed='terrier')


Dog.print_all_dogs()
