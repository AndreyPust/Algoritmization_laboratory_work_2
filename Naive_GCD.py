#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Импортирование модуля времени
import time

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


# Начало отсчета
start = time.time()
print("НОД чисел a и b =", naive_gcd(number_a, number_b))
# Конец отсчета
end = time.time()
print("Время выполнения алгоритма:", (end - start), "сек.")
