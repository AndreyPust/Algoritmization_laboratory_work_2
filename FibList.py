#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time  # Импортирование модуля времени

print("Введите n-ое число Фибоначчи, которое требуется вычислить:")
n = int(input())


def fib_list(n):
    fib_numbers = [0]*100  # Пустой лист для записи чисел Фибоначчи
    fib_numbers[1] = 1
    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]
    return fib_numbers[n]


# Начало отсчета
start = time.time()
print(n, "число Фибоначчи =", fib_list(n))
# Конец отсчета
end = time.time()
print("Время выполнения алгоритма:", (end - start), "сек.")
