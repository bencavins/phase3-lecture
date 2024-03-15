class Dog:
    all = []

    def __init__(self, name_param, age_param, owner_param=None):
        self.name = name_param
        self.age = age_param
        self.owner = owner_param  # use this attribute to store the dog's owner
        Dog.all.append(self)

    def __repr__(self):
        return f"<Dog {self.name} {self.age}>"


class Owner:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        # self.dogs = [Dog(), Dog()]  # more efficient but and lead to data inconsistency 
    
    def get_dogs_no_list_comp(self):  # option 1
        result = []
        for dog_obj in Dog.all:
            if dog_obj.owner is self:  # if the dog's owner is myself
                result.append(dog_obj)
        return result

    def get_dogs(self):  # option 2
        return [dog_obj for dog_obj in Dog.all if dog_obj.owner is self]
    
    @property
    def dogs(self):  # option 3
        result = []
        for dog_obj in Dog.all:
            if dog_obj.owner is self:  # if the dog's owner is myself
                result.append(dog_obj)
        return result
    
    def __repr__(self):
        return f"<Owner {self.name} {self.phone_number}>"
    

my_owner = Owner('john', '555-555-5555')
my_dog = Dog('fido', 3, my_owner)
Dog('rando', 9999)

stray_dog = Dog('stray', 3)
