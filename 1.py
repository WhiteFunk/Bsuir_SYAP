numb = int(input("Введите целое число: "))
print("Результат:", end = " ")
for i in range(numb, 0, -1):
    if (numb % i == 0):
        print(i, end = " ")

