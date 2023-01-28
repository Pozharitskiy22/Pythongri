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

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s)


# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
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

print("Проверка репозитория")

print("Разобрался с github")

