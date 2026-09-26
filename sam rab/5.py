i=int(input("Введите число: "))
ostatok=[5*k+3 for k in range(1, i+1)]
print("Прямой порядок чисел -", ostatok)
print("Обратный порядок чисел -", list(reversed(ostatok)))