# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


from random import choice


def polynom_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as n1, \
            open(name_2, "r", encoding="utf-8") as n2:
        first = n1.readlines()
        second = n2.readlines()

        if len(first) == len(second):
            with open("sum_poly.txt", "a", encoding="utf-8") as result:
                for i, v in enumerate(first):
                    result.write(f"{v[:-5]} + {second[i]}")
        else:
            print("Error!!!")



polynom_sum("name_1.txt", "name_2.txt")


# Смог сделать лишь конкатенацию,не знаю, то ли имелось ввиду....