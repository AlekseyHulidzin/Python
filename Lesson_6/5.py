# Есть список случайных чисел в промежутке от 1 до 200, количеством 200. Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

from random import randint as rnd

input_list = list(map(lambda x:rnd(1,101),range(200)))
print(input_list)
cort_list=[]
for index,elem in enumerate(input_list):
    if index!=elem:
        to_add= index,elem
        cort_list.append(to_add)
        print(cort_list)
    elif index+elem%5:
        print(cort_list)
  