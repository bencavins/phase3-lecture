from dog import Dog

class Owner:
    def __init__(self, name):
        self.name = name
        self.dogs = []
    
    def pet_all(self):
        for dog in self.dogs:
            print(f"{dog.name} says <3")

if __name__ == '__main__':
    owner = Owner('joe')
    dog1 = Dog(name='rex', age=2, owner=owner)
    dog2 = Dog(name='fido', age=5, owner=owner)
    owner.dogs.extend([dog1, dog2])
    # owner.dogs = owner.dogs + [dog1, dog2]
