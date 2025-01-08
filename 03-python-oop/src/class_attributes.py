class Dog:
    # class attributes
    genus = 'canine'
    all = []
    valid_breeds = ['bulldog', 'poodle', 'terrier']

    @classmethod
    def add_new_breed(cls, new_breed):
        print(cls)
        cls.valid_breeds.append(new_breed)
    
    @classmethod
    def get_most_popular_breed(cls):
        # count all the different breeds
        breed_counts = {}
        for dog in cls.all:
            if dog.breed in breed_counts:
                breed_counts[dog.breed] += 1
            else:
                breed_counts[dog.breed] = 1
        # find the largest count
        # return max(breed_counts, key=lambda breed: breed_counts[breed])
        print(breed_counts)
        max_breed = None
        max_count = 0
        for breed in breed_counts:
            count = breed_counts[breed]
            if count > max_count:
                max_count = count
                max_breed = breed
        return max_breed

    def __init__(self, name, breed):
        # instance attributes
        self.name = name
        self.breed = breed
        # append the new dog to the all class attribute
        Dog.all.append(self)
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, new_breed):
        if new_breed in Dog.valid_breeds:
            self._breed = new_breed
        else:
            raise ValueError('invalid breed')
    
    def bark(self):
        print('bark!')
    
    def __repr__(self):
        return f'<Dog name={self.name} breed={self.breed}>'


d1 = Dog(name='fido', breed='bulldog')
d2 = Dog(name='rex', breed='poodle')
d3 = Dog(name='fluffy', breed='poodle')
