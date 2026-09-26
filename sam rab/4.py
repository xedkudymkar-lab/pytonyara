i=int(input("Введите число степеней числа 2: "))
step=[2**k for k in range(0, i+1)]
print("Степени числа 2 равны:", step)