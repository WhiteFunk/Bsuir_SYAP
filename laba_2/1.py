def find_divident(divident):
    print("Результат:", end = " ")
    for i in range(divident, 0, -1):
        if (divident % i == 0):
            print(i, end = " ")
            print(i*-1, end = " ")
            


while True:
    numb = input("Введите целое число: ")
    if numb.lstrip('-').isnumeric():
        numb = int(numb)
        if numb < 0:
            numb *=-1
        break
    else :
        print("Неверный ввод")
        

find_divident(numb)
