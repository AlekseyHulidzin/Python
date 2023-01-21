# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


count = 150

def player_turn(player: str):
    global count
    print(f'На столе лежит {count} конфет')
    while True:
        player_take = int(input(f'{player} игрок введите число конфет: '))
        if 0<player_take<=28:
            break
        print('Брать надо от 1 до 28 конфет')
    count -= player_take
    if count <= 0:
        print(f'{player} игрок победил')
        return True
    return False

def CPU_turn():
    global count
    print(f'На столе лежит {count} конфет')
    if count <= 28:
        cpu_take = count
    elif (count-29)%28 == 0:
        cpu_take = 28
    else:
        cpu_take = (count-29)%28
    print(f'Бот взял {cpu_take} конфет')
    count -= cpu_take
    if count <= 0:
        print(f'Бот победил')
        return True
    return False

while True:
    if player_turn('Первый'):
        break
    if CPU_turn():
        break