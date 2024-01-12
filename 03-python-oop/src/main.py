"""
Create an Owner class that relates to Dog
Owners can have multiple Dogs
Dogs can have only one Owner

Add these Owner methods:
add_dog(new_dog)
  - adds a new dog obj to the owner
get_all_dog_names()
  - returns a list of strings of all dog names this owner owns
get_oldest_dog()
  - returns the oldest dog (i.e., the Dog obj with the largest age)
get_puppies()
  - returns a list of Dog objects that have an age between 0-1.
"""

class Owner():
    def __init__(self, name):
        self.name = name
        self.dogs = []
    
    def add_dog(self, new_dog):
        new_dog.owner = self
        self.dogs.append(new_dog)

    def get_all_dog_names(self):
        result = []
        for dog in self.dogs:
            result.append(dog.name)
        return result
        # return [dog.name for dog in self.dogs]
    
    def get_oldest_dog(self):
        oldest_dog = self.dogs[0]  # pick the first one for starters
        for current_dog in self.dogs:
            if current_dog.age > oldest_dog.age:
                oldest_dog = current_dog
        return oldest_dog
    
    def get_oldest_dog_v2(self):
        oldest_dog = None  # initialize to None
        for current_dog in self.dogs:
            if oldest_dog is None:  # True only for first iteration
                oldest_dog = current_dog
            else:
                if current_dog.age > oldest_dog.age: # our regular if check
                    oldest_dog = current_dog
        return oldest_dog
    
    def get_oldest_dog_v3(self):
        if len(self.dogs) == 0:
            return None
        oldest_dog = self.dogs[0]  # pick the first one for starters
        for current_dog in self.dogs:
            if current_dog.age > oldest_dog.age:
                oldest_dog = current_dog
        return oldest_dog
    
    def get_puppies(self):
        result = []
        for dog in self.dogs:
            if 0 <= dog.age <= 1:  # if dog.age >= 0 and dog.age <= 1
                result.append(dog)
        return result
    
    def __repr__(self):
        return f'<Owner {self.name}>'

class Dog:
    def __init__(self, name, age, owner=None):  # constructor function
        """
        This function gets called every time an object is built
        with this class
        """
        self.name = name  # attributes
        self.age = age

        if owner is not None:
            self.owner = owner  # link owner to dog
            self.owner.dogs.append(self)  # link dog to owner

    @property
    def age(self):
        """Getter function for age"""
        # print('in age getter')
        return self._age # this prevents a name conflict
    
    @age.setter
    def age(self, new_age):
        """Setter function for age"""
        # print('in setter')
        if new_age >= 0:
            self._age = new_age
    
    def bark(self):  # methods
        print(f'{self.name} says bark!')
    
    def feed(self, food):
        if food == 'kibble':
            print('yum!')
        else:
            print('yuck!')
    
    def __repr__(self) -> str:
        return f'<Dog {self.name}>'

if __name__ == '__main__':
    joe = Owner('joe')
    josh = Owner('josh')

    rex = Dog('rex', 0, joe)
    fido = Dog('fido', 1, joe)
    gus = Dog('gus', 0)
    josh.add_dog(gus)

    print(joe.get_puppies())

    # print(joe.dogs)
    # print(joe.get_oldest_dog())
