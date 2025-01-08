class Animal:
    sound = None

    def __init__(self, name, age):
        print('setting name and age')
        self.name = name
        self.age = age

    def speak(self):
        print(self.sound)

class Dog(Animal):
    sound = 'bark'
    speak_count = 0

    def __init__(self, name, age, breed):
        # super looks at the parent class
        # calls the constructor for Animal (e.g., Animal.__init__())
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        Dog.speak_count += 1
        print(f'speak count is: {Dog.speak_count}')
        super().speak()  # call the parent version of speak

    def __repr__(self):
        return f'<Dog name={self.name} age={self.age} breed={self.breed}>'
    
class Cat(Animal):
    sound = 'meow'

    def __repr__(self):
        return f'<Cat name={self.name} age={self.age}>'

class Bird(Animal):
    sound = 'chirp'
    
    def __repr__(self):
        return f'<Bird name={self.name} age={self.age}>'

d1 = Dog(name='fluffy', age=3, breed='poodle')
c1 = Cat(name='garfield', age=15)
b1 = Bird(name='tweety', age=2)

pets = [d1, b1, c1]

for pet in pets:
    pet.speak()
