# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком




from functools import reduce

def create_num_name_cort(name, num):
    result = list(zip(num, [i.upper() for i in name]))
    return result

def filter_points_name_cort(name, num):
    result = [reduce(lambda x, y: x + ord(y), i, 0) for i in name]
    print(f'Список очков: {result}')
    result = [(result[i], name[i]) for i in range(len(num)) if result[i] % num[i] == 0]
    return result

name_lang = ['PYTHON', 'C#']
serial_num = [i + 1 for i in range(0, len(name_lang))]

print(f'Исходный список: {create_num_name_cort(name_lang, serial_num)}')
print(f'Cписок, отвечающий условию : {filter_points_name_cort(name_lang, serial_num)}')
