class Course:
    def __init__(self, id):
        self.id = id
        self.students = []
    
    def enroll(self, student):
        self.students.append(student)
        student.courses.append(self)
    
    def get_all_students(self):
        return [s for s in self.students]
    
    def __repr__(self):
        return f"<Course {self.id}>"