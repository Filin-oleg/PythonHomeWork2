# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


def inputNumbers(text):
    isfloat = False
    while not isfloat:
        try:
            number = float(input(f"{text}"))
            isfloat = True
        except ValueError:
            print("Это не число! Повторите ввод")
    return number


def sum(x):
    if float(x) < 0:
        x = float(x) * (-1)
    sum = 0

    for i in str(x):
        if i != '.':
            sum += int(i)
    return sum


x = inputNumbers("Введите число ")
print(f'Сумма цифр, введенного Вами числа = {sum(x)}')