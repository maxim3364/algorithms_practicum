f1 = 1; f2 = 2
n = int(input())
print(f1, f2, end=' ')
while n > 2:
    f1, f2 = f2, f1 + f2
    print(f1, end=' ')
    n -= 1

