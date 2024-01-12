class Blog:
    def __init__(self, title):
        self.title = title
        self.comments = []  # array of Comment objects
    
    def __repr__(self) -> str:
        return f'<Blog {self.title}>'

class User:
    def __init__(self, username):
        self.username = username
        self.comments = []  # array of Comments objects

    def __repr__(self) -> str:
        return f'<User {self.username}>'

class Comment:
    def __init__(self, text, blog, user):
        self.text = text
        self.blog = blog  # this comment is for one and only one Blog
        self.user = user  # this comment is for one and only one User

        self.blog.comments.append(self)  # link this comment to blog
        self.user.comments.append(self)  # link this comment to user

    def __repr__(self) -> str:
        return f'<Comment {self.text}>'


if __name__ == '__main__':
    blog1 = Blog('Python 101')
    user1 = User('joe123')
    user2 = User('andy7777')
    comment1 = Comment('luv it', blog1, user1)
    comment2 = Comment('h8 it', blog1, user2)

    # the blog can access all User objects (who commented)
    for comment in blog1.comments:
        print(comment.user)
    
    # the user can access all the Blog object (that they wrote a comment for)
    for comment in user1.comments:
        print(comment.blog)

    print(dir(blog1))