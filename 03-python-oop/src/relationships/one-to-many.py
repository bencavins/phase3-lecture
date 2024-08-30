class Owner:
    def __init__(self, name):
        self.name = name
        # self.pets = []  # array of Pet objects

    def get_pets(self):
        """Return an array of pets that belong to this owner"""
        result = []
        for pet in Pet.all:
            if pet.owner is self:  # is keyword better than ==
                result.append(pet)
        return result
    
    def feed(self):
        for pet in self.get_pets():
            print(f'feeding {pet.name}')
    
    def __repr__(self) -> str:
        return f'<Owner {self.name}>'
    

class Pet:
    all = []

    def __init__(self, name, age, type, owner):
        self.name = name
        self.age = age
        self.type = type

        # build out relationships
        self.owner = owner  # Owner object
        # self.owner.pets.append(self)  # add this pet to the owner's pets array

        Pet.all.append(self)  # add this pet to the all pets array
    
    def __repr__(self) -> str:
        return f'<Pet {self.name} {self.age} {self.type}>'
    

bob = Owner('bob')
fido = Pet('fido', 3, 'dog', owner=bob)
rex = Pet('rex', 1, 'dog', owner=bob)


john = Owner('john arbuckle')
garfield = Pet('garfield', 15, 'cat', owner=john)
odie = Pet('odie', 2, 'dog', owner=john)

# garfield.owner = bob

# john.feed()

print(bob.get_pets())
# print(john)
# print(john.get_pets())


# print(garfield)
# print(garfield.owner)
