"""
One-to-one Relationship
Person <-> ContactInfo
"""


class Person:
    def __init__(self, name, age, phone):
        from contact_info import ContactInfo
        self.name = name
        self.age = age
        self.contact_info = ContactInfo(phone, self)

    def get_info(self):
        return f"name={self.name} age={self.age} phone={self.contact_info.phone}"

    def __repr__(self):
        return f"<Person name={self.name} age={self.age}>"


if __name__ == '__main__':
    p1 = Person('joe', 33, '555-555-5555')
