while True:
    numb = input("Введите целое число: ")
    if numb.isdigit():
        numb = int(numb)
        break
    else :
        print("Неверный ввод")
        


def find_divident(divident):
    print("Результат:", end = " ")
    for i in range(divident, 0, -1):
        if (divident % i == 0):
            print(i, end = " ")
            
find_divident(numb)
