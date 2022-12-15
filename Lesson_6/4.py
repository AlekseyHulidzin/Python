# 4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна
import random

def sum_up_odd_numbers():
    size = int(input("Длинна списка: "))
    lst = [random.randint(0, 10) for i in range(size)]
    print(*lst)
    sum_up = 0

    for num in range(len(lst)):
        if num %2 == 0:
            sum_up+=lst[num]

    print(sum_up)

sum_up_odd_numbers()
