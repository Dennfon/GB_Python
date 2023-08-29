"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""

def give_out_unique_numbers_of_sets(n,m):
    list1 = []
    for i in range(n):
     list1.append(int(input("Введите число N -> ")))

    list2 = []
    for j in range(m):
     list2.append(int(input("Введите число M -> ")))
    set1 = set(list1)
    set2 = set(list2)
    res = set1.intersection(set2)
    return res

n = int(input("Введите количество чисел первого множества N: "))
m = int(input("Введите количество чисел второго множества M: "))

print(give_out_unique_numbers_of_sets(n,m))