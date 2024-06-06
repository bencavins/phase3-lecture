class Pet:  # parent class
    def __init__(self, name, age, sound='hello'):
        self.name = name
        self.age = age
        self.sound = sound
    
    def say_hi(self):
        print(f'{self.name} says {self.sound}')
    
    def f(self):
        pass
    
    def __repr__(self):
        return f'<Pet {self.name} {self.age}>'

class Dog(Pet):  # Dog inherits from Pet
    def __init__(self, name, age, breed):
        super().__init__(name, age, sound='bark')  # calls the parent constructor
        self.breed = breed
    
    def go_for_walk(self):
        pass

    def say_hi(self):
        super().say_hi()  # calls the parent version of say_hi()
        print('dog wags tail')
        self.go_for_walk()

    def __repr__(self):
        return f'<Dog {self.name} {self.age} {self.breed}>'

class Cat(Pet):  # Cat inherits from Pet
    def __init__(self, name, age):
        super().__init__(name, age, sound='meow')

    def __repr__(self):
        return f'<Cat {self.name} {self.age}>'
    

pets = [
    Dog('fido', 3, 'bulldog'),
    Cat('angie', 14),
    Dog('rex', 5, 'terrier')
]


# print(dir(Dog('fido', 3, 'bulldog')))

for pet in pets:
    pet.say_hi()  # cats and dogs can say hi because they inherited from parent


