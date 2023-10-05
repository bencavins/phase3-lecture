class Employee:
    def __init__(self, name, contact_info=None):
        self.name = name
        self.contact_info = contact_info

class ContactInfo:
    def __init__(self, phone, employee=None):
        self.phone = phone
        self.employee = employee

e = Employee('joe', ContactInfo('555-555-5555'))
# ci = ContactInfo('555-555-5555')

# e.contact_info = ci
# ci.employee = e


def builder(employee_name, phone):
    # build objects
    e = Employee(employee_name)
    ci = ContactInfo(phone)

    # link them
    e.contact_info = ci
    ci.employee = e

    # return them
    return e, ci


my_employee, my_contact = builder('joe', '555-555-5555')
print(my_employee.name, my_employee.contact_info.phone)
e, ci = builder('sam', '999-555-5555')
print(e, ci)