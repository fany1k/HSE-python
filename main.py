def IsPointInSquare(x, y):
    return abs(x) + abs(y) <= 1


def IsPointInCircle(x, y, xc, yc, r):
    if (xc - r <= x <= xc + r) and (yc - r <= y <= yc + r):
        return (x - xc)**2 + (y - yc)**2 <= r**2


def IsPointInArea(x, y):
    return ((y >= -x) and (y >= 2 * x + 2) and
            ((x + 1)**2 + (y - 1) ** 2) <= 4) or\
           ((y <= -x) and (y <= 2 * x + 2) and
            ((x + 1)**2 + (y - 1) ** 2) >= 4)


def xor(x, y):
    return x + y == 1


def MinDivision(n):
    i = 2
    while n % i != 0:
        i += 1
        if i > n**0.5:
            return n
    return i


def IsPrime(n):
    if n == 2 or n == 3:
        return True
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input())
print('YES' if IsPrime(n) else 'NO')
