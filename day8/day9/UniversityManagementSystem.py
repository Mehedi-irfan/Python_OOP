class UniversityMember:
    universityName = "Nanjing University"

    def __init__(self, name, member_id, email):
        self.name = name
        self.member_id = member_id
        self.email = email
        self.is_active = True

    @classmethod
    def changeUniversityName(cls, new_name):
        cls.universityName = new_name
        return f"University Name is :- {new_name}"

    @staticmethod
    def isValidEmail(email):
        return "@" in email and "." in email and len(email) > 5

    def deactivate(self):
        self.is_active = False
        return f"{self.name} Deactivate"

    def activate(self):
        self.is_active = True
        return f"{self.name} Activated"

    def get_info(self):
        status = "Active" if self.is_active else "Inactive"
        return f"{self.name} and Id Number is {self.member_id} - {status}"


university = UniversityMember("irfan", 4572, "mehediirfan@gamil.com")
print(university.get_info())
print(
    university.changeUniversityName(
        "Nanjing University Of Information Science and Technology"
    )
)
print(university.isValidEmail("Mehediirfan99@gmail.com"))
print(university.activate())
print(university.get_info())


class Student(UniversityMember):
    def __init__(self, name, studentId, email, department, cgpa=0.0):
        super().__init__(name, studentId, email)
        self.department = department
        self.cgpa = cgpa
        self.enrolledCourse = []

    @staticmethod
    def is_valid_cgpa(cgpa):
        return 0.0 <= cgpa <= 4.00

    # course enrolled method
    def enrolledCourse(self, course):
        self.enrolledCourse.append(course)
        self.enrolledStudent.append(self)
        return f"{self.name} he enrolled {course.course_name}"
