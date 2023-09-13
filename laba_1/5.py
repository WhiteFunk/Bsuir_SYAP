# my_dict = {"брошь": ["Золото", 200, 2], "колье": ["Золото", 500, 1], "кольцо": ["Серебро", 300, 20], "серьги": ["Золото", 550, 1]}

my_dict = {}

i = input("Количество товаров: ")

if i.isdigit():
        i = int(i)
        if i <=0:
            print("Неверный ввод")
            i = 1
else :
        print("Неверный ввод")
        i = 1

for j in range(0,i):
    name = input("Введите название товара: ")
    compound = input("Из чего состоит: ")
    price = input("Цена: ")
    
    if price.isdigit() :
        price = float(price)
        if price <= 0:
            print("Отрицательный или нулевой ввод")
            continue
    else :
        print("Неверный ввод")
        continue
    number = input("Количество: ")
    
    if number.isdigit():
        number = int(number)
        if number < 0:
            print("Отрицательный ввод")
            continue
    else :
        print("Неверный ввод")
        continue
    
    my_dict[name] = [compound,price,number]

keys = list(my_dict.keys())




while True:
    print("""
1. Просмотр описания: название – описание
2. Просмотр цены: название – цена.
3. Просмотр количества: название – количество.
4. Всю информацию.
5. Покупка
6. До свидания""")
    choice = input()
    if choice.isdigit():
        choice = int(choice)
    else :
       continue
    
    
    if choice == 1:
        for i in range(0, len(keys)):
            print(keys[i], " - " ,my_dict.get(keys[i])[0])
    elif choice == 2:
        for i in range(0, len(keys)):
            print(keys[i], " - " ,my_dict.get(keys[i])[1])
    elif choice == 3:
        for i in range(0, len(keys)):
            print(keys[i], " - " ,my_dict.get(keys[i])[2])
    elif choice == 4:
        for i in range(0, len(keys)):
            print(keys[i], " - " ,my_dict.get(keys[i]))
    elif choice == 5:
        to_buy = input("Какое изделие вы хотели бы купить: ").lower()
        if to_buy in keys:
        
            amount = int(input("Сколько вы хотели бы купить: "))
            if my_dict.get(to_buy)[2] < amount or amount <=0:
                print("Покупка не удалась :()")
                continue
            else:
                my_dict.get(to_buy)[2] -= amount 
                print("Покупка совершена!")
                print("Цена: ",my_dict.get(to_buy)[1]*amount)
            number_of_product = 0;
            for i in list(my_dict.values()):
                number_of_product += i[2]
            print(number_of_product, "- столько товаров осталось в изначальном списке")
        
        else:
            print("Товара нет")
    elif choice == 6:
        print("До свидания")
        break        
    else:
        print("Неправильный ввод!!!!")
    