'''
3.Вовочка подготовил одно очень важное письмо, но везде указал неправильное время.
Поэтому нужно заменить все вхождения времени на строку (TBD). Время — это строка вида HH:MM:SS или HH:MM, в которой HH — число от 00 до 23, а MM и SS — число от 00 до 59. 
**ВВОД:** Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. 
**ВЫВОД**: Уважаемые! Если вы к (TBD) не вернёте чемодан, то уже в (TBD) я за себя не отвечаю.
'''
from re import sub

string = input('\nВведите пустую строку (Enter), если хотите оставить образец.\nВведите строку: ')
if string == '':
    string = 'Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю.'
print('\nИсходная строка:', string)
string = sub(r'\d{2}:\d{2}(:\d{2})?', 'TBD', string)
print('Строка после изменений:', string)

'''
4. Владимир устроился на работу в одно очень важное место. 
И в первом же документе он ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п. 
Тогда он решил собрать все аббревиатуры, чтобы потом найти их расшифровки на http://sokr.ru/. Помогите ему.
Будем считать аббревиатурой слова только лишь из заглавных букв (как минимум из двух). 
Если несколько таких слов разделены пробелами, то они считаются одной аббревиатурой.
'''
from re import findall

string = input('\nВведите пустую строку (Enter), если хотите оставить образец.\nВведите строку: ')
if string == '':
    string = 'И в первом же документе он ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п. '
print('\nИсходная строка:', string)
abbreviations = findall(r'\b[ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ]{2,}(?:\s+[ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ]{2,})*\b', string)
print('Все абревеатуры из строки:', abbreviations)