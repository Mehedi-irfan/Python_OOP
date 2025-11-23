def even_gen(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i


for num in even_gen(10):
    print(num)
# print(next(even_gen(10)))
