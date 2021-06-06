"""
Создать функцию calc(a, b, operation). Описание входных параметров:
1. Первое число
2. Второе число
3. Действие над ними:
   1) + Сложить
   2) - Вычесть
   3) * Умножить
   4) / Разделить
   5) В остальных случаях функция должна возвращать "Операция не поддерживается"
"""
def calc(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Операция не поддерживается"
print(calc(int(input()),int(input()),input()))