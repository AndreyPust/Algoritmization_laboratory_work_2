import time  # Импортирование модуля времени
print("Введите n-ое число Фибоначчи, которое требуется вычислить:")
n = int(input())

def fib_list(n):
    fib_numbers = [0]*100  # Пустой лист для записи чисел Фибоначчи
    fib_numbers[1] = 1
    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]
    return fib_numbers[n]


start = time.time()  # Начало отсчета
print(n, "число Фибоначчи =", fib_list(n))
end = time.time()  # Конец отсчета

print("Время выполнения алгоритма:", (end - start), "сек.")
