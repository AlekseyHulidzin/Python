# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними 
# в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def input_numbers(x): 
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        reality = False
        while not reality:
            try:
                number = int(input(f"Введите координату {xy[i]}: "))
                a.append(number)
                reality = True
            except ValueError:
                print("Не тот цифра, что после запятой идет. Цифра тот, что без запятых")
    return a


def Length(a, b):  
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)  
    return lengthSegment


print("Введите координаты точки А")
pointA = input_numbers(2)
print("Введите координаты точки В")
pointB = input_numbers(2)

print(f"Длина отрезка: {round(Length(pointA, pointB),2)}")