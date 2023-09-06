"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

На входе : [ 1, 5, 88, 100, 2, -4]
33
200
Ответ: [2, 3]
"""
import random

k = int(input('Введите количество элементов списка: '))
min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))

def index_of_array_elements (k, min, max):

    list = []
    for i in range(k):
      number = random.randint(-10, 10)
      list.append(number)
      print(number, end= " ")

    list_ind = []
    for j in range(k): 
        if min <= list[j] <= max:
            list_ind.append(j)
    return list_ind

print(f'\n {index_of_array_elements(k, min, max)}')