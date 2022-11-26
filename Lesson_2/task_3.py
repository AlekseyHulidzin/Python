# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]
import random

count=0
nam=int(input("Namber:"))

rand=[random.randint(-100,100) for i in range(nam)]

for i in range(nam):
    if rand[i]<0 :
        rand.insert(i+1,count)
    if rand[-1]<0:
        rand.append(0)

print(rand)

#ну или такое решение,где в ручную нужно вводить любые числа через пробел
# count=0
# list_1=input('введите числа:').split()

# list_1=[int(i) for i in list_1 ]

# for j in range(len(list_1)-1,-1,-1):
#     if list_1[j]<0:
#         list_1.insert(j+1,count)

# print(list_1)