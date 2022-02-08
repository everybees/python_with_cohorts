class Student:
    def __init__(self,student_name, student_mark):
        self.student_name = student_name
        self.student_mark = student_mark

    def print(self):
        print('The student name is ' + self.student_name)
        print('The student mark is ' , int(self.student_mark))


students = Student('Jack', 60)
students.print()
judith = Student('Judith', 90)
judith.print()


class NewStudent:
    def __init__(self, student_id,student_name ):
        self.student_name = student_name
        self.student_id = student_id


student_data = NewStudent(1,"Inc")
print(student_data.__dict__)
student_data.__setattr__("student_class", "Cohort 1")
print(student_data.__dict__)
student_data.__delattr__("student_name")
print(student_data.__dict__)