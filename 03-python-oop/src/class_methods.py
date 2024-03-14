class Dog:
    species = 'canine'  # class attribute
    all = []

    @classmethod
    def print_species(cls):  # class method
        print(cls.species)  # print(Dog.species)

    def __init__(self, name_param, age_param, breed_param):
        self.name = name_param
        self.age = age_param
        self.breed = breed_param
        Dog.all.append(self)  # append this dog to Dog.all