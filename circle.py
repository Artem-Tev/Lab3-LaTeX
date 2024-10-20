import math


def area(r):
    '''
    Принимает радиус окружности (int или float).
    Возводит этот радиус в квадарат.
    умножает квадрат радиуса на число пи, получаемое с помощью библиотеки math.
    Параметры:
        r (int или float): радиус окружности
    Возвращаемое значение:
        площадь круга (float)
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус окружности (int или float).
    Умножает радиус на 2, а затем на число пи, получаемое из библиотеки math.
    Параметры:
        r (int или float): радиус окружности
    Возвращаемое значение:
        периметр круга (float)
    '''
    return 2 * math.pi * r

