import json

try:
    with open("firms.txt", "r", encoding='utf-8') as firms_f:
        
        m = {}
        sum = 0
        counter = 0
        lst  = []
        
        for line in firms_f:
            l = line.split()
            
            if int(l[2]) > int(l[3]):
                counter +=1
                sum +=int(l[2]) - int(l[3])
                
            
            m[l[0]] = int(l[2]) - int(l[3])
            

    lst.append(m)
    lst.append({"average_profit": sum/counter})
    print (lst)
    json_firms = json.dumps(lst)
    print(json_firms)
except IOError:
    print("Произошла ошибка ввода-вывода!")
