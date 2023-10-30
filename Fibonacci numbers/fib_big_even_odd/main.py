def fib_eo(n):
    if n <= 0:
        return False
    elif n % 3 == 2:
        return True
    else:
        return False
n = int(input("Введите номер числа Фибоначчи: "))
if fib_eo(n):
    print(f"Число Фибоначчи {n} четное(even)")
else:
    print(f"Число Фибоначчи {n} нечетное(odd)")