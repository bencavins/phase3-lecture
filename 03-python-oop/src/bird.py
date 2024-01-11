"""
Write a Bird class that lets us:
- Store the bird's name as a string called 'name'
- Store the bird's type as a string called 'type' (for example, 'goose', 'swallow', 'robin', etc)
"""

class Bird:
    def __init__(self, name, type):
        self.name = name  # calls the setter
        self.type = type

    @property  # name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) == 0:
            raise ValueError("Name cannot be zero chars")
        else:
            self._name = new_name
    
    def __repr__(self):
        """
        Needs to return a string.
        This string will be what is printed when the obj is printed
        """
        return f"<Bird {self.name} {self.type}>"
    

if __name__ == '__main__':
    bird = Bird('tweety', 'canary')
    print(bird.name)
