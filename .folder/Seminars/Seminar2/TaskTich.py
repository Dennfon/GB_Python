from random import *
import time

def show_test():
    print(randint(1,10))
    print(time.time())

show_test()
print(show_test())

"""
def show_test(upper: int) -> str :
    print(randint(1,upper))
    print(time.time() )
    return 1234


print(show_test(100))
"""

sp = [55, 111, True, "sssss", [55,77,88] ]

for i in range(len(sp)):
    print(sp[i], end = " ")

print(end = "\n")
for el in sp:
    print(el, end = " ")

print(end = "\n")
for item in enumerate(sp):
    print(item)

print(end = "\n")
print(list(range(1000)))