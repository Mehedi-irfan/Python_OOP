class SuperCalculator:
    def add(self, *numbers):
        print(f"Adding {len(numbers)} numbers : {numbers}")

        if len(numbers) == 0:
            return 0
        else:
            total = 0
            for num in numbers:
                total += num
            return total


super = SuperCalculator()

print(super.add())
print(super.add(5))
print(super.add(4, 3, 2, 1))
print(super.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 65, 56, 5, 1))
