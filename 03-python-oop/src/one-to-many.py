class Dog:
    def __init__(self, name, age, owner=None):  # constructor function
        """
        This function gets called every time an object is built
        with this class
        """
        self.name = name  # attributes
        self.age = age
        self.owner = owner

        if owner is not None:
            owner.dogs.append(self)  # append myself to the owner's dogs array
    
    def bark(self):  # methods
        print(f'{self.name} says bark!')

    def print_owner_name(self):
        print(self.owner.name)

    def __repr__(self) -> str:
        return f'<Dog {self.name}>'


class Owner:
    def __init__(self, name):
        self.name = name
        self.dogs = []  # array of Dog objects
    
    def add_dog(self, dog):
        """Takes a Dog obj and adds it to the dogs array"""
        self.dogs.append(dog)

    def feed(self):
        for dog in self.dogs:
            print(f'feeding {dog.name}')

    def __repr__(self) -> str:
        return f'<Owner {self.name}>'



if __name__ == '__main__':
    joe = Owner('joe')
    fido = Dog('fido', 3, joe)
    rex = Dog('rex', 4, joe)

    joe.feed()
