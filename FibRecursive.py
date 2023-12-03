import time  # Импортирование модуля времени
print("Введите n-ое число Фибоначчи, которое требуется вычислить:")
n = int(input())


def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


start = time.time()  # Начало отсчета
print(n, "число Фибоначчи =", fib_recursive(n))
end = time.time()  # Конец отсчета

print("Время выполнения алгоритма:", (end - start))
