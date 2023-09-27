import random

def input_int(s):
    while True:
        numb = input(s)
        if numb.isdigit():
            numb = int(numb)
            if numb >= 0:
                break
            else:
                print("Неверный ввод")
        else :
            print("Неверный ввод")
    return numb
            
row = input_int("Количество рядов: ")
column = input_int("Количество столбцов: ")

A = [ [0]*column for i in range(row) ]

for i in range(row):
    for j in range(column):
        A[i][j] = random.randint(-10, 10)

for i in range(row):        
    for j in range(column): 
        print(A[i][j], end = ' ')
    print()  



for i in range(row):
    check = False
    for j in range(1,column):
        if A[i][j] < A[i][j-1]:
            check = True
    if check == False:
        left = 0
        right = column -1
        while left < right:
            temp = A[i][left]
            A[i][left] =  A[i][right]
            A[i][right] = temp
            left +=1
            right -=1
        break

for i in range(row):        
    for j in range(column): 
        print(A[i][j], end = ' ')
    print()   
    
