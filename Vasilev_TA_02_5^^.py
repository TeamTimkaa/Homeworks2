'''
I need a wristband. Help me in identifying an actual wristband.
A wristband can have 4 patterns:
horizontal: each item in a row is identical.
vertical: each item in each column is identical.
diagonal left: each item is identical to the one on it's upper left or bottom right.
diagonal right: each item is identical to the one on it's upper right or bottom left.
Write a function that returns True if the section can be correctly classified into one of the 4 types, and False otherwise.
Examples
Part of horizontal wristband
is_wristband([
  ["A", "A"],
  ["B", "B"],
  ["C", "C"]
]) # True 
Part of vertical wristband
is_wristband([
  ["A", "B"],
  ["A", "B"],
  ["A", "B"]
]) # True 
Part of diagonal left wristband
is_wristband([
  ["A", "B", "C"],
  ["C", "A", "B"],
  ["B", "C", "A"],
  ["A", "B", "C"]
]) # True
Part of diagonal right wristband
is_wristband([
  ["A", "B", "C"],
  ["B", "C", "A"],
  ["C", "A", "B"],
  ["A", "B", "A"]
]) # True
'''
def is_horizontal(section):
    # Проверяем, что каждая строка идентична
    return all(row == section[0] for row in section)

def is_vertical(section):
    # Проверка по вертикали
    return all(col == [section[i][0] for i in range(len(section))] for col in section[0])

def is_diagonal_left(section):
    # Проверка по левой диагонали
    return all(section[i][j] == section[i-1][j-1] for i in range(1, len(section)) for j in range(1, len(section[0])))

def is_diagonal_right(section):
    # Проверка по правой диагонали
    return all(section[i][j] == section[i-1][j+1] for i in range(1, len(section)) for j in range(len(section[0]) - 2))

def is_wristband(section):
    if is_horizontal(section): return True
    if is_vertical(section): return True
    if is_diagonal_left(section): return True
    if is_diagonal_right(section): return True
    return False


# Проверка
print(is_wristband([["A", "A"], ["B", "B"], ["C", "C"]]))  # Проверка на горизонтальном примере из дано
print(is_wristband([["A", "B"], ["A", "B"], ["A", "B"]]))  # Проверка на вертикальном примере из дано
print(is_wristband([["A", "B", "C"], ["C", "A", "B"], ["B", "C", "A"], ["A", "B", "C"]]))  # Проверка на примере диагоналей слева из дано
print(is_wristband([["A", "B", "C"], ["B", "C", "A"], ["C", "A", "B"], ["A", "B", "A"]]))  # Проверка на примере даигоналей справа из дано