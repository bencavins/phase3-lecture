class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def get_all_courses(self):
        return [c for c in self.courses]

    def __repr__(self):
        return f"<Student {self.name}>"

if __name__ == '__main__':
    from course import Course
    s1 = Student('joe')
    s2 = Student('jane')
    s3 = Student('ralph')

    math = Course('math')
    cs = Course('computer science')
    
    math.enroll(s1)
    math.enroll(s2)
    cs.enroll(s2)
    cs.enroll(s3)

