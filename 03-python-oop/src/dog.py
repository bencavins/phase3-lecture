"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

# name
# age
# breed

class Dog:
    # constructor method
    def __init__(self, name_param, age, breed):
        # attributes
        self._name = None  # this attribute is private (can only be access with getter and setter)
        self._age = None

        self.name = name_param  # uses setter
        self.age = age  # uses setter
        self.breed = breed

    def get_name(self):  # name getter
        # avoid calling self.name -> self.get_name(), infinite loop
        return self._name

    def set_name(self, new_name):  # name setter
        # make sure the new_name is a string
        # and has at least one character
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            print(f'error invalid name: {new_name}')

    # creating a name property
    # that is linked to the getter and setter
    name = property(get_name, set_name)

    # getter for age
    @property
    def age(self):
        return self._age
    
    # setter for age
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and new_age >= 0:
            self._age = new_age
        else:
            print(f'invalid age: {new_age}')

    # method
    def bark(self, n):
        print(f'{self.get_name()} says "bark!"')

    def has_birthday(self):
        self.age += 1


# instansiate some dog objects
d1 = Dog('fido', 4, 'bulldog')  # kinda like Dog.__init__()
d2 = Dog('fluffy', 2, 'poodle')


print(d1.age)  # calls getter
d1.age = -1  # calls setter
print(d1.age)


# writing the attribute
# calling d1.set_name([1, 2, 3])
d1.name = [1, 2, 3]

# reading the attribute
# calling d1.get_name()
d1.name


