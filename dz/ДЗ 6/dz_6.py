from random import randint

#  Задача #1

mas = [randint(0, 100) for i in range(20)]
print(mas)
print("Summa:", sum(mas))

#  Задача #2

# from random import randint
#
# m = [randint(0, 10) for x in range(6)]
#
# a = [[randint(0, 10) for x in range(6)] for y in range(6)]
# for i in range(len(a)):
#     if i % 2 == 0:
#         a.pop(i)
#         a.insert(i, m)
#     for b in range(len(a[i])):
#         print(a[i][b], end="\t")
#     print()


# print(m)
