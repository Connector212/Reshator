# Импорты
from math import sqrt
# Основные переменные
MENU_TEXT = """1. Решение линейных уравнений
2. Решение квадратных уравнений
3. Построение арифметической прогрессии
4. Арифметические операции с дробями"""
# Первый вывод меню
print("Приветствуем! Это решатор, который поможет вам с некоторыми математическими задачами")
print("Мы можем помочь вам со следующими пунктами:")
print(MENU_TEXT)
print("Введите номер интересующего вас пункта")
user_chose = input()
# Ключевой цикл
while user_chose != '0':  
    if user_chose == '1':
        print("Общий вид линейного уравнения: ax + b = 0")
        print("Введите значения коэффициентов a и b через пробел")
        a, b = map(float, input().split())
        x = -b / a
        print(f"Ответ: x = {x}")
    elif user_chose == '2':
        print("Общий вид квадратного уравнения: ax^2 + bx + c = 0")
        print("Введите значения коэффициентов a, b и c через пробел")
        a, b, c = map(float, input().split())
        d = b**2 - 4 * a * c
        if d < 0:
            print("Данное уравнение не имеет решений")
        elif d == 0:
            x = -b / (2 * a)
            print(f"Ответ: x = {x}")
        else:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            print(f"Ответ: x1 = {x1}, x2 = {x2}")
    elif user_chose == '3':
        print("Введите значение первого элемента прогрессии")
        elem = int(input())
        print("Введите значение разности между соседними элементами")
        step = int(input())
        print("Выберите один из трех пунктов, введя соответствущий номер")
        print("1. Вывести все элементы прогрессии")
        print("2. Вывести номер элемента прогрессии, равного определенному значению")
        print("3. Вывести значение элемента прогрессии под определенным номером")
        user_chose = int(input())
        if user_chose == 1:
            print("Введите количество элементов в прогрессии")
            elements_count = int(input())
            print("Получившая арифметическая прогрессия:")
            for _ in range(elements_count):
                print(elem, end=' ')
                elem += step
            print()
        elif user_chose == 2:
            print("Введите значение элемента прогрессии:")
            value_need = int(input())
            elem_number = 1
            while elem < value_need:
                elem += step
                elem_number += 1
            if elem == value_need:
                print(f"Элемент со значением {value_need} находится под номером {elem_number}"
                )
            else:
                print("Такого элемента нет в прогрессии!")
        elif user_chose == 3:
            print("Введите номер элемента прогрессии:")
            elem_number_need = int(input())
            for _ in range(elem_number_need - 1):
                elem += step
            print(
                f"Элемент под номером {elem_number_need} имеет значение {elem}")
    elif user_chose == '4':
        print("Введите числитель и знаменатель первой дроби через пробел")
        x1, y1 = map(int, input().split())
        print("Введите числитель и знаменатель второй дроби через пробел")
        x2, y2 = map(int, input().split())
        print("Введите номер операции, которую вы хотите применить к данным дробям")
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        user_chose = int(input())
        if user_chose == 1:
            answer_x = x1 * y2 + x2 * y1
            answer_y = y1 * y2
            print(f"{x1}/{y1} + {x2}/{y2} = ", end='')
        elif user_chose == 2:
            answer_x = x1 * y2 - x2 * y1
            answer_y = y1 * y2
            print(f"{x1}/{y1} - {x2}/{y2} = ", end='')
        elif user_chose == 3:
            answer_x = x1 * x2
            answer_y = y1 * y2
            print(f"{x1}/{y1} * {x2}/{y2} = ", end='')
        elif user_chose == 4:
            answer_x = x1 * y2
            answer_y = y1 * x2
            print(f"{x1}/{y1} / {x2}/{y2} = ", end='')
        NOD = abs(answer_x)
        if abs(answer_y) < NOD:
            NOD = abs(answer_y)
        while not (abs(answer_x) % NOD == 0 and abs(answer_y) % NOD == 0):
            NOD -= 1
        answer_x //= NOD
        answer_y //= NOD
        print(f"{answer_x}/{answer_y}")
    else:  
        print("Ну так-то это не цифра пункта... Попробуй ещё раз!")
    print('_' * 87)
    print(MENU_TEXT)
    print("Введите номер интересующего вас пункта или 0, если хотите завершить работу с программой")
    user_chose = input()
print("Благодарим вас за использование нашего сервиса! До встречи!")