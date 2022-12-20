# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

namber=input('Введите вещественное число:\n')
result=[]


for i in namber:
    if i == '.':
        continue

    else:
        result+=i
        
summa_namber=sum(list(map(int,(result))))
print(f'-> {summa_namber}')
