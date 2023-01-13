# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



from random import randrange, choice


def Polynom(k, Lesson_4):
    if k > 0:
        with open(Lesson_4, 'a+', encoding='utf-8') as my_file:
            signs = ['+', '-']
            polynom = ''
            for i in range(k, -1, -1):
                koef = randrange(11)
                if i > 1 and koef != 0:
                    polynom += f'{koef}*x^{i} {choice(signs)} '
                elif i > 1 and koef == 0:
                    polynom += ''
                elif i == 1:
                    polynom += f'{koef}*x {choice(signs)} '
                elif i == 0 and koef != 0:
                    polynom += f'{koef} = 0'
                elif i == 0 and koef == 0:
                    polynom += ' = 0'
            my_file.write(polynom + '\n')
        return polynom


for i in range(2):
    Polynom(int(input('Введите число для 1 полинома:\n')),
            'name_1.txt')
    Polynom(int(input('Введите число для 2 полинома:\n')),
            'name_2.txt')


