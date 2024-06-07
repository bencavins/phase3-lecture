class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def books(self):
        """Gets all of the books written by this author"""
        result = []
        for book in Book.all:
            if book.author is self:
                result.append(book)
        return result

    def get_best_seller(self):
        """Returns the book with the most sales"""
        max_book = self.books[0]
        for book in self.books:
            if book.sales > max_book.sales:
                max_book = book
        return max_book

    def get_total_sales(self):
        """Returns the sum of all sales for this author"""
        total = 0
        for book in self.books:
            total += book.sales
        return total
    
    def print_books(self):
        for book in self.books:
            print(book)

    def __repr__(self):
        return f"<Author {self.name}>"

class Book:
    all = []

    def __init__(self, title, author, sales=0):
        self.title = title
        self.author = author  # this is an Author object
        self.sales = sales
        Book.all.append(self)
    
    def add_sales(self, num):
        """Should add `num` to the sales for this book"""
        # self.sales = self.sales + num
        if num > 0:
            self.sales += num
        else:
            raise ValueError('num must be positive')

    def __repr__(self):
        return f"<Book {self.title} by {self.author.name}>"
    


author = Author('Stephen King')
a2 = Author('Jane Austin')

b1 = Book('The Shining', author, 50)
b2 = Book('Christine', author, 110)
b3 = Book('Pride and Prejudice', a2)

print(author.get_total_sales())
