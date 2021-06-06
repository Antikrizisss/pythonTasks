"""
Проверить, есть ли в последовательности дубликаты
lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]
"""
lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]
counter = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            counter += 1
if counter == 0:
    print("Дубликатов нет")
else:
    print("Дубликаты есть")