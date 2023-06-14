"""
Write a Bird class that lets us:
- Store the bird's name as a string called 'name'
- Store the bird's type as a string called 'type' (for example, 'goose', 'swallow', 'robin', etc)
"""

class Bird:
    def __init__(self, name):
        self.name = name
        self.is_pretty = True

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