x = float(input())
y = float(input())
epsilon = 10 ** -6
if abs(x - y) < epsilon:
    print('Equal')
else:
    print('Not equal')
