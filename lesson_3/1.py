#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

text=input('Введите текст:').split()
result=[int(item) for item in text]         #конвертируем список строк в числа
summ=0
for i in range(1, len (result),2):
    if i%2==1:
        summ+=result[i]
print(summ)

#это если по простому брать уже готовый список
#my_lst = [2, 3, 5, 9, 3]     
#result = []
#for i in range(len(my_lst)):
#    if i % 2 != 0:
#        result.append(my_lst[i])
#summa_el = sum(result)
#print(f'{my_lst} -> на нечётных позициях элементы {result}, ответ: {summa_el}')
