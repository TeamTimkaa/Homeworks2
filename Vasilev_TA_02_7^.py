# from Python_7 одну простую (1,2,3) и одну сложную(5,6)
'''
2.Выберите любую папку на своем компьютере, имеющую вложенные директории. 
Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
'''
from os import walk, path

def print_docs(directory):
    for root, dirs, files in walk(directory):
        if root == directory:
            print(f'\nПуть до папки: {root}\nЕё содержимое:')
            for file in files:
                print(f'{path.join(file)}')
        else:
            print(f'\nПуть до вложенной папки: {root}\nЕё содержимое:')
            for file in files:
                print(f'{path.join(file)}')

print_docs(input('Вствьте путь до папки, содержимое которой хотите узнать: '))


'''
6.При помощи библиотеки Pillow в директории circles (создайте ее во время выполнения функции) 
нарисуйте и сохраните 100 кругов радиусом 300 пикселей случайных цветов в формате jpg на белом фоне 
(каждый круг - отдельный файл). 
Для этого напишите функцию circles_generator(num_of_circles=100).
'''
# Директорию circles можно не создавать, сделается автоматически
from random import randint
from os import path, makedirs
from PIL import Image, ImageDraw 
# Кстати Pillow у меня установлен, проверял через pip, но pycharm не хочет его импортировать

def circles_generator(num_of_circles=100):
    # Создание папки circles
    if not path.exists('circles'):
        makedirs('circles')

    for i in range(num_of_circles):
        # Создаем новое изображение
        image = Image.new('RGB', (500, 500), 'white') # В описании задачи не указаны размеры холста, поэтому 500х500
        draw = ImageDraw.Draw(image)
        # Генератор случайных цветов
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        # Рисуем круг
        draw.ellipse((100, 100, 400, 400), fill=color)
        # Сохраняем изображение
        name = path.join('circles', f'Круг №{i + 1}.jpg')
        image.save(name, 'JPEG')
    print('Папка успешно создана')
a = input('Сгенерировать папку circules и 100 случайных кругов в ней?\n(y/n): ')
if a == 'y': circles_generator()
else: print('генерация папки с кругами была отменена')
# Примечательно, то что круг нарисован с "помехами" по краям со всех сторон