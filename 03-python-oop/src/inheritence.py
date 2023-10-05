class Pet:
    sound = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f'{self.name} says {self.sound}')

class Dog(Pet):  # Dog inherents from Pet
    genus = 'canine'
    sound = 'bark'

class Cat(Pet):
    genus = 'feline'
    sound = 'meow'


dog = Dog('fido', 3)
cat = Cat('angie', 12)
cat.say_hello()