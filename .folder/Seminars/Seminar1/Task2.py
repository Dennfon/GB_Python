"""
Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с
«хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер.
Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать невозможно.

Input: 3 4(ввод на разных строках)
Output: 6
"""
train_wagons_that_vitya_got_on = int(input("Введите вагон, в который сел Витя :"))
number_wagons_of_vitya = int(input("Введите номер вагона, в который сел Витя :"))

if train_wagons_that_vitya_got_on != number_wagons_of_vitya:
    print(f"количество вагонов поезда {train_wagons_that_vitya_got_on + number_wagons_of_vitya - 1}")
else:
    print("Без дополнительной информации определить количество вагонов невозможно")