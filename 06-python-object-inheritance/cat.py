from animal import Animal

class Cat(Animal):
    sound = 'meow'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self) -> str:
        return f"<Cat {self.name} {self.age}>"