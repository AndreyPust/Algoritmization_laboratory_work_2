import time  # Импортирование модуля времени
print("Введите число а:")
number_a = int(input())
print("Введите число b:")
number_b = int(input())


def naive_gcd(a, b):
    gcd = 1
    for d in range(2, max(a, b)):
        if a % d == 0 and b % d == 0:
            gcd = d
    return gcd


start = time.time()  # Начало отсчета
print("НОД чисел a и b =", naive_gcd(number_a, number_b))
end = time.time()  # Конец отсчета

print("Время выполнения алгоритма:", (end - start), "сек.")
