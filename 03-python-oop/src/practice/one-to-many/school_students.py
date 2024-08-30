"""
Create two classes, School and Student

One school has many students, one student belongs to only one school. Build
out the one-to-many relationship.

Student
- should have an attribute 'name'
- should have an attribute 'gpa'
    - write a getter and setter for gpa
    - validate the it is a number between 0.0 and 4.0
- should have an attribute 'school' that is a School object

School
- should have an attribute 'name'
    - write a getter and setter for name
    - validate that name is not empty
- should have a function get_students()
    - returns a list of all student objects that attend that school
- should have a function get_average_gpa()
    - returns the average gpa of all students at the school
- should have a function get_validictorian()
    - returns the student with the highest gpa at the school
"""

class School:
    pass

class Student:
    pass
