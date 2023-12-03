import time  # Импортирование модуля времени
print("Введите число а:")
number_a = int(input())
print("Введите число b:")
number_b = int(input())


def euclide_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return euclide_gcd(a % b, b)
    if b >= a:
        return euclide_gcd(a, b % a)


start = time.time()  # Начало отсчета
print("НОД чисел a и b =", euclide_gcd(number_a, number_b))
end = time.time()  # Конец отсчета

print("Время выполнения алгоритма:", (end - start), "сек.")
