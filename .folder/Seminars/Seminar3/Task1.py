"""
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

n = int(input('Введите количество элементов: '))
list = [int(input('Введите число -> ')) for item in range(n)]
k = int(input('Введите число сдвига: '))
for i in range(k):
     list.insert(0,list.pop())
print(list)