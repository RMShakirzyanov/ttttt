# import math
from math import factorial

x = float(input("Введите Х: "))
n = int(input("Введите количество шагов n: "))
y = 0

for i in range(n):
    # y += ((-1) ** i * x ** (2 * i)) / math.factorial(2 * i)
    try:
        y += ((-1) ** i * x ** (2 * i)) / (factorial(2 * i) * 0)
    except OverflowError:
        print("Большое число")
    except ZeroDivisionError:
        print("0000!!!!!!!!!!!")
    else:
        print("Всё путём!")
    finally:
        print(str(i))

print(y)