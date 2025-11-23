class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def isAdult(age):
        return age >= 18

    @staticmethod
    def calculateMarks(marks):
        if marks >= 80:
            return "A+"
        elif marks >= 70:
            return "A"
        else:
            return "B"


print(Student.isAdult(25))
print(Student.calculateMarks(85))
