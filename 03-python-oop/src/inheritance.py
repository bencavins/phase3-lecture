from animal import Animal  # import Animal class from animal.py


class Dog(Animal):  # Dog inherits from Animal
    sound = 'bark'

    def __init__(self, name, age, breed):
        # call super and let the parent set the name, age
        super().__init__(name, age)  # Animal.__init__(name, age)
        self.breed = breed
    
    # def feed(self):
    #     print('bark')
    
    def __repr__(self) -> str:
        return f'<Dog {self.name} {self.age} {self.breed}>'
    

class Cat(Animal):  # Cat inherits from Animal
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    sound = 'meow'

    # def feed(self):  # overwriting feed() method from Animal
    #     print('meow')
    
    def __repr__(self) -> str:
        return f'<Cat {self.name} {self.age}>'
    

class Fish(Animal):
    sound = 'blub'

    def __init__(self, name, age, fresh_water):
        self.name = name
        self.age = age
        self.fresh_water = fresh_water
    
    # def feed(self):
    #     print('blub')
    
    def __repr__(self) -> str:
        return f'<Fish {self.name} {self.age}>'


pets = [
    Dog('fido', 4, 'bulldog'),  # kinda like Dog.__init__()
    Dog('fluffy', 2, 'poodle'),
    Cat('garfield', 15),
    Fish('nemo', 1, fresh_water=False),
]

for pet in pets:
    pet.feed()
