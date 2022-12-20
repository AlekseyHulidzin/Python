# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран,
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

number = int(input("Введите список: "))
sum = 0
d = {3 * i + 1 for i in range(1,number+1)}
print(f"Для n = {number} {d}")

for i in range(1, number + 1):

    sum += (1 + 1 / i) ** i
print(f'Сумма последовательности из {number} чисел равна: {sum}')

def sequence(number):

    return [round((1 + 1 / n)**n, 2) for n in range (1, number + 1)]   

print(f'Для {number} ->',sequence(number))

