
'''Задача 32: Определить элементs массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
1
19
Вывод: [1, 9, 13, 14, 19]'''


list1 = [int(i) for i in input("Введите массив: ").split()]
max_n = int(input("max: "))
min_n = int(input("min: "))

list2 = []
for i in list1:
    if min_n <= i <= max_n:
        list2.append(i)
print(list2)


# list1 = [int(i) for i in input('Введите массив чисел через пробел: ').split(' ')]
# start_number = int(input('Введите начальное число: '))
# end_number = int(input('Введите последнее число: '))
# list2 = [i for i in list1 if start_number <= i <= end_number]
# print(list2)