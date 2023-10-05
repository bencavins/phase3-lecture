class Owner:
    def __init__(self, name):
        self.name = name
        self.dogs = []
    
    def add_dog(self, dog_name):
        new_dog = Dog(dog_name)
        new_dog.owner = self  # link from dog -> owner
        self.dogs.append(new_dog)  # link from owner -> dog(s)

class Dog:
    def __init__(self, name, owner=None):
        self.name = name
        self.owner = owner


owner = Owner('joe')
owner.add_dog('fido')
owner.add_dog('rex')


print(f'owner {owner.name} has these dogs:')
for dog in owner.dogs:
    print(dog.name)