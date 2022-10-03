# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


def inputNumbers(text):
    it_OK = False
    while not it_OK:
        try:
            number = int(input(f"{text}"))
            it_OK = True
        except ValueError:
            print("Это не число! Повторите ввод")
    return number


def sum(x):
    if float(x) < 0:
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number


x = inputNumbers("Введите число ")
print(f'Сумма цифр, введенного Вами числа = {sum(x)}')