import re
values = re.split("[, ]+",input('Введите числа через запятую: '))#.replace(',',' ').split()
lst = values
tup = tuple(lst)
print('Список:', lst)
print('Кортеж:', tup)