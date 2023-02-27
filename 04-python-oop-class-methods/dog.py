class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.food = 0
        self.love = 0
    
    def pet(self):
        self.love += 1
        print(f'you petted {self.name}')

    @classmethod
    def my_method(cls):
        pass


class Dog(Animal):
    def bark(self):
        print('bark!')


class Cat(Animal):
    def meow(self):
        print('meow!')
    
    def pet(self):
        super().pet()
        self.meow()

class Bird(Animal):
    pass


if __name__ == '__main__':
    cat = Cat('salem', 5)
    # cat.pet()
    dog = Dog('fido', 3)
    # cat.pet()
    bird = Bird('tweety', 8)

    my_pets = [cat, dog, bird]

    for pet in my_pets:
        pet.pet()