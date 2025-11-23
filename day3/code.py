# Create a set of 5 countries, add one, remove one, print the set.
country = {"bangladesh", "China", "Germany", "Australia", "America", "Italy"}
country.add("Norway")
country.remove("America")
print(country)

"""Given A = {1,2,3,4} and B = {3,4,5,6}, print union, intersection, difference, and symmetric difference."""

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"Union - {A.union(B)}")
print(f"intersection - {A.intersection(B)}")
print(f"difference - {A.difference(B)}")
print(f"symmetric_difference - {A.symmetric_difference(B)}")

# Create a dictionary with your info (name, age, city, university), then print each key and value on a new line.

myself = {"name": "Mehedi", "age": 24, "city": "nanjing", "University": "NUIST"}

for x, y in myself.items():
    print(f"{x}:{y}")

# Create a dictionary of 3 students and their marks, then print the average mark.

students = {"irfan": 90, "tanvir": 89, "roki": 85}

avrageMark = sum(students.values()) / len(students)
print(avrageMark)

# Make two dictionaries and merge them using .update() method.
num1 = {"a": 1, "b": 2, "c": 3}
num2 = {"d": 4, "e": 5, "g": 6}
num1.update(num2)
print(num1)
