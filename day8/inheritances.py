# Create a Person -> Employee -> Manager inheritance chain
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        return f"My name is {self.name} and i am {self.age} years old!"


class Employee(Person):
    def __init__(self, name, age, employee_id, employee_salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.employee_salary = employee_salary

    def work(self):
        return f"MR. {self.name} working so hard."


class Manager(Employee):
    def __init__(self, name, age, employee_id, employee_salary, department):
        super().__init__(name, age, employee_id, employee_salary)
        self.department = department

    def contact_meeting(self):
        return f"{self.name} is conducting a meeting in {self.department} department"

    def work(self):
        return f"{self.name} managing a Team"


manager = Manager("Jhon", 35, "m013", 6500, "accounting")
print(manager.introduction())
print(manager.work())
print(manager.contact_meeting())
