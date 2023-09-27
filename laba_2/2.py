import re


def some_func(arg):
    if(isinstance(arg,list)):
         i = arg.index(0)
         i2 = arg.index(0, i + 1)
         print(sum(arg[i:i2]))
    elif(isinstance(arg,str)):
        print(re.sub('.',lambda x: r'\u % 04x' % ord(x.group()),arg))
    elif(isinstance(arg,int)):
        sum = 0
        while arg>0:
            if(arg%10%2 == 0):
                sum +=arg%10
            arg //=10
        print(sum) 
    elif(isinstance(arg,tuple)):
        minVal = min(arg)
        maxVal = max(arg) 
        tmp = []
        for i in arg:
            if i == minVal:
                tmp.append(maxVal)
                continue
            if i == maxVal:
                tmp.append(minVal)
                continue
            tmp.append(i)
        print(tmp)


while True:
    print("""
    1. Список
    2. Кортеж
    3. Число
    4. Строка
    5. До свидания""")
    choice = input()
    if choice.isdigit():
        choice = int(choice)
    else :
       continue
    
    
    if choice == 1:
        try:
            values = re.split("[, ]+",input('Введите числа через запятую: '))
            list_of_integers = [int(x) for x in values]
            some_func(list_of_integers)
        except:
            print("Неправильный ввод")
    elif choice == 2:
        try:
            values = tuple(re.split("[, ]+",input('Введите числа через запятую: ')))
            tup = tuple([int(x) for x in values])
            some_func(values)
        except:
            print("Неправильный ввод")
    elif choice == 3:
        bl = True
        while bl:
            value =input("Введите число: ")
            if value.lstrip('-').isdigit():
                value =int(value)
                if value < 0:
                    value *=-1
                bl = False
            else :
                continue
        some_func(value)
    elif choice == 4: 
         value =input("Введите строку: ")
         some_func(value)
    elif choice == 5:
        print("До свидания")
        break        
    else:
        print("Неправильный ввод!!!!")
        
