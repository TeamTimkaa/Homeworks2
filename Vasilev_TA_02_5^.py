'''
Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). 
Найти и напечатать координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный. 
Вычисления оформить в виде процедуры.
'''
from math import atan2
from random import randint

def f(x1, x2, y1, y2, z1, z2):
    ang_x = atan2(x2, x1)
    ang_y = atan2(y2, y1)
    ang_z = atan2(z2, z1)
    min_ang = min(ang_x, ang_y, ang_z)
    if min_ang == ang_x: return x1, x2
    elif min_ang == ang_y: return y1, y2
    else: return z1, z2

# Задаем случайные координаты трех точек
x1, x2 = randint(1, 10), randint(1, 10)
y1, y2 = randint(1, 10), randint(1, 10)
z1, z2 = randint(1, 10), randint(1, 10)
print('x1, x2 =', x1, x2,'\ny1, y2 =', y1, y2,'\nz1, z2 =', z1, z2)

# Задаем координаты трех точек
# x1, x2 = 1, 2
# y1, y2 = 5, 8
# z1, z2 = 9, 3

print("Координаты точки с минимальным углом:", f(x1, x2, y1, y2, z1, z2))


'''
Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром, т. е. читается одинаково слева направо и справа налево.
'''
def prostoe(n):
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                return False
                break
            else:
                return True

def bin_code(n):
    bin_n = bin(n)[2:]
    return bin_n == bin_n[::-1]

def final(n):
    for i in range(2, n + 1):
        bin_n = bin(i)[2:]
        if prostoe(i) and bin_code(i):
            print(i, ' bin:', bin_n)

n = int(input('Введите значение n.\n'))
print('Простых натуральных чисел, не превосходящих', n, 'являющиеся палиндромами в bin.')
final(n)

# Код ниже работает, но при n > 10000 считает очень долго, слишком много циклов в цикле
'''s = []
x = 0
n = int(input('Введите n.\n'))
print('Список палиндромов с их двоичным кодом.')
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0: break
        else:
            x = bin(i)[2:]
            if str(x) == str(x)[::-1] and x not in s:
                s.append(x)
for i in s:
    print('Число:', int(i, 2), 'Его двочная запись:', i)'''