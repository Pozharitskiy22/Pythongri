# num1 = 12345
# num = num1
# a = num % 10
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
# num = num // 10
# e = num
# f = a * b * c * d * e
# g = ((a + b + c + d + e)/5)
# print("Произведение цифр числа:", num1, "=", f)
# print("Среднее арифметическое цифр числа:", num1, "=", g)


a = int(input("Введите число от 1 до 99: "))
c = a
c = c % 10
print(c)
if 11 <= a <= 14:
    print(a, "копеек")
elif a > 99:
        print("Ощибка")
else:
    if c == 1:
        print(a, "копейка")
    if 2 <= c <= 4:
        print(a, "копейки")
    if 5 <= c <= 9 or c == 0 or 11 <= a <= 14:
        print(a, "копеек")




