try:
    f = open("predmety.txt", "r", encoding='utf-8')

    m = {}

    for line in f:
        l = line.split()
        subject = l[0]
        l.pop(0)
        sum = 0;
        for i in l:
            t,trash = i.split('(')
            
            sum +=int(t)
        m[subject] = sum
        
    print (m)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f.close()