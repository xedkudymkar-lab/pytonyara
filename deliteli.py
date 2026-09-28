number=int(input("Введите число: "))
print("Делится на", 1)
k=1
while k<number//2:
    k=k+1
    if number%k!=0:
        continue
    print("Делится на ", k)
print("Делится на ", number)