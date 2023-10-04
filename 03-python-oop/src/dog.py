"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class User:
    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name


u = User('joe', 'smith', 'pass123')
print(u.full_name)


class Dog:
    # constructor 
    def __init__(self, name, age=None):
        self._name = name
        self.age = age

    # getter function for age
    @property
    def age(self):
        print('inside getter')
        return self._age
    
    # setter function for age
    @age.setter
    def age(self, new_age):
        print('inside setter')
        if not isinstance(new_age, int) or new_age < 0:
            raise ValueError('invalid age')
        self._age = new_age
    
    # getter with no setter makes the property read-only
    @property
    def name(self):
        return self._name
    
    @property
    def pi(self):
        return 3.14
    
    def bark(self):
        print(f"{self.name} says 'bark!'")
    
    def __repr__(self):
        """
        This gets called whenever the obj is printed
        This should return a string
        """
        return f"<Dog name={self.name} age={self.age}>"


my_dog = Dog('fido', 7)
# my_dog.age = 'hello'
# my_dog.name = 'rex'
print(my_dog)
# another_dog = Dog('rex', 4)
# another_dog.bark()
# print(another_dog)