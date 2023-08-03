"""
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.
"""

distance_of_day_n = int(input("Введите расстояние, которое машина проезжает за день в км: -> "))
total_distance_m = int(input("Введите общую дистанцию пути в км: -> "))

count_of_days_distance = (total_distance_m + distance_of_day_n) // distance_of_day_n

print(round(f"Автомобиль проедет маршрут за  {count_of_days_distance} днь(я/ей)"))