f=int(input("Введите количество чисел для последовательности Фибоначчи: "))
a, b = 1, 1
print(a, b, end=" ")
for k in range(f-2):
    a, b= b, a+b
    print(b, end=" ")