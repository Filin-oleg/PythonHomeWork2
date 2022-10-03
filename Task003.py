# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

import math


def inputNumber(text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{text}"))
            is_OK = True
        except ValueError:
            print("Это не натуральное число! Повторите ввод")
    return number


def result_dictionary(n: int) -> list:
    new_list = [2]
    for num in range(1, n+1):
        new_list.append(num)
        new_list.append(math.ceil(new_list[-2]+(1+1/num)**num))
    new_list.pop(0)
    result_dict = {new_list[i]: new_list[i+1]
                   for i in range(0, len(new_list), 2)}
    return result_dict


n = inputNumber("Введите натуральное число: ")
my_dictionary = result_dictionary(n)
print(result_dictionary(n))