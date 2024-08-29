class Dog:
    my_class_attribute = 'some value'
    genus = 'canine'
    species = 'familiaris'
    valid_breeds = ['bulldog', 'terrier', 'poodle']
    all = []

    @classmethod
    def print_sci_name(cls):
        # print(cls)
        print(cls.genus, cls.species)

    @classmethod
    def get_avg_age(cls):
        total = 0
        for dog in cls.all:
            total += dog.age
        return total / len(cls.all)

    def __init__(self, name, age, breed):
        self.name = name  # uses setter
        self.age = age  # uses setter
        self.breed = breed
        Dog.all.append(self)  # append this dog obj to Dog.all

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, new_breed):
        if new_breed in Dog.valid_breeds:
            self._breed = new_breed
        else:
            raise ValueError(f'invalid breed: {new_breed}')
    
    def __repr__(self) -> str:
        return f'<Dog {self.name} {self.age} {self.breed}>'


# instansiate some dog objects
d1 = Dog('fido', 4, 'bulldog')  # kinda like Dog.__init__()
d2 = Dog('fluffy', 2, 'poodle')
# d3 = Dog('fluffy', 2, 'xyz')

# access class attributes with ClassName.attribute_name
# print(Dog.genus, Dog.species)
# # can also use obj.class_attribute
# print(d1.genus, d1.species)

print(Dog.get_avg_age())