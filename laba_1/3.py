s = input('Введите числа через запятую: ').replace(',',' ').split()

print(s)
try:
    ints = [int(x) for x in s]
except:
    print("Неверный ввод")
    
max_int = 0;
for i in ints:
    if i % 2 == 0:
        if i > max_int:
            max_int = i
if max_int != 0:
    print(max_int)
else:
    print (ints[0])
    
print(sorted(ints, reverse = True))
        
