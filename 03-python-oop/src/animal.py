class Animal:
    sound = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def feed(self):
        print(self.sound, ':)')