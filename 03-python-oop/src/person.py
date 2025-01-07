p1 = {
    'id': 123,
    'name': 'alice',
    'age': 34
}


# class / object
# class -- blueprint, descriptes what an object looks like
# object -- something that was built using a class
# attribute -- a variable on an object (ex p1.name, p1.age)
# method -- a function on an object (p1.get_full_name())

# getters and setters
# getter -- function responsible for getting data
# setter -- function responsible for setting data

# public attributes -- can be accessed anywhere
# private attributes -- should only be accessed with getter/setter
#   - should start with '_' (ex self._name, self._age, etc)


class Person:
    def __init__(self, id=None, first_name='', last_name='', age=None):  # constructor
        # returns a new Person object
        self.id = id
        self.first_name = first_name
        self._last_name = ''  # this attribute is private!
        self.set_last_name(last_name)  # call our setter
        # self.full_name = first_name + ' ' + last_name
        self.age = age

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, new_last_name):
        # only set the last_name if it is a string
        if isinstance(new_last_name, str):
            self._last_name = new_last_name
    
    def get_full_name(self):
        return self.first_name + ' ' + self._last_name
    
    def __repr__(self):
        return f'<Person id={self.id} name={self.first_name} age={self.age}>'


# calls the Person constructor (__init__)
p1 = Person(
    id=123, 
    first_name='bob', 
    last_name='smith', 
    age=55) # Person.__init__()
p2 = Person(
    id=234, 
    first_name='alice', 
    last_name='jones', 
    age=34)

persons = [p1, p2]
for p in persons:
    print(p.get_full_name())
