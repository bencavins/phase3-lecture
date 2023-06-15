
class ContactInfo:
    def __init__(self, phone, person=None):
        from person import Person
        self.phone = phone
        self.person = person
    
    def __repr__(self):
        return f"<ContactInfo phone={self.phone}>"