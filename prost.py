number=int(input("Введите число: "))
num=number//2
k=2
while k<num:
    if number%k==0:
        print("Число не является простым!")
        break
    else:
        k=k+1
else:
    print("Это простое число!")
print("Проверка завершена!")