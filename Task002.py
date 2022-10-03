# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def inputNumber(text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{text}"))
            is_OK = True
        except ValueError:
            print("Это не натуральное число! Повторите ввод")
    return number


def factorial(n: int) -> list:
    set = [1]
    for i in range(2, n+1):
        set.append(set[-1] * i)
    return set


number = inputNumber("Введите натуральное число: ")
print(f"Произведение чисел от 1 до введенного Вами числа = {factorial(number)}")
