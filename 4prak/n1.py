import math

x = float(input("Введите число(int): "))

if x < 0:
    x = x * (-1)

print(math.floor(x)+math.ceil(x))