# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок


text='Пугать ты галок пугай'
print(text)
string=input('Введите слово: ')

text=text.split(' ')


for i in text:
    if i.lower()==string.lower():
        text.remove(i)
print(' '.join(text))