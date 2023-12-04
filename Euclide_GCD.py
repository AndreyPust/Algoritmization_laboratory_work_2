#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Импортирование модуля времени
import time

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


# Начало отсчета
start = time.time()
print("НОД чисел a и b =", euclide_gcd(number_a, number_b))
# Конец отсчета
end = time.time()
print("Время выполнения алгоритма:", (end - start), "сек.")
