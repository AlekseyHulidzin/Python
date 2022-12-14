# 2 - Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Не использовать множества.

from typing import List
from random import randint
from for_gb import give_int


def random_list(amount: int) -> List[int]:


    data_list = list()
    for i in range(amount):
        rep = randint(1, amount)
        temp = randint(0, amount)
        for j in range(rep):
            data_list.append(temp)
    return data_list


def find_unique_val(data: List[int]) -> List[int]:
   

    unq_val = []
    for i in data:
        if i not in unq_val:
            unq_val.append(i)
        unq_val = sorted(unq_val)
    return unq_val


num = give_int('Type some natural number: ', 1)
rnd_list = random_list(num)
result = find_unique_val(rnd_list)
print(f'Start list:\n{rnd_list}\nUnique values:\n{result}')