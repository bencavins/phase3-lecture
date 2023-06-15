"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class Dog:
    # constructor 
    def __init__(self, name='fido', age=1, owner=None):
        self.name = name
        self.age = age
        self.owner = owner

    def get_name(self):
        print('calling get_name')
        return self._name
    
    def set_name(self, new_name):
        print('calling set_name')
        if type(new_name) == str:
            self._name = new_name
        else:
            print('invalid name')
    
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        print('calling set_age')
        if type(new_age) == int and new_age >= 0:
            self._age = new_age
        else:
            raise Exception('invalid age')

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    
    def bark(self):
        print(f'{self.name} says: bark!')
    
    def __repr__(self):
        return f'<Dog name={self.name} age={self.age} >'


if __name__ == '__main__':
    my_dog = Dog()
    print(my_dog)