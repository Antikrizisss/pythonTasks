"""
Напишите программу, которая будет выводить нечетные числа из списка и остановится, если встретит число 139
"""
lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7, 19, 50, 55, 139, 10, 11]
def main(l : list):
    for i in range(len(l)):
        if l[i] == 139:
            break
        elif l[i] % 2 != 0:
            print(l[i])
main(lst)