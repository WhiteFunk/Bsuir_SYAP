while True:
    numb = input("Введите целое число: ")
    if numb.isdigit():
        numb = int(numb)
        break
    else :
        print("Неверный ввод")
        

print("Результат:", end = " ")
for i in range(numb, 0, -1):
    if (numb % i == 0):
        print(i, end = " ")

