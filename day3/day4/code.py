# Check whether a number is positive, negative, or zero.
number = 0
if number > 0:
    print("the number is positive")
elif number < 0:
    print("the number is negative")
else:
    print("The number is zero")


# Print all even numbers from 1 to 50.

for x in range(0, 51, 2):

    print(f"even number {x}")

# Write a program that prints the sum of numbers from 1 to n (input n).
number = int(input("take a number :-"))

if number > 0:
    result = number * (number + 1) // 2
    print(result)
else:
    print("Number is 0")


# Use a loop to print a multiplication table for any number.
num = int(input("Take a number for Multiplication "))
print(f"Multiplication table of {num}")

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# Use break and continue in one small example (your own idea).
for x in range(8):
    print(x)
    if x == 3:
        continue
    elif x == 6:
        break
