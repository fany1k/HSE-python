import math
n = int(input())
listOfX = []
summ = 0
while n != 0:
    listOfX.append(n)
    n = int(input())
s = sum(listOfX) / len(listOfX)
x = 0
for i in listOfX:
    x += (i - s) ** 2
sd = math.sqrt(x / (len(listOfX) - 1))
print(sd)
