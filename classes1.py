class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        try:
            return sum(self.marks)/ len(self.marks)
        except ZeroDivisionError:
            return "enter valid input"
        
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super(). __init__(name, school)
        self.salary = salary
    


working_object = WorkingStudent("gunasekhar", "himaja", "250")
print(working_object.name)
print(working_object.average())
print(working_object.salary)

