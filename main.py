# name = "Elena"
# print("Hello,", name)
# age = 20
# print(age)

# a = 5
# print(type(a))
# a = "Hello"
# print(type(a))

# a = 4
# b = 5
# print(a)
# a = b
# print(a)

# print("строка символов")
# print('строка символов')

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 3)

# print(375482356823585872658726)
# print(3.75482356823585872658726)

# a = 5
# b = 7
# c = 3
# d = a + b + c
# print("Сумма:", d)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", d / 3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
#
# number = (6 + 4) * 5 ** 2 + 7
# print(number)


# num = 10
# num += 5  # num = num + 5
# print(num)
#
# num -= 3
# print(num)

# num = 4321
# print(num)
# a = num % 10
# print(a)
# num = num // 10
# print(num)
# b = num % 10
# print(b)
# num = num // 10
# print(num)
# c = num % 10
# print(c)
# num = num // 10
# print(num)
# d = num
# print(d)
# print(a, b, c, d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# print(num)
# res = num % 10 * 1000
# num = num // 10
# res += num % 10 * 100
# num = num // 10
# res += num % 10 * 10
# num = num // 10
# res += num % 10
# print("res=", res)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)

# name = input("Введите имя: ")
# print("Вас зовут", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
#
# res = num ** power
# print("Число", num, "В степени", power, "равно:", res)

# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# c = int(input("Введите число: "))
# d = int(input("Введите число: "))
#
# res12 = a + b
# res34 = c + d
#
# res = res12 / res34
# res = round(res, 2)
# print("Результат:", res)

# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
# else:
#     print("Доступ запрещён")

# a = 25
# b = 15
# if a > b:
#     print("a>b")
# if b > a:
#     print("b>a")
# else:
#     print("b==a")

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите введите третью сторону: "))
#
# if a == b == c:
#     print("Треугольник равносторонний")
#
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# a = int(input("Введите номер месяца: "))
#
# if a == 1 or a == 2 or a == 12:
#     print("Зима")
# if 3 <= a <= 5:
#     print("Весна")
# if 6 <= a <= 8:
#     print("Лето")
# if 9 <= a <= 11:
#     print("Осень")
# if a > 12:
#     print("Такого месяца нет")

# n = int(input("Введите количество ворон: "))


# if a == 1 or a == 2 or a == 12:
#     print("Зима")
# if 3 <= a <= 5:
#     print("Весна")
# if 6 <= a <= 8:
#     print("Лето")
# if 9 <= a <= 11:
#     print("Осень")
# if a > 12:
#     print("Такого месяца нет")


#  14/01


# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_2
#     case шаблон_2:
#         действие_2
#     case шаблон_n:
#         действие_n

# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case 'moderator':
#         print("Модератор")
#     case  _:
#         print("Пароль не верен

# day = 'суббота'

# match day:
# time = 14
#
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг': if 9 <= time <= 14:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной")
#     case _:
#         print("Такого дня недели не существует")

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)


# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# print("На ноль делить нельзя" if b == 0 else a / b)

# n = int(input("Введите целое число: "))
# print(5 / n)


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
# print("Код далее")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Нельзя делить на ноль")
# else:
#     print("Все нормально. Ввели числа", n, "и", m)
# finally:
#     print("Конец программы")
#
# print("Код далее")


# try:
#     n = input("Введите первое число: ")
#     m = input("Введите второе число: ")
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)

#  Циклы

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("Введите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     print(a, end=" ")
#     if a % 2:
#         res += a
#     a += 1
# print("\n", res)

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не чётное")
#         n = input("Введите целое число")
#
# if n % 2 == 0:
#     print("Чётное число")
# else:
#     print("Нечётное")

# i = 0
# while i <10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end="")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершён")


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# res = 1
# while True:
#     n = int(input("Введите положительное число: "))
#     print(n)
#     res *= n
#
#     if n == 0:
#         print(res)
#         break


# i = 0
# while i < 3:
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# a = int(input("Количество символов: "))
# b = input("Тип символа: ")
# c = int(input("Выберите ориентацию линии (0 - горизонтальная, 1 - вертикальная): "))
# i = 1
# while i <= a:
#     if c == 0:
#         print(b, end="")
#         i += 1
#     if c == 1:
#         print(b)
#         i += 1


# 15.01


# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 1
#     while j < 5:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("*", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1


# for element in collection:
#   тело цикла

# for color in 'red', 'orange', 'yellow','green', 20, 0.3:
#     print(color)

#  print(range(9)) # встроенная функция - range(start, stop, step)

# for i in range(9):
#     print(i, end=" ")
# print()

# a = int(input("Введите целое число "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 101):
#     if i % 11 == 0:
#         print(i)

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done!')

# for i in range(3):
#     for j in range(6):
#         print("*", end="")
#     print()


# w = int(input("Введите ширину прямоугольника "))
# h = int(input("Введите высоту прямоугольника "))
# symbol = input("Введите символ: ")
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()

# w = 16
# h = 4

# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h -1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# w = [letter for letter in "Hello"]
# print(w)

# Списки

# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(nums[1])
# print(nums[2])

# n = list(range(2, 100, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(n2)
# if n == n2:
#     print("списки равны")
# else:
#     print("списки разные")

#  генератор списков

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
#
# print(a)
#
# c = [i * 3 for i in "list"]
# print(c)


# a = [0] * int(input("Введите количество "))
# print(a)
# for i in range (len(a)):
#     a[i] = input('-> ')
# print(a)

# a = [input("-> ") for i in range(int(input("n = ")))] # тоже самое range(4)
# print(a)

# a = [input("-> ") for i in range(4)]
# print(a)

# a = [9, 8, 6, 4, 3]
# for i in range(len(a)):
#     print(i, ":" a[i])
# print()
# for i in a:
#     print(i)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# i = 0
# j = 0
# for i in a:
#     if i == i:
#         print(i)
# # while i < (len(a)):
# #     while j < (len(a)):
# #         if a[i] == a[j]:
# #             print("нет")
# #             j += 1
# #
# #         i += 1

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# l = len(a)
#
# for i in range(l):
#
#     res = 0
#     for j in range(l):
#         if a[i] == a[j]:
#             res += a[i]
#     if res == a[i]:
#         print(a[i])
#         # else:
#         #     res += a[i]
# print()

# a = [5, 1, 9, 7, 6, 3]
# l = len(a)
# for i in range(1, l):
#      for j in range(l):
#         if a[i] > a[j]:
#             print(a[i], end="")
#         else:
#             break
# print()

# a = [2, 9, 4, 6, 3, 5]
# n = len(a)
# i = 1

# for i in range(1, int(input("n = "))):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")
#     i += 1
#
# print()


# 21.01


#  срез

#  список [start:stop:step]

# a = [6, 3, 0, 8, 2, 7]
# print(a[1:4])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[6:])
# print(s[-1:])
# print(s[3:4])
# print(s[-3:])
#
# a = "Hello"
# print(a[1:3])
# print(list(a))
#
# a = [6, 3, 0, 8, 2, 7]
# print(a[:])
# a[1:3] = [1, 1, 1, 1]
# print(a)
# a[1:2] = [20]
#
# print(a)
# a[2] = 50
# print(a)
#
# # b = 0
# # del b
# # print(b)
#
# del a[2]
# print(a)


#  Методы списка

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# #  a[6] = 99
# a.append(99) #  добавляет один элемент в конец списка
# print(a)
#
# a.extend([5, 6, 7]) #  добавляет несколько элементов в конец существующего списка
# print(a)
# a.extend("add")
# print(a)

# a = []
# a.extend([i**2 for i in range(1, 11)])
# print(a)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s)


# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)


# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# a.insert(2, 100) #  добавляет элемент списка (второй параметр - добавляет значение) в определённое место
# (первый параметр - индекс), при этом элементы списка сдвигаются.
# a.remove(1) #  удаляет первый попавшийся элемент из списка по значению
# print(a)
# last = a.pop() #  удаляет последний элемент из списка и возвращает удалённый элемент
# second = a.pop(0) #  удаляет элемент из списка по его индексу и возвращает его
# print(a)
# print(second)
# print(last)
# a.clear() #  очищает список
# print(a)


# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# num = a.count(2) #  считает кол-во заданных значений в списке
# print(num)
#
# # ind = a.index(9) #  возвращает положение первого индекса по заданному значению
# print(ind)

# c = [1, 2, 3]
# d = c
# print("c = ", c)
# print("d =", d)
# c.append(4)
# d.insert(0, 100)
# print("c = ", c)
# print("d =", d)

# c = [1, 2, 3]
# d = c.copy() #  возвращает копию списка
# print("c = ", c)
# print("d =", d)
# c.append(4)
# d.insert(0, 100)
# print("c = ", c)
# print("d =", d)


# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# a.reverse() #  развернули элементы списка в обратном порядке
# print(a)
#
# a.sort() #  отсортировали по возрастанию
# print(a)
#
# a.sort(reverse=True) #  отсортировали по убыванию
# print(a)
#
# s = ["Виталий", "Александр", "Сергей", "Анна"]
# s.sort()
# print(s)
#
# s = ["Виталий", "Александр", "Сергей", "Анна"]
# s.sort(key=len)
# print(s)
#
# s = ["Виталий", "Александр", "Сергей", "Анна"]
# s.sort(key=len, reverse=True)
# print(s)
#
# b = sorted(a, reverse)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in range(len(a)):
#     if a[i] < 0:
#         a.pop(i)
# print(a)

# a = [5, -2, 9, 2, 1, 2, 4, 3, 2, 4]
# a.pop(1)
# print(a)
# i = 0
# a = [5, -2, 9, 2, 1, 2, 4, 3, 2, 4]
# print(len(a))
# # n = int(input("Кол-во элементов списка: "))
# while i < 9:
# # for i in range(9):
#     if a[i] > 0:
#         a.pop(i)
#         i += 1
# print(a)

# a = [2, -9, 4, 6, 3, 5]
# n = len(a)
# i = 1

#  Домашка


# s = []
# a = [int(input("Введите элемент списка ")) for i in range(int(input("Введите длину списка: ")))]
# print("Список:", a)
# for i in a:
#     if i > 0:
#         s.append(i)
# print("Новый список, состоящий из положительных элементов: ", s)
# s.sort()
# #  print(s, end=" ")
# print("Наибольший элемент списка:", s[-1])
#
# print()

# print "Hello"

# print("Проверка репозитория")
#
# print("Разобрался с github")


# 22.01

#  Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(0, 5))
# print(random.randrange(5, 15, 2))

# import random as r
#
# print(r.random())
# print(r.randint(0, 5))
# print(r.randrange(5, 15, 2))

# from random import randint, randrange
#
#
# print(randint(0, 5))
# print(randrange(5, 15, 2))


# from random import *
#
#
# print(randint(0, 5))
# print(randrange(5, 15, 2))
# print(uniform(10.5, 25.5))
# print(round(uniform(10.5, 25.5), 2))
#
# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(choice(city_list))
# print(choices(city_list, k=2))
#
#
# s = [55, 66, 77, 88, 99]
# print(choice(s))
# print(choices(s, k=2))
# shuffle(s)
# print(s)

# from random import randint
#
# mas = [i for i in range(10)]
# print(mas)
# mas = [0 for i in range(10)]
# print(mas)
# #  mas = [input("-->") for i in range(10)]
# print(mas)
# mas = [randint(0, 20) for i in range(5)]
# print(mas)


#  Функции агрегирования


# lst = [16, 0, 4, 13, 15]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

from random import randint

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# max_1 = max(mas)
# print(max_1)
# mas.remove(max_1)
# mas.insert(0, max_1)
# print(mas)

# mas = [randint(- 20, 20) for i in range(10)]
# mas.sort(reverse=True)
# print(mas)
# max_1 = max(mas)
# print(max_1)
# mas.remove(max_1)
# mas.insert(0, max_1)
# print(mas)

# mas = [randint(0, 100) for i in range(10)]
#
# print(mas)
# min_1 = min(mas)
# print(min_1)
# ind = mas.index(min_1)
#
# del mas[:ind]
# print(mas)


# lst = []
# if len(lst) == 0:
#     print("Список пустой")
# if not lst:
#     print("!!!Список пустой")


# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
#
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for i in range(n2)]
#
# print("Первый список:", a)
# print("Второй список:", b)
#
# c = a + b
# print("Третий список:", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений:", c)
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков:", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)


# k = int(input("Размер списка: "))
# s = []
# while len(s) < k:
#     w = randint(0, k-1)
#     if w not in s:
#         s.append(w)
# print(s)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # print(len(m))
# print(m)
# # print(m[1][2])
#
# # a = [2, 'Hello', 5]
# # print(a[1][1])
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
#
# for row in m:
#     # print(row)
#     for x in row:
#         print(x ** 2, end="\t\t")
#     print()


# matrix = [[0 for x in range(5)]for y in range(3)]
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# matrix = []
#
# for y in range(3):
#     new_row = []
#     for x in range(5):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()


# for x, y, z in [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4]]:
#     print(z, ")", x, "+", y, "=", x + y)


# matrix = [[randint(-20, 10) for x in range(4)]for y in range(3)]
# s = 0
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             s += 1
#     print()
#
# print(s)

# n = int(input("n= "))
# m = [[randint(0, 100) for x in range(n)]for y in range(n)]
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()
# t = m[0][0]
# for k in range(n):
#     if t > m[k][k]:
#         t = m[k][k]
# print(t)


#  29.01

# import math

# num1 = math.sqrt(4)  #  Вычисляет корень квадратный числа
# num2 = math.ceil(3.2)  #  округление в большую сторону
# num3 = math.floor(3.8) #  округляет в меньшую сторону
# num4 = math.pi #  Число Пи
#
# print(num1)
# print(num2)
# print(num3)
# print(num4)
#
# print(dir(math))

# from math import sqrt
# import math as m
# num1 = m.sqrt(4)
# # num1 = sqrt(4)
# print(num1)

# from math import pi
#
# r = int(input("Введите радиус окружности: "))
#
# s = round(2 * pi * r, 2)
# print(s)

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
#
# # print(dir(time))
# s = time.time()
# print(s)
#
# local = time.ctime()
# print(local)
#
# res = time.localtime()
# print(res)
# print(res.tm_year, ".", res.tm_mon, sep="")
#
# print(time.strftime("%d.%m.%Y"))
# print(time.strftime("Today is %B %d.%Y"))
# print(time.strftime("Сегодня %B %d.%Y"))


# pause = 2
# print("Программа запущена")
# time.sleep(pause)
# print("Программа завершена")


# text = input("Название напоминания: ")
# t = float(input("Через сколько минут:"))
# t = t * 60
# time.sleep(t)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)
#
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)
print()

# def hello(name):
#     print("Hello,", name)
#
#
# hello("Irina")
# hello("Ivan")


# def get_sum(a, b):
#     print(a + b)
#
#
# get_sum(2, 5)
# get_sum('2', '5')
#
#
# x = 2
# y = 5
#
# get_sum(x, y)


# def get_sum(a, b):
#     print("Сумма:")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
#
# print(res)


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# x = int(input("-->"))
# y = int(input("-->"))
#
#
# def res(a, b):
#     if a > b:
#         print(a + b)
#     else:
#         print(a - b)
#
#
# res(x, y)

# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cub(i))


# def change(lst):
#     #  lst[0], lst[-1] = lst[-1], lst[0]
#     a = lst.pop()  # последний элемент который мы удалили
#     b = lst.pop(0)  # первый элемент, который мы удалили
#     lst.append(b)
#     lst.insert(0, a)
#
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'л', 'о', 'н']))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(10, 5))
# print(func(5, 10))
# a = 10
# b = 5
#
# if func(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надёжный пароль")
# else:
#     print("Это не надёжный пароль")


# def get_sum(a=0, b=0, c=0, d=0):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, d=2))
# print(get_sum())
# print(get_sum(d=2, a=5))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age, end="\n\n")
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")


#  Домашняя работа
#  Задание №1

# import math
#
#
# def square(h, b, r, p):
#     print("Площадь прямоугольника:", h * b)
#     print("Площадь треугольника:", 0.5 * h * b)
#     print("Площадь круга:", round((p * r ** 2), 2))
#
#
# p = math.pi
# h = 10
# b = 16
# r = 8
# square(h, b, r, p)

# Задание №2

s = []
p = []


a = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
for i in a:
    sl = 0
    for j in range(1, 1000):
        if i % j == 0:
            sl += 1
    if sl == 2:
        p.append(i)
    elif sl > 2:
        s.append(i)

# print(p)
# print(s)
print("Min: ", min(p))
print("Max:", max(s))