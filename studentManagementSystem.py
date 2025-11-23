# Student Management System তৈরি করুন:
# Student class: name, student_id, marks (list)
# Methods: add_mark(), get_average(), get_grade()
# Class variable: school_name = "ABC School"
# Class method: get_school_info()
class Student:
    schoolName = "ABC School"

    def __init__(self, name, studentId):
        self.name = name
        self.studentId = studentId
        self.marks = []

    def addMarks(self, marks):
        self.marks.append(marks)
        return f"Mark {marks}  added for {self.name}"

    def get_average(self):
        if len(self.marks) == 0:
            return 0
        total = sum(self.marks)
        average = total / len(self.marks)
        return average

    def get_grade(self):
        average = self.get_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    @classmethod
    def get_school_info(cls):
        return f"School Name :- {cls.schoolName}"

    def student_info(self):
        return f" {self.name} ID : {self.studentId} - Average : {self.get_average()} Grade : {self.get_grade()}"


student = Student("Irfan", 202353460028)
student1 = Student("Alvi", 202375485685)

print(f"{student.name} and {student.studentId}")
print(f"{student1.name} and {student1.studentId}")

print(student.addMarks(85))
print(student.addMarks(75))
print(student.addMarks(98))
print(student.addMarks(69))
print(student.addMarks(52))

print(student1.addMarks(82))
print(student1.addMarks(72))
print(student1.addMarks(92))
print(student1.addMarks(62))
print(student1.addMarks(52))

print(f"{student.name} average mark is {student.get_average()}")
print(f"{student1.name} average mark is {student1.get_average()}")

print(f"{student.name} average mark is {student.get_grade()}")
print(f"{student1.name} average mark is {student1.get_grade()}")

print(Student.get_school_info())

print(student.student_info())
print(student1.student_info())
