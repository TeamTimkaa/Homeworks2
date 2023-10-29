'''
In some countries of former Soviet Union there was a belief about lucky tickets. 
A transport ticket of any sort was believed to posess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half. 
Here are examples of such numbers:

003111    #             3 = 1 + 1 + 1
813372    #     8 + 1 + 3 = 3 + 7 + 2
17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number when adding the halves.
56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
Such tickets were either eaten after being used or collected for bragging rights.

Your task is to write a funtion luck_check(str), which returns true/True if argument is string decimal representation of a lucky ticket number, or false/False for all other numbers. 
It should throw errors for empty strings or strings which don't represent a decimal number.
'''
# По умолчанию программа будет выдавать ошибки, т.к. стоит проверка на не подходящие строки
# А внизу две проверки с пустой и буквенной строками
def luck_check(number_str):
    # Проверка на пустую строку и наличие только цифр
    if not number_str or not number_str.isdigit():
        raise ValueError('Строка должна содержать только цифры и не быть пустой')

    middle = len(number_str) // 2

    # Разделение строки на две половины
    left_half = number_str[:middle]
    right_half = number_str[-middle:]

    # Сумма цифр в левой и правой половинах
    sum_left = sum(map(int, left_half))
    sum_right = sum(map(int, right_half))

    return sum_left == sum_right

# print(luck_check(input('Введите число: ')))

# Проверки на примерах из дано
print('Дана строка: 003111. Ответ функции:',luck_check("003111"))    
print('Дана строка: 813372. Ответ функции:',luck_check("813372"))     
print('Дана строка: 17935. Ответ функции:',luck_check("17935"))     
print('Дана строка: 56328116. Ответ функции:',luck_check("56328116"))   
print('Дана строка: 123. Ответ функции:',luck_check("12345"))      
print('Дана строка: 123857. Ответ функции:',luck_check("1234567"))    
print('Дана строка: "". Ответ функции:',luck_check(""))           
print('Дана строка: abc123. Ответ функции:',luck_check("abc123"))     