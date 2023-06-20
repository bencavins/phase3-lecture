class Animal:
    sound = None

    def __init__(self, name, age, species):
        print('inside Animal')
        self.name = name
        self.age = age
        self.species = species
    
    def say_hello(self):
        print(f'{self.name} says {self.sound}!')