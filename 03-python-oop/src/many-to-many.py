class User:
    def __init__(self, name):
        self.name = name

    @property
    def reviews(self):
        result = []
        for review in Review.all:
            if review.user is self:
                result.append(review)
        return result
    
    def get_products(self):
        products = []
        for review in self.reviews:
            products.append(review.product)
        return products

    def __repr__(self):
        return f'<User {self.name}>'


class Review:
    all = []

    def __init__(self, text, rating, user=None, product=None):
        self.text = text
        self.rating = rating
        self.user = user
        self.product = product
        Review.all.append(self)

    def __repr__(self):
        return f'<Review user:{self.user.name}: "{self.text}" {self.rating}/5>'

        
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def reviews(self):
        result = []
        for review in Review.all:
            if review.product is self:
                result.append(review)
        return result
    
    def get_users(self):
        users = []
        for review in self.reviews:
            users.append(review.user)
        return users
    
    def get_avg_rating(self):
        total = 0
        count = 0
        for review in self.reviews:
            # if review.rating >= 2 and review.rating <= 4:
            # if 2 <= review.rating <= 4:
            total += review.rating
            count += 1
        return total / count

    def __repr__(self):
        return f'<Product {self.name} ${self.price}>'


u1 = User(name='bob')
u2 = User(name='alice')

p1 = Product(name='laptop', price=599.99)
p2 = Product(name='video game', price=59.99)

r1 = Review(text='great!', rating=5, user=u1, product=p1)
r2 = Review(text='ok', rating=3, user=u1, product=p2)
r3 = Review(text='bad', rating=1, user=u2, product=p2)