"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

# old style properties
class Dog:
    def __init__(self, name_param, age_param, breed_param):
        self.name = name_param
        self._age = age_param
        self.breed = breed_param
    
    def get_age(self):  # getter function/method
        print('inside getter')
        return self._age

    def set_age(self, new_age):
        print('inside setter')
        if new_age >= 0:
            self._age = new_age
        else:
            print('invalid age')
    
    age = property(get_age, set_age)  # forces us to use getter/setter whenever we access self.age


# my_dog.age actually calles my_dog.get_age()
# my_dog.age = 3 actually calls my_dog.set_age(3)


# my_dog = Dog('fido', 3, 'bulldog')  # build dog
# print(my_dog.age)  # get age (by calling get_age)
# my_dog.age = -1 # change age
# print(my_dog.age)
# my_dog.age = -1  # this bypasses our setter :(
# print(my_dog.get_age())  # get age



# new style properties
class Dog:
    def __init__(self, name_param, age_param, breed_param):
        self.name = name_param
        self._age = age_param
        self.breed = breed_param
    
    @property  # this marks this function as a getter for age
    def age(self):  # getter function/method
        print('inside getter')
        return self._age

    @age.setter  # this marks this function as a setter for age
    def age(self, new_age):
        print('inside setter')
        if new_age >= 0:
            self._age = new_age
        else:
            print('invalid age')

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    # age = property(get_age, set_age) 


my_dog = Dog('fido', 3, 'bulldog')  # build dog
print(my_dog.age)  # get age (by calling my_dog.get_age())
my_dog.age = -1 # change age (by calling my_dog.set_age(-1))
print(my_dog.age)