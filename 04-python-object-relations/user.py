class User:
    def __init__(self, name):
        self.name = name
        self.reviews = []
    
    def get_all_books(self):
        return [r.book for r in self.reviews]

    def __repr__(self) -> str:
        return f"<User {self.name}>"