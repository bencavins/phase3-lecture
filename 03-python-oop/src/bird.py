"""
Write a Bird class that lets us:
- Store the bird's name as a string called 'name'
- Store the bird's type as a string called 'type' (for example, 'goose', 'swallow', 'robin', etc)
"""


class Bird:
    all_birds = []
    genus = 'avian'

    @classmethod
    def get_genus(cls):
        return cls.genus

    @classmethod
    def all_names(cls):
        return [b.name for b in cls.all_birds]
    
    @classmethod
    def all_species(cls):
        return [b.species for b in cls.all_birds]

    def __init__(self, name='hihi', species=''):
        self.name = name
        self.is_pretty = True
        Bird.all_birds.append(self)

    @property
    def is_pretty(self):
        return self._is_pretty
    
    @is_pretty.setter
    def is_pretty(self, new_val):
        self._is_pretty = bool(new_val)

    @property
    def name(self):  # getter (get_name)
        return self._name

    @name.setter
    def name(self, new_name): # setter (get_name)
        if len(new_name) > 0:
            self._name = new_name
        else:
            raise Exception('invalid name')


if __name__ == '__main__':
    Bird()
    Bird(name='joe')
    Bird(name='tweety')