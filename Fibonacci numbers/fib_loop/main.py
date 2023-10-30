def fib(n):
    if n <= 0:
        return
    elif n == 1:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b
n = int(input("Введите номер числа Фибоначчи: "))
result = fib(n)
print(f"Значение: {result}")