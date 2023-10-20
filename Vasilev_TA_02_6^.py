
'''
1.Дан двумерный массив размером 3x3. 
Определить максимальное значение среди элементов третьего столбца массива; максимальное значение среди элементов второй строки массива. 
Вывести полученные значения.
'''
from random import randint
# Генерация рандомной матрицы
n = 3
max_a = 0
max_b = 0
arr = []
for i in range(n):
  brr = []
  for i in range(n):
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
m,n = int(input()), int(input())
arr = []
for i in range(n):
  brr = []
  for i in range(m):
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
3. Дана целая квадратная матрица n-го порядка. 
Определить, является ли она магическим квадратом, т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.
'''
# from random import randint ранее импортировал

# Генерация рандомной матрицы
n = 3
max_a = 0
max_b = 0
arr = []
for i in range(n):
  brr = []
  for i in range(n):
    brr.append(randint(0,9))
  arr.append(brr)
