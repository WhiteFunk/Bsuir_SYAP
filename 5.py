my_dict = {"Брошь": ["Золото", 200, 2], "Колье": ["Золото", 500, 1], "Кольцо": ["Серебро", 300, 20], "Серьги": ["Золото", 550, 1]}
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
        print()
    elif choice == 6:
        break        
    