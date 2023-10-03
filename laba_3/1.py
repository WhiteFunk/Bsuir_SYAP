import re

f1 = open('f1.txt', 'w')

while(True):
    i = input("Your line: ")+'\n'
    if i=="\n":
        break 
    f1.write(i)

f1.close() 

reg = "[0-9]"
pattern = re.compile(reg)


f2 = open('f2.txt', 'w')
f1_r = open("f1.txt", "r")

for line in f1_r:
    print (line, " - ", pattern.search(line) is None)
    if pattern.search(line) is None:
        f2.write(line)