# parent class
class Animal:
    species = None
    all = []

    def __init__(self, name_param, age_param):
        self.name = name_param
        self.age = age_param
        Animal.all.append(self)
    
    def say_hi(self):
        print(f"{self.name} says hello!")


# child class (inherites from Animal)
class Dog(Animal):
    species = 'canine'

    def __init__(self, name_param, age_param, breed_param):
        super().__init__(name_param, age_param)  # this calls Animal.__init__
        self.breed = breed_param

    def bark(self):
        print('bark')

    def say_hi(self):
        print(f"{self.name} says bark!")


# child class (inherites from Animal) 
class Cat(Animal):
    species = 'feline'
    
    def meow(self):
        print('meow')
    
    def say_hi(self):
        print(f"{self.name} says meow!")



Dog('fido', 4, 'bulldog')
Dog('gus', 12, 'terrier')
Cat('fluffy', 10)

for animal in Animal.all:
    animal.say_hi()
