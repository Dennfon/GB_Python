"""
Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
"""

days = int(input("Введите количество дней: "))
num = 0
count = 0
max = 0
while num < days:
    temp = int(input("Введите значение температуры: "))
    if temp > 0:
         count+=1
    elif temp<=0:
         max = count
         count=0
    num+=1
if count > max:
    max = count
print(max)

"""
def daily_temperature_iput(n_days):
    temperaturs = []
    i = 0
    while i < n_days:
        temperaturs.append(int(input(f'Введите температуру день {i + 1} ->')))
        i += 1
    return temperaturs


def longest_temperature_show(daily_temperature):
    current = []
    max = current
    for i in daily_temperature:
        if i > 0:
            current.append(i)
        else:
            current = []
    if len(current) > len(max):
        max = current
    return len(max)


n = daily_temperature_iput(int(input('Введите число дней ->')))
print(longest_temperature_show(n))
"""

"""
import random

def count_plus_day(all_count_day):
    count_day = 0
    max_day = count_day
    for i in range(all_count_day):
        grad_day = random.randrange(-50,50)
        print(grad_day, end = " ")
        if grad_day < 1:
            if max_day < count_day:
                max_day = count_day
            count_day = 0
        else:
            count_day += 1
    if max_day < count_day:
        max_day = count_day
    print(end = "\n")
    return max_day


try:
    number = int(input("Введите общее кол-во дней: "))

    print(count_plus_day(number))
except:
    print("Ввели неверные данные")
"""