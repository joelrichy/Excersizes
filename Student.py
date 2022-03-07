class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

        def get_grade(self):
            return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    #method to add students to a course
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True # to confirm student added
        return False # when student not added


    def get_average(self):
        total = 0
        for student in self.students


# main routine
# instanciate 3 student objects

s1 = Student("Tim", 19, 95)
s2 = Student("Bell", 19, 75)
s3 = Student("Caleb", 19, 65)

course1 = Course("Computer Science", 2)
