n=int(input("Введите верхнюю границу суммы чисел: "))
s=0
k=0
while k<n:
    k=k+1
    s=s+k
print("Сумма чисел от 1 до", n, "равна: ", s)

print(sum(list(range(1,n+1))))