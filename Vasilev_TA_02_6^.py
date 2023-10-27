
'''
1.Дан двумерный массив размером 3x3. 
Определить максимальное значение среди элементов третьего столбца массива; максимальное значение среди элементов второй строки массива. 
Вывести полученные значения.
'''
from random import randint
# Генерация рандомной матрицы
print('\nЗадание 1.')
n = 3
max_a = 0
max_b = 0
arr = []
for i in range(n):
  brr = []
  for j in range(n):
    brr.append(randint(0,9))
  arr.append(brr)
# Вывод получившегося массива
print('Сгенерированный массив:')
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ',)
    print()
# Нахождение и вывод ответов
for i in range(n):
    if arr[i][2] > max_a:
        max_a = arr[i][2]
print('Максимальное значение среди элементов третьего столбца:', max_a)
for j in range(n):
    if arr[1][j] > max_b:
       max_b = arr[1][j]
print('Максимальное значение среди элементов второй строки:', max_b)


'''
2.Дан двумерный массив размером mxn. 
Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями. 
Вывести оба массива.
'''
# from random import randint ранее импортировал

# Генерация рандомной матрицы m x n.
print('\n\nЗадание 2.')
m,n = int(input('Введтите m.\n')), int(input('Введтите n.\n'))
arr = []
for i in range(n):
  brr = []
  for j in range(m):
    brr.append(randint(-9,9))
  arr.append(brr)
# Вывод получившегося массива
print('Сгенерированный массив:')
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ',)
    print()
# Создание нового массива
for i in range(n):
    for j in range(m):
        if arr[i][j] > 0: arr[i][j] = 1
        else: arr[i][j] = 0
# Вывод нового массива
print('Новый массив:')
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ',)
    print()


'''
3.Дана целая квадратная матрица n-го порядка. 
Определить, является ли она магическим квадратом, т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.
'''
# from random import randint ранее импортировал

print('\n\nЗадание 3.')
n = int(input('Введите n.\n'))
arr = []
# Генерация рандомной матрицы
for i in range(n):
  brr = []
  for j in range(n):
    brr.append(randint(0,9))
  arr.append(brr)
# Вывод массива
print('Сгенерированный массив:')
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ',)
    print()

def func(arr):
    # Проверка строк
    for i in arr:
        if sum(i) != sum(arr[0]):
            return False
    # Проверка столбцов
    for j in range(n):
        if sum(arr[i][j] for i in range(n)) != sum(arr[0]):
            return False
    return True

if func(arr): print('Матрица является магическим квадратом.')
else: print('Матрица не является магическим квадратом.')


'''
4.Определить, является ли заданная целая квадратная матрица n-го порядка симметричной (относительно главной диагонали).
'''

# from random import randint ранее импортировал

print('\n\nЗадание 4.')
n = int(input('Введите n.\n'))
arr = []
flag = 0
# Генерация рандомной матрицы
for i in range(n):
  brr = []
  for j in range(n):
    brr.append(randint(0,9))
  arr.append(brr)
# Вывод массива
print('Сгенерированный массив:')
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ',)
    print()

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i][j] != arr[j][i]:
            flag += 1

if flag == 0: print("Матрица симметрична.")
else: print("Матрица не симметрична.")


'''
5.Дана прямоугольная матрица. 
Найти строку с наибольшей и строку с наименьшей суммой элементов. 
Вывести на печать найденные строки и суммы их элементов.
'''

# from random import randint ранее импортировал

print('\n\nЗадание 5.')
max_sum = 0
min_sum = 10000000
max_row = ''
min_row = ''
# Генератор прямоугольной матрицы
m,n = randint(2,4), randint(5,9)
arr = []
for i in range(n):
  brr = []
  for j in range(m):
    brr.append(randint(0,9))
  arr.append(brr)
# Вывод получившегося массива
print('Сгенерированный массив:')
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ',)
    print()

for i in arr:
  a = sum(i)
  if a > max_sum:
    max_sum = a
    max_row = i
  if a < min_sum:
    min_sum = a
    min_row = i
print('Строка с наименьшей суммой элементов:', min_row)
print('Сумма элементов в ней:', min_sum)
print('Строка с наибольшей суммой элементов:', max_row)
print('Сумма элементов в ней:', max_sum)


'''
6.Дана действительная матрица размером n х m, все элементы которой различны. 
В каждой строке выбирается элемент с наименьшим значением. 
Если число четное, то заменяется нулем, нечетное - единицей. 
Вывести на экран новую матрицу.
'''
# from random import randint ранее импортировал

print('\n\nЗадание 6.')
# Генератор прямоугольной матрицы
m,n = randint(3,4), randint(3,4)
arr = []
ind = 0
for i in range(n):
  brr = []
  for j in range(m):
    brr.append(randint(1,9))
  arr.append(brr)
# Вывод получившегося массива
print('Сгенерированный массив:')
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ',)
    print()

for i in range(n):
    ind = min(arr[i])
    for j in range(m):
        if arr[i][j] == ind:
            if ind % 2 == 0:
                arr[i][j] = 0
            else:
                arr[i][j] = 1

print('Новый массив:')
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ',)
    print()