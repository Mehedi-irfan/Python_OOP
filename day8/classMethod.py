class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_school_info(cls):
        return f"School name is {cls.school_name}"

    @classmethod
    def get_birth_year(cls, name, birthYear):
        age = 2025 - birthYear
        return cls(name, age)


print(Student.get_school_info())
student2 = Student.get_birth_year("mehedi", 2000)
print(f"{student2.name} and his age is {student2.age}")
