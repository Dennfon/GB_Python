"""
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
"""
number_of_student = 0

count_of_class = 3

student_of_parts = 2

while count_of_class > 0:
    count = int(input("Введите количество учеников -> "))
    number_of_student = number_of_student + count
    count_of_class = count_of_class - 1

count_parts = number_of_student / student_of_parts  

print(round(f"Всего школе необходимо преобрести {count_parts} парт(у/ы)"))
