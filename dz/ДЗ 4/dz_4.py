# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# n = int(len(a))
#
# for i in range(n):
#
#     res = 0
#     for j in range(n):
#         if a[i] == a[j]:
#             res += a[i]
#     if res == a[i]:
#         print(a[i], end=" ")
#
# print()


# a = [int(input("-> ")) for w in range(0, int(input("n = ")))]
# print(a)
# n = int(len(a))
# for i in range(n):
#     if a[i] > a[i - 1]:
#             print(a[i], end=" ")


# a = [27] * 100
# n = int(len(a))
# res = 0
# for i in range(0, n):
#     a[i + 1] = int(input("Введите число от 1 до 100: "))
#     res += 1
#     if a[i + 1] == 0:
#         break
#     if a[i + 1] > a[0]:
#         print("Загаданное число меньше")
#
#     if a[i + 1] < a[0]:
#         print("Загаданное число больше")
#
#     if a[i + 1] == a[0]:
#
#         print("Вы угадали выбранное число с", res, "раза")
#         break
#
# print()


