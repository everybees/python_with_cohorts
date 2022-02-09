# 9. Write a python class named student with two attributes student_name, marks.
# Modify the attribute values of the said class and print the ooriginal and modified values of the said attributes.
class Student:
    def __init__(self, student_name, mark):
        self.student_name = student_name
        self.mark = mark

def original_values():
    original = Student("David", 50)

    print(original.student_name)
    print(original.mark)
# original_values()


def modified_values():
    original = Student("Angel", 100)

    print()

    print(original.student_name)
    print(original.mark)
# modified_values()


#10.
class SecondQeustion:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

def new():
    original = SecondQeustion(100, "Michael")
    # print(original.__dict__) to get the result as a dictionary
    original.__dict__.update(student_class = "Jss3", sex = "Male") #to update or add an attribute to a class

    print(original.student_name)
    print(original.student_id)
    print(original.student_class)
    print(original.sex)

new()

# def student_name_removed():
    


    



    


