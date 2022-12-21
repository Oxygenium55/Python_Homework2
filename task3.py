# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random

list = []

for i in range(10):
    list.append(i)

print(list)

for i in range(9, 0, -1):
    j = random.randint(0, i + 1)
    list[i], list[j] = list[j], list[i]
    
print(list)


