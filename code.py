num1 = float(input("first number :-"))
num2 = float(input("second number :-"))

print(f"sum of two numbers :- {num1 + num2}")
avarages = (num1 + num2) / 2
print(f"avarage number :- {round(avarages, 2)}")

if num1 > num2:
    print("NUmber1 is grater")
else:
    print("number2 is grater")
