#  Задача #1

s = []
a = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
print("Список:", a)
for i in a:
    if i > 0:
        s.append(i)
print("Новый список, состоящий из положительных элементов: ", s)
s.sort()
#  print(s, end=" ")
print("Наибольший элемент списка:", s[-1])

print()

#  Задача #2

# a = [int(input("--> ")) for i in range(int(input("Введите элементы списка:\nn = ")))]
#
# k = int(input("Введите индекс:\nk = "))
# c = int(input("Введите значение:\nc = "))
# a.insert(k, c)
# print(a)

#  Задача #3

# n = [int(input("--> ")) for i in range(int(input("Введите элементы списка:\nn = ")))]
# print(n)
# x = int(input("Введите число:\nch = "))
# for i in range(len(n)):
#     if x == n[i]:
#         print("Число присутствует в элементах списка")
#     else:
#         print("Число отсутствует в элементах списка")
#         break
#
# print()

