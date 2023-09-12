string = input('Введите строку: ')
words = string.split(' ')
max_len = 0
for x in words:
    if len(x) % 2 == 0:
        print(x, end = ' ')
    if len(x) > max_len:
        max_len = len(x)
        max_word = x
print("\nМаксимальное слово: ", max_word, " длинной: ",max_len)
