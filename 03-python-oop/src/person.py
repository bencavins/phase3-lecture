# very old school code
p1_name = 'ben'
p1_age = 32

p2_name = 'joe'
p2_age = 22

# next iteration of this problem
p1 = {
    'name': 'ben',
    'age': 32,
    'hobby': 'programming'
}

p2 = {
    'person_name': 'joe',
    'Age': 22
}


# classes are a blueprint for how to build person objects
class Person:
    def __init__(self, first_name_param, last_name_param, age_param=21):  # constructor function
        # build a person object
        self.first_name = first_name_param  # assign attribute 
        self.last_name = last_name_param  # assign attribute
        self.age = age_param
    
    def get_full_name(self, end_char='!'):  # functions in a class are called methods
        return f"{self.first_name} {self.last_name}{end_char}"
    
    def set_age(self, new_age):  # function for setting the name (aka setter function)
        if new_age >= 0:
            self.age = new_age
    
    def __repr__(self):  # this function gets called when we print a string
        return f"<Person {self.get_full_name()} {self.age}>"


# building one person object using our class
my_person = Person('joe', 'smith', 22) # this calls my_persion.__init__()
# print(my_person)  # this calls my_person.__repr__()
# my_person.set_age(-1)
# print(my_person)

another_person = Person('anne', 'doe', 28)


my_persons = [
    Person('joe', 'smith', 22),
    Person('anne', 'doe', 28),
    Person('jane', 'doe', 55),
]

for person in my_persons:
    print(person.get_full_name())