students = {"Math": 90, "English": 85, "AI": 95}
for x, y in students.items():
    print(f"{x}:{y}")

averageMark = sum(students.values()) / len(students)
print(f"averageMark {averageMark}")
highestScore = max(students, key=students.get)
print(f"Highest Score :- {highestScore}")
