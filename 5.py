my_dict = {"брошь": ["Золото", 200, 2], "колье": ["Золото", 500, 1], "кольцо": ["Серебро", 300, 20], "серьги": ["Золото", 550, 1]}
keys = list(my_dict.keys())

while True:
    print("""
1. Просмотр описания: название – описание
2. Просмотр цены: название – цена.
3. Просмотр количества: название – количество.
4. Всю информацию.
5. Покупка
6. До свидания""")
    
    choice = int(input())
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
        amount = int(input("Сколько вы хотели бы купить: "))
        if my_dict.get(to_buy)[2] < amount:
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
    elif choice == 6:
        print("До свидания")
        break        
    