"""Write a Python program that:

Asks the user for a number n.

Prints all numbers from 1 to n.

Prints the sum of even numbers and sum of odd numbers separately.

At the end, prints which sum is larger.

💡 Example Output:
Enter a number: 10
Sum of even numbers: 30
Sum of odd numbers: 25
Even numbers sum is greater."""

number = int(input("Take a number: "))

even_sum = 0
odd_sum = 0

print(f"Number of 1 to {number}")
for i in range(1, number + 1):
    print(i, end=" ")
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"Sum of the Even Numbers :- {even_sum}")
print(f"Sum of the Odd Numbers :- {odd_sum}")

# check which one is largest sum
if even_sum > odd_sum:
    print("Even sum is Larger")
elif odd_sum > even_sum:
    print("Odd sum is larger")
else:
    print("Both are same")
