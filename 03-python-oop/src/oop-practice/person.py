from datetime import date, datetime

countries = [
    'USA',
    'Canada',
    'Mexico'
]

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    
    @property
    def age(self):
        return date.today().year - self.dob.year
    
    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, new_country):
        if new_country in countries:
            self._country = new_country
        else:
            raise ValueError(f'Invalid country: {new_country}')
        

p = Person('anne', 'USA', datetime(1991, 4, 22))