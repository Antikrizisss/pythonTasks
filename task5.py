"""
Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца -
и возвращает название сезона, к которому относится этот месяц.
Например, передаем 2, на выходе получаем 'Зима'.
"""
def month_to_season(n):
    if n == 12 or n == 1 or n == 2:
        return "Зима"
    elif n > 2 and n < 6:
        return "Весна"
    elif n > 5 and n < 9:
        return "Лето"
    elif n > 8 and n < 12:
        return "Осень"
print(month_to_season(int(input())))