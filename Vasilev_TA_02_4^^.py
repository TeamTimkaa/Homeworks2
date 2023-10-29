# Вы на паре по моей просьбе выдали другое задание. 
'''
4.Есть папка, в ней лежат n папок. 
Переименовать их в числовом порядке от 1 до n.
'''
from os import * # Импортировал всё, потому что 'from os import path.isdir' не работало

flag = 1 # Для проверки существования каталога
while flag == 1: 
    folder = input('Вставьте путь до каталога с папками: ')
    if path.isdir(folder): #Проверка существования каталога
        flag = 0 
        chdir(folder) # Перенаправление python 3 в каталог для работы с ним
        print('\nРабочий каталог для смены папок:', getcwd())
        # Второй флаг для защиты от случайный переименований
        flag_2 = input('Изменить наименования всех папок в нём по принципу от 1 до n?\nВведите (y/n): ') 
        if flag_2 == 'n':
            print('Изменения отменены.')
        if flag_2 == 'y':
            arr = listdir(folder)
            # На этом моменте заметил файл .DS_Store, содержащий (насколько я разобрался) параметры каталога, поэтому нужно убрать его из массива
            if '.DS_Store' in arr: 
                arr.remove('.DS_Store')
            for i in range(len(arr)):
                a = str(folder) + '/' + arr[i] # Задаём a = пути до каждой папке
                rename(a, str(i+1))
            print('\nПрограмма завершила работу.')

    else:  
        print('\nУказанный каталог не найден.')