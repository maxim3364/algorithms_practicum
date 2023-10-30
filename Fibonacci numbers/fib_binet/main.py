import math
def fib(n):
    if n <= 0:
        return "Неверное значение n"
    else:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        fib = (phi**n - psi**n) / sqrt5
        return round(fib)

n = int(input("Введите номер числа Фибоначчи: "))
result = fib(n)
print(f"Число Фибоначчи под номером {n} равно {result}")