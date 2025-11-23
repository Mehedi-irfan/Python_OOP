numbers = []

for i in range(1, 6):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

print(f"\nNumbers: {numbers}")
print(f"Largest Number: {max(numbers)}")
print(f"Smallest Number: {min(numbers)}")
print(f"Tuple: {tuple(numbers)}")
