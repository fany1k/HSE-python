import math
a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b != 0:
        print(1, -c / b)
    if b == 0 and c == 0:
        print(3)
    if b == 0 and c != 0:
        print(0)
else:
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print(2, x2, x1) if x1 > x2 else print(2, x1, x2)

    elif discr == 0:
        x = -b / (2 * a)
        print(1, x)
    else:
        print(0)
