a = 5
b = 5.98
c = 'hello'

# Варианты сборки данных для вывода
# print (a,b,c)
# print (a,' - ',b,' - ',c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

#Ввод данных с помощью функции input
print('Введите первую строку')
a = int(input())
#print(a)
print('Введите второе число')
b = int(input())

#Сумма двух чисел (В результате была конкатенация строк)
#print(a, ' + ', b, ' = ', a + b)

#Приведение Типов
c = 5.89
#print(c)

n = int(c) #Приведение к Int
#print(n)

d = str(n) #Приведеник Строке str

print(a, ' + ', b, ' = ', a + b)

a = 5.89
b = 6.55
print(round(a*b,3)) #ограничение вывода дробной части до 3 знаков после запятой

