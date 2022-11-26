# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

def product(n: int) -> list:
    factorial = [1]
    for i in range(2, n+1):                               # диапазон от 2 до числа+1
        factorial.append(factorial[-1] * i)               # Заносим в факториал 1* каждое число 1*(-2...)
    return factorial

n = int(input('Введите число: '))
factorial = product(n)
print(factorial)