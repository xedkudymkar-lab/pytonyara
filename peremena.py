a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))

print("До обмена:")
print(a)
print(b)

a, b= b,a

print("После обмена: ")
print(a)
print(b)