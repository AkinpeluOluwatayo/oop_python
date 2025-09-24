class Student:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age


class Course:
    def __init__(self, course_name, max_student):
        self.course_name = course_name
        self.max_student = max_student


    def get_course_name(self):
        return self.course_name

    def get_max_student(self):
        return self.max_student




s = Student('Tayo', "male", 18)
s.set_name("Tosin")
print(s.get_name())

c = Course()

