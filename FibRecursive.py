#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Импортирование модуля времени
import time
print("Введите n-ое число Фибоначчи, которое требуется вычислить:")
n_fib = int(input())


def fib_recursive(n_fib):
    if n_fib <= 1:
        return n_fib
    else:
        return fib_recursive(n_fib - 1) + fib_recursive(n_fib - 2)


# Начало отсчета
start = time.time()
print(n_fib, "число Фибоначчи =", fib_recursive(n_fib))
# Конец отсчета
end = time.time()
print("Время выполнения алгоритма:", (end - start))
