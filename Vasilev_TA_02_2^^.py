# Усложнённое задание №2
# Ссылка на github для получения доп. баллов: https://github.com/TeamTimkaa
'''
Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
Освободившиеся в конце массива элементы заполнить нулями.
'''
from random import randint

# Генератор случайных массивов
arr, len_arr = [], randint(5, 20)
for i in range(len_arr): arr.append(randint(0,100))
print('Сгенерированный массив:', arr)

count = 0
arr_2 = []
a, b = int(input('Введите нижнюю границу интервала.\n')), int(input('Введите верхнюю границу интервала.\n'))
for i in arr:
    if a <= i <= b:
        arr_2.append(i)
        count += 1
for i in arr_2:
    if i in arr:
        arr.pop(arr.index(i))
        arr.append(0)
print('Массив после изменений:', arr)
print('Элементы, заменённые на 0:', arr_2)