n = int(input())
i = 1
m = -1
if n != 0:
    m = n
    n = int(input())
    if 0 != n != m:
        i += 1
typeOfSubsequence = n > m
maxi = i
while n != 0:
    m = n
    n = int(input())
    if n == 0:
        continue
    if n == m:
        i = 1
        continue
    typeOfPrevSubsequence = typeOfSubsequence
    typeOfSubsequence = n > m
    if typeOfSubsequence == typeOfPrevSubsequence and n != m:
        i += 1
        if i > maxi:
            maxi = i
    else:
        i = 2
print(maxi)
