# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран,
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

number = int(input("Введите число: "))
summa = 0


def func(num):
    return [round((1 + 1 / n) ** n, 2) for n in range(1, number + 1)]


for i in range(1, number + 1):
    summa += round(((1 + 1 / i) ** i), 2)

print(f'Для {number} ->', func(number))
print(f'Сумма последовательности из {number} чисел равна: {summa}')
