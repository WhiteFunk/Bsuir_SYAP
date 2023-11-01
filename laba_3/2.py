min = 0;
surname_min = ""

try:
    f = open("Sotrudnyki.txt", "r", encoding='utf-8')

    for worker in f:
        last_name, salary = worker.split()
        salary = int(salary)
        if salary > 2000:
            print(last_name)
        if salary < min or min == 0:
            min = salary
            surname_min = last_name
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f.close()
print (surname_min, " - ", min)