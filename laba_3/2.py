f = open("Sotrudnyki.txt", "r", encoding='utf-8')

for worker in f:
    last_name, salary = worker.split()
    salary = int(salary)
    if salary > 2000:
        print(last_name)